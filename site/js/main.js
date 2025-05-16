// Seleciona o formulário e adiciona um evento de submit
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio padrão do formulário

    // Simula um envio com setTimeout
    setTimeout(() => {
        alert('Mensagem enviada com sucesso!');
        contactForm.reset(); // Reseta o formulário
    }, 1000);
});

// Função para scroll suave
const smoothScrollLinks = document.querySelectorAll('nav ul li a');
smoothScrollLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Previne o comportamento padrão
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Modal dinâmico para projetos (exemplo básico)
const projects = [
    {
        title: 'Projeto 1',
        image: 'https://placehold.co/300x200',
        tech: ['HTML', 'CSS', 'JavaScript'],
        description: 'Descrição do Projeto 1'
    },
    // Adicione mais projetos aqui
];

const projectGrid = document.querySelector('.project-grid');
projects.forEach(project => {
    const card = document.createElement('div');
    card.className = 'project-card';
    card.innerHTML = `
        <img src="${project.image}" alt="${project.title}">
        <h3>${project.title}</h3>
        <div class="project-tech">
            ${project.tech.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
        </div>
    `;

    card.addEventListener('click', () => {
        alert(project.description); // Exibe descrição do projeto em um modal
    });

    projectGrid.appendChild(card);
});