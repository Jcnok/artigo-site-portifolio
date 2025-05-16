// Seleciona os elementos do formulário
const form = document.getElementById('contact-form');
const feedback = document.getElementById('form-feedback');

// Adiciona evento de envio ao formulário
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o comportamento padrão do formulário

    // Simula um envio com setTimeout
    setTimeout(() => {
        feedback.innerText = 'Mensagem enviada com sucesso!';
        feedback.style.color = 'green';
        form.reset(); // Limpa o formulário
    }, 2000);
});

// Função para scroll suave
const links = document.querySelectorAll('nav a');
links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); // Previne o comportamento padrão do link
        const targetId = this.getAttribute('href');
        const target = document.querySelector(targetId);
        target.scrollIntoView({ behavior: 'smooth' }); // Scroll suave
    });
});

// Exibir modal dinâmico (exemplo simplificado)
const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach(card => {
    card.addEventListener('click', () => {
        // Aqui você pode implementar a lógica para abrir um modal com detalhes do projeto
        alert('Detalhes do projeto'); // Placeholder
    });
});