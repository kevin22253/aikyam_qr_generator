async function generateQR() {
    const name = document.getElementById("name").value;

    // Send data to the backend for QR code generation
    const response = await fetch('/generate_qr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name }),
    });

    if (response.ok) {
        const qrData = await response.json();
        displayQRCode(qrData);
    } else {
        alert('Failed to generate QR code. Please try again.');
    }
}

function displayQRCode(qrData) {
    const qrContainer = document.getElementById('qrContainer');
    qrContainer.innerHTML = `<img src="${qrData.qrImagePath}" alt="QR Code">`;
}
