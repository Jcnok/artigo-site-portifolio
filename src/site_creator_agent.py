# site_creator_agent.py
import os
from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import BaseTool
from typing import List, Optional, Any
from pydantic import Field

class SiteCreatorAgent:
    def __init__(self):
        self.llm = self._setup_llm()
        self.tools = self._setup_tools()
        self.agent = self._setup_agent()
    
    def _setup_llm(self) -> AzureChatOpenAI:
        return AzureChatOpenAI(
            openai_api_version="2023-05-15",
            azure_deployment=os.getenv("DEPLOYMENT_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.3
        )
    
    def _setup_tools(self) -> List[BaseTool]:
        return [
            CreateHTMLTool(llm=self.llm),
            CreateCSSTool(llm=self.llm),
            CreateJSTool(llm=self.llm)
        ]
    
    def _setup_agent(self) -> AgentExecutor:
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Você é um gerador especializado em sites de portfólio. Regras absolutas:
             1. Estrutura semântica HTML5 rigorosa
             2. CSS em 'css/style.css'
             3. JavaScript em 'js/main.js'
             4. Layout responsivo com media queries
             5. Seguir exatamente o modelo de https://jcnok.github.io/portfolio/"""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True
        )
    
    def run(self, query: str) -> Any:
        return self.agent.invoke({"input": query})

class CreateHTMLTool(BaseTool):
    name: str = "create_html"
    description: str = "Cria o arquivo HTML principal"
    llm: AzureChatOpenAI = Field(default_factory=AzureChatOpenAI)

    def _run(self, content: Optional[str] = None, **kwargs: Any) -> str:
        prompt = """Gere HTML para um portfolio profissional com:
        1. Header fixo com menu hambúrguer
        2. Seção Hero com grid 50/50
        3. Seção Projetos com 3 cards
        4. Formulário de contato válido
        5. Links corretos para CSS/JS"""
        
        content = self.llm.invoke(prompt).content
        
        essential_elements = ['<header', '<section class="hero"', 'projects-grid', '<form id="contact-form"']
        for elem in essential_elements:
            if elem not in content:
                content = content.replace('<body>', f'<body>\n<!-- {elem} missing -->')
        
        os.makedirs("site", exist_ok=True)
        with open("site/index.html", "w", encoding="utf-8") as f:
            f.write(content)
        return "HTML gerado com sucesso"

class CreateCSSTool(BaseTool):
    name: str = "create_css"
    description: str = "Cria o arquivo CSS de estilos"
    llm: AzureChatOpenAI = Field(default_factory=AzureChatOpenAI)

    def _run(self, content: Optional[str] = None, **kwargs: Any) -> str:
        prompt = """Gere CSS para:
        1. Design responsivo mobile-first
        2. Grid/Flexbox layouts
        3. Animações suaves
        4. Media queries para mobile
        5. Estilos do modelo de referência"""
        
        content = self.llm.invoke(prompt).content
        
        required_styles = ['.projects-grid', '@media', '.hero', 'transform']
        for style in required_styles:
            if style not in content:
                content += f"\n/* {style} missing */"
        
        os.makedirs("site/css", exist_ok=True)
        with open("site/css/style.css", "w", encoding="utf-8") as f:
            f.write(content)
        return "CSS gerado com sucesso"

class CreateJSTool(BaseTool):
    name: str = "create_js"
    description: str = "Cria o arquivo JavaScript"
    llm: AzureChatOpenAI = Field(default_factory=AzureChatOpenAI)

    def _run(self, content: Optional[str] = None, **kwargs: Any) -> str:
        prompt = """Gere JavaScript para:
        1. Scroll suave
        2. Validação de formulário
        3. Carregamento dinâmico de projetos
        4. Interações do menu mobile"""
        
        content = self.llm.invoke(prompt).content
        
        if 'addEventListener' not in content:
            content = "// Event listeners\n" + content
        
        os.makedirs("site/js", exist_ok=True)
        with open("site/js/main.js", "w", encoding="utf-8") as f:
            f.write(content)
        return "JS gerado com sucesso"