document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-training-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {

            const training_id = this.getAttribute('data-training-id');

            if (confirm(`Are you sure you want to delete training ID ${training_id}?`)) {

                const deleteLink = `/training/delete/${training_id}`;

                fetch(deleteLink, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => {
                    if (response.redirected) {
                        // If flask redirects
                        window.location.href = response.url;
                    } else if (response.ok) {
                        // Reload to reflect deletion
                        window.location.reload();
                    } else {
                        alert('Failed to delete training.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An unexpected error occurred during deletion.');
                });
            }
        });
    });
});
