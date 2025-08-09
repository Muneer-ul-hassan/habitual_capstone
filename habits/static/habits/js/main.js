document.addEventListener('DOMContentLoaded', () => {
    const logButtons = document.querySelectorAll('.log-habit');
    logButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const habitId = event.target.dataset.habitId;
            fetch(`/log/${habitId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.is_completed) {
                        event.target.classList.remove('btn-secondary');
                        event.target.classList.add('btn-success');
                        event.target.textContent = 'Completed!';
                    } else {
                        event.target.classList.remove('btn-success');
                        event.target.classList.add('btn-secondary');
                        event.target.textContent = 'Complete';
                    }
                });
        });
    });
});
