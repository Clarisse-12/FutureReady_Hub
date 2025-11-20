document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-internship-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {

            const internship_id = this.getAttribute('data-internship-id');

            if (confirm(`Are you sure you want to delete internship ID ${internship_id}?`)) {

                const deleteLink = `/internship/delete/${internship_id}`;

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
                        alert('Failed to delete internship.');
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
