// Script para envio de formulário
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    alert('Mensagem enviada!'); // Exibe um alerta de confirmação
    this.reset(); // Limpa o formulário
});