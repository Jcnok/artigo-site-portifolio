document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário
    alert('Mensagem enviada com sucesso!');
});