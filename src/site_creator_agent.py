# site_creator_agent.py
import os
from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import BaseTool
from typing import List, Optional

class SiteCreatorAgent:
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
            CreateHTMLTool(),
            CreateCSSTool(),
            CreateJSTool()
        ]
    
    def _setup_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Você é um especialista em desenvolvimento web front-end.
            Seu trabalho é criar um site de portfólio profissional e moderno.
            
            Use as ferramentas disponíveis para criar os arquivos HTML, CSS e JavaScript.
            O site deve ser responsivo, visualmente atraente e otimizado para SEO."""),
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

class CreateCSSTool(BaseTool):
    name: str = "create_css"
    description: str = "Cria o arquivo CSS para estilizar o site de portfólio"
    
    def _run(self, content: Optional[str] = None) -> str:
        if not content:
            return "Por favor, forneça o conteúdo CSS para criar o arquivo."
        
        os.makedirs("site/css", exist_ok=True)
        with open("site/css/style.css", "w") as f:
            f.write(content)
        return "Arquivo CSS criado com sucesso em site/css/style.css"

class CreateJSTool(BaseTool):
    name: str = "create_js"
    description: str = "Cria o arquivo JavaScript para adicionar interatividade ao site"
    
    def _run(self, content: Optional[str] = None) -> str:
        if not content:
            return "Por favor, forneça o conteúdo JavaScript para criar o arquivo."
        
        os.makedirs("site/js", exist_ok=True)
        with open("site/js/main.js", "w") as f:
            f.write(content)
        return "Arquivo JavaScript criado com sucesso em site/js/main.js"
class CreateHTMLTool(BaseTool):
    name: str = "create_html"
    description: str = "Cria o arquivo HTML principal do site de portfólio"
    
    def _run(self, content: Optional[str] = None) -> str:
        if not content:
            return "Por favor, forneça o conteúdo HTML para criar o arquivo."
        
        os.makedirs("site", exist_ok=True)
        with open("site/index.html", "w") as f:
            f.write(content)
        return "Arquivo HTML criado com sucesso em site/index.html"