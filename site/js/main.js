// JavaScript para interatividade do portfólio

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Previne o envio do formulário
        alert('Mensagem enviada!'); // Simulação de envio
        form.reset(); // Reseta o formulário
    });
});