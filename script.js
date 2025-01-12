document.getElementById('submit').addEventListener('click', async () => {
    const symptoms = document.getElementById('symptoms').value;

    if (!symptoms) {
        alert('Please enter symptoms!');
        return;
    }

    try {
        const response = await fetch('/diagnose', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ symptoms })
        });

        const data = await response.json();
        document.getElementById('diagnosis').innerText = `Disease: ${data.disease}`;
        document.getElementById('precautions').innerText = `Precautions: ${data.precautions.join(', ')}`;
        document.getElementById('doctors').innerText = `Nearby Doctors: ${data.doctors}`;
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching the data.');
    }
});
