// Seleciona o formulário e adiciona um evento de submissão
const contactForm = document.getElementById('contactForm');

contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o comportamento padrão do formulário

    // Simulação de envio
    setTimeout(() => {
        alert('Mensagem enviada com sucesso!'); // Exibe mensagem de sucesso
        contactForm.reset(); // Reseta o formulário
    }, 1000);
});

// Função para scroll suave
const links = document.querySelectorAll('nav ul li a');

links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); // Previne o comportamento padrão
        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        targetSection.scrollIntoView({ behavior: 'smooth' }); // Scroll suave
    });
});

// Função para modal dinâmico
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
    card.addEventListener('click', function() {
        const modalContent = this.getAttribute('data-modal');
        alert('Detalhes do Projeto: ' + modalContent); // Exibe detalhes do projeto
    });
});

// Animação de fade-in ao rolar a página
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
});

const sections = document.querySelectorAll('section');
sections.forEach(section => {
    observer.observe(section);
});