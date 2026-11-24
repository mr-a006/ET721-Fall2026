const uploadForm = document.getElementById('uploadForm');
const imageInput = document.getElementById('imageInput');
const message = document.getElementById('message');
const gallery = document.querySelector('.gallery');

uploadForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        message.textContent = result.message;

        if (response.ok) {
            const card = document.createElement('div');
            card.className = 'card';

            const img = document.createElement('img');
            img.src = result.url;
            img.alt = 'Uploaded image';

            card.appendChild(img);
            gallery.appendChild(card);

            imageInput.value = '';
        }
    } catch (error) {
        message.textContent = 'An error occurred while uploading the image.';
    }
});