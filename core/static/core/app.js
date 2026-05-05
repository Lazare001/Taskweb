document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('ai-form');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = submitBtn.querySelector('.loader');
    const responseContainer = document.getElementById('response-container');
    const responseText = document.getElementById('ai-response');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Show loading state
        submitBtn.disabled = true;
        btnText.textContent = 'მუშავდება...';
        loader.classList.remove('hidden');
        responseContainer.classList.add('hidden');
        responseText.textContent = '';

        // Add an artificial delay to simulate AI processing and show off the loader
        await new Promise(resolve => setTimeout(resolve, 800));

        const formData = {
            task_type: document.getElementById('task_type').value,
            business_name: document.getElementById('business_name').value,
            business_type: document.getElementById('business_type').value,
            user_prompt: document.getElementById('user_prompt').value
        };

        try {
            const response = await fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (data.status === 'success') {
                responseText.textContent = data.response;
                responseContainer.classList.remove('hidden');
            } else {
                responseText.textContent = 'შეცდომა მოხდა: ' + data.message;
                responseContainer.classList.remove('hidden');
            }
        } catch (error) {
            responseText.textContent = 'ქსელის შეცდომა. გთხოვთ სცადოთ თავიდან.';
            responseContainer.classList.remove('hidden');
        } finally {
            // Reset button state
            submitBtn.disabled = false;
            btnText.textContent = 'დავალების მიცემა';
            loader.classList.add('hidden');
        }
    });
});
