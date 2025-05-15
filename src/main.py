# main.py
from site_creator_agent import SiteCreatorAgent
from devops_agent import DevOpsAgent
from dotenv import load_dotenv
import os

def validate_environment():
    required_vars = [
        "AZURE_OPENAI_API_KEY",
        "GITHUB_USERNAME",
        "GITHUB_EMAIL",
        "GITHUB_TOKEN",
        "GITHUB_REPO"
    ]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        print(f"⚠️ Variáveis de ambiente obrigatórias não definidas: {', '.join(missing)}")
        print("Por favor, configure-as no arquivo .env e tente novamente.")
        return False
    return True

def main():
    load_dotenv()
    
    if not validate_environment():
        return
    
    print("🚀 Iniciando sistema de portfólio automatizado com IA")
    
    # Inicializar agentes
    site_creator = SiteCreatorAgent()
    devops_agent = DevOpsAgent()
    
    # Etapa 1: Criar o site de portfólio
    print("\n📝 Agente Criador de Site em ação...")
    site_result = site_creator.run(
        "Crie um site de portfólio profissional para um desenvolvedor Python especializado em IA. "
        "O site deve ter seções para apresentação pessoal, projetos, habilidades e contato. "
        "Use um design moderno, responsivo e otimizado para SEO."
    )
    print(f"Resultado do Agente Criador: {site_result}")
    
    # Etapa 2: Configurar Git e GitHub Actions
    print("\n🔧 Agente DevOps em ação...")
    devops_result = devops_agent.run(
        "Configure um repositório Git para este projeto, comite as mudanças e "
        "configure o GitHub Actions para fazer deploy automático no GitHub Pages "
        "sempre que houver um push para a branch main."
    )
    print(f"Resultado do Agente DevOps: {devops_result}")
    
    print("\n✅ Sistema de portfólio automatizado concluído com sucesso!")
    print("Seu site está pronto e configurado para deploy automático no GitHub Pages.")
    print(f"Acesse: https://{os.getenv('GITHUB_USERNAME')}.github.io/{os.getenv('GITHUB_REPO')}")

if __name__ == "__main__":
    main()
