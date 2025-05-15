# devops_agent.py
import os
import git
import yaml
from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import BaseTool

class DevOpsAgent:
    def __init__(self):
        self.llm = self._setup_llm()
        self.tools = self._setup_tools()
        self.agent = self._setup_agent()
        
    def _setup_llm(self):
        return AzureChatOpenAI(
            openai_api_version="2025-01-01-preview",
            azure_deployment=os.getenv("DEPLOYMENT_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.7
        )
    
    def _setup_tools(self):
        return [
            InitGitTool(),
            CommitChangesTool(),
            SetupGitHubActionsTool(),
            PushToGitHubTool()
        ]
    
    def _setup_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Você é um especialista em DevOps e automação de CI/CD.
            Seu trabalho é configurar um sistema de controle de versão e deploy automático para um site de portfólio.
            
            Use as ferramentas disponíveis para inicializar o Git, comitar mudanças, configurar GitHub Actions e fazer push para o GitHub."""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )
    
    def run(self, query):
        return self.agent.invoke({"input": query})

class InitGitTool(BaseTool):
    name: str = "initialize_git"
    description: str = "Inicializa um repositório Git local"
    
    def _run(self) -> str:
        try:
            repo = git.Repo.init(os.getcwd())
            return "Repositório Git inicializado com sucesso"
        except Exception as e:
            return f"Erro ao inicializar repositório Git: {str(e)}"

class CommitChangesTool(BaseTool):
    name: str = "commit_changes"
    description: str = "Adiciona e comita mudanças no repositório Git"
    
    def _run(self, message: str = "Atualização automática do site de portfólio") -> str:
        try:
            repo = git.Repo(os.getcwd())
            repo.git.add(all=True)
            repo.git.config('user.name', os.getenv("GITHUB_USERNAME"))
            repo.git.config('user.email', os.getenv("GITHUB_EMAIL"))
            repo.git.commit('-m', message)
            return f"Mudanças commitadas com sucesso: {message}"
        except Exception as e:
            return f"Erro ao comitar mudanças: {str(e)}"

class SetupGitHubActionsTool(BaseTool):
    name: str = "setup_github_actions"
    description: str = "Configura o GitHub Actions para CI/CD"
    
    def _run(self) -> str:
        # Obter o diretório raiz do projeto (um nível acima do diretório src)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        workflow_dir = os.path.join(project_root, '.github', 'workflows')
        os.makedirs(workflow_dir, exist_ok=True)        
        
        workflow_content = {
            'name': 'Deploy to GitHub Pages',
            'on': {
                'push': {
                    'branches': ['main']
                }
            },
            'jobs': {
                'build-and-deploy': {
                    'runs-on': 'ubuntu-latest',
                    'steps': [
                        {
                            'name': 'Checkout',
                            'uses': 'actions/checkout@v3'
                        },
                        {
                            'name': 'Deploy to GitHub Pages',
                            'uses': 'JamesIves/github-pages-deploy-action@v4',
                            'with': {
                                'folder': 'site'
                            }
                        }
                    ]
                }
            }
        }
        
        with open(os.path.join(workflow_dir, 'deploy.yml'), 'w') as f:
            yaml.dump(workflow_content, f, default_flow_style=False)
        
        return "GitHub Actions configurado com sucesso para deploy automático"

class PushToGitHubTool(BaseTool):
    name: str = "push_to_github"
    description: str = "Envia as mudanças para o GitHub"
    
    def _run(self, remote_url: str = None) -> str:
        if not remote_url:
            remote_url = f"https://{os.getenv('GITHUB_TOKEN')}@github.com/{os.getenv('GITHUB_USERNAME')}/{os.getenv('GITHUB_REPO')}.git"
        try:
            repo = git.Repo(os.getcwd())
            
            # Verificar se o remote já existe
            try:
                repo.git.remote('add', 'origin', remote_url)
            except git.GitCommandError:
                # Remote já existe, atualizando URL
                repo.git.remote('set-url', 'origin', remote_url)
            
            repo.git.push('--set-upstream', 'origin', 'main')
            return "Mudanças enviadas para o GitHub com sucesso"
        except Exception as e:
            return f"Erro ao enviar mudanças para o GitHub: {str(e)}"
