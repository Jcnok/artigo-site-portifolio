// Seleciona todos os links de navegação
const links = document.querySelectorAll('nav a');

// Adiciona evento de clique para cada link
links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); // Previne o comportamento padrão
        const targetId = this.getAttribute('href'); // Obtém o ID do destino
        const targetElement = document.querySelector(targetId); // Seleciona o elemento alvo
        targetElement.scrollIntoView({ behavior: 'smooth' }); // Rolagem suave
    });
});

// Função para abrir o modal
function openModal(content) {
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = `<div class='modal-content'><span class='close'>&times;</span><p>${content}</p></div>`;
    document.body.appendChild(modal);

    // Fecha o modal ao clicar no X
    modal.querySelector('.close').onclick = function() {
        modal.remove();
    };
}

// Adiciona evento de clique nos cards de projeto
const projetoCards = document.querySelectorAll('.projeto-card');
projetoCards.forEach(card => {
    card.addEventListener('click', function() {
        const content = this.getAttribute('data-modal-content');
        openModal(content);
    });
});

// Validação do formulário
const contactForm = document.getElementById('contact-form');
const formFeedback = document.getElementById('form-feedback');
contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Previne o comportamento padrão

    // Simulação de envio com setTimeout
    setTimeout(() => {
        formFeedback.textContent = 'Mensagem enviada com sucesso!';
        contactForm.reset();
    }, 2000);
});