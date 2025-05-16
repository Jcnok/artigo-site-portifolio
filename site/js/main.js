document.addEventListener('DOMContentLoaded', () => {
    // Scroll suave para links
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Modal dinâmico
    const modals = document.querySelectorAll('.modal');
    const cards = document.querySelectorAll('.card');
    const closeModal = document.querySelectorAll('.close');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            const modalId = card.getAttribute('data-modal');
            document.getElementById(modalId).style.display = 'block';
        });
    });

    closeModal.forEach(close => {
        close.addEventListener('click', () => {
            close.parentElement.parentElement.style.display = 'none';
        });
    });

    // Validação do formulário
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Previne o comportamento padrão
        const feedback = document.getElementById('feedback');
        feedback.innerText = 'Enviando...';
        setTimeout(() => {
            feedback.innerText = 'Mensagem enviada com sucesso!';
            form.reset();
        }, 2000);
    });
});