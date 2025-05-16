document.addEventListener('DOMContentLoaded', function() {
    // Scroll suave para links de navegação
    const links = document.querySelectorAll('nav a');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Modal dinâmico para projetos
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('click', function() {
            // Aqui você pode colocar código para abrir um modal com detalhes do projeto
            alert('Detalhes do projeto!'); // MODIFIQUE AQUI
        });
    });

    // Validação de formulário
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Previne o comportamento padrão do formulário
        const feedback = document.getElementById('feedback');
        feedback.classList.remove('hidden');
        setTimeout(() => {
            feedback.classList.add('hidden');
        }, 3000); // Simula o envio
    });
});