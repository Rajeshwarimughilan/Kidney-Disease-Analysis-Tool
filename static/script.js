document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Show spinner
    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    document.querySelector('.container').appendChild(spinner);

    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <h2>Result</h2>
            <p><strong>Name:</strong> ${data.name}</p>
            <p><strong>Age:</strong> ${data.age}</p>
            <p><strong>Phone:</strong> ${data.phone}</p>
            <p><strong>Prediction:</strong> ${data.result}</p>
            <button id="generateReportButton">Generate Report</button>
        `;
        // Hide spinner
        spinner.remove();

        // Add event listener for the "Generate Report" button
        document.getElementById('generateReportButton').addEventListener('click', function() {
            // Show full report
            resultDiv.innerHTML += `
                <h2>Full Report</h2>
                <p><strong>Name:</strong> ${data.name}</p>
                <p><strong>Email:</strong> ${data.email}</p>
                <p><strong>Phone:</strong> ${data.phone}</p>
                <p><strong>Age:</strong> ${data.age}</p>
                <p><strong>Sex:</strong> ${data.sex}</p>
                <p><strong>Blood Pressure:</strong> ${data.bloodPressure}</p>
                <p><strong>Blood Sugar:</strong> ${data.bloodSugar}</p>
                <p><strong>Creatinine:</strong> ${data.creatinine}</p>
                <p><strong>Urea:</strong> ${data.urea}</p>
                <p><strong>Hemoglobin:</strong> ${data.hemoglobin}</p>
                <p><strong>WBC:</strong> ${data.wbc}</p>
                <p><strong>Diabetes Status:</strong> ${data.diabetes}</p>
                <p><strong>Hypertension Status:</strong> ${data.hypertension}</p>
                <p><strong>Appetite Changes:</strong> ${data.appetite}</p>
                <p><strong>Swelling:</strong> ${data.swelling}</p>
                <p><strong>Anemia:</strong> ${data.anemia}</p>
                <p><strong>Cholesterol:</strong> ${data.cholesterol}</p>
                <p><strong>Prediction:</strong> ${data.result}</p>
            `;
        });
    })
    .catch(error => {
        console.error('Error:', error);
        // Hide spinner
        spinner.remove();
    });
});
