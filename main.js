// Camera functionality for registration
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('capture');

if (captureBtn) {
    captureBtn.addEventListener('click', function() {
        canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
        canvas.style.display = 'block';
        
        // Convert to blob and upload
        canvas.toBlob(function(blob) {
            const formData = new FormData();
            formData.append('image', blob, 'capture.jpg');
            
            fetch('/register', {
                method: 'POST',
                body: formData
            });
        });
    });
}

// Start camera
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            if (video) video.srcObject = stream;
        })
        .catch(function(error) {
            console.error('Camera error:', error);
        });
}

// Export to CSV
document.getElementById('export-csv')?.addEventListener('click', function() {
    window.location.href = '/export_csv';
});

// Refresh page
document.getElementById('refresh')?.addEventListener('click', function() {
    location.reload();
});
