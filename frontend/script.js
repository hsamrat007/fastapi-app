document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    // Convert checkbox value to boolean
    data.smoker = data.smoker === 'on';

    // Convert numeric values
    data.age = parseInt(data.age);
    data.weight = parseFloat(data.weight);
    data.height = parseFloat(data.height);
    data.income_lpa = parseFloat(data.income_lpa);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const resultDiv = document.getElementById('result');
        if (result.prediction) {
            resultDiv.innerHTML = `Predicted Insurance Premium: ${result.prediction}`;
        } else {
            resultDiv.innerHTML = 'Error: Could not get a prediction.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'An error occurred. Please check the console.';
    });
});
