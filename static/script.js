document.getElementById('questionForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Get the question from the form
    const question = document.getElementById('question').value;

    // Send the question to the server
    fetch('/process_question', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the answer on the page
        document.getElementById('answer').innerHTML = `<p>${data.answer}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
