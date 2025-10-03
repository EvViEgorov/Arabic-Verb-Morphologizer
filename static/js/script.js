document.getElementById('verbForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем перезагрузку страницы

    const formData = new FormData(this);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Отображаем результат
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <h2>Результат:</h2>
            <p><strong>Начальная форма:</strong> ${data.root}</p>
            <p><strong>Грамматические показатели:</strong></p>
            <ul>
                <li>Время: ${data.features.время}</li>
                <li>Лицо: ${data.features.лицо}</li>
                <li>Число: ${data.features.число}</li>
                <li>Род: ${data.features.род}</li>
            </ul>
        `;
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
});