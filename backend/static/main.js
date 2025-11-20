//main.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize search functionality
    initSearchForms();
});

function initSearchForms() {
    //internship form
    const internshipForm = document.getElementById('internshipSearchForm');
    if (internshipForm) {
        internshipForm.addEventListener('submit', function(e) {
            e.preventDefault();
            searchInternships(this);
        });
    }

    //training form
    const trainingForm = document.getElementById('trainingSearchForm');
    if (trainingForm) {
        trainingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            searchTraining(this);
        });
    }
}
//search internship
async function searchInternships(form) {
    const formData = new FormData(form);
    const params = new URLSearchParams();
    
    for (const [key, value] of formData.entries()) {
        if (value) params.append(key, value);
    }

    showLoading(true);
    
    try {
        const response = await fetch(`/search/internships?${params}`);
        const data = await response.json();
        
        if (data.success) {
            displayResults(data.data, 'internship');
        } else {
            showError('Search failed: ' + data.error);
        }
    } catch (error) {
        showError('Network error: ' + error.message);
    } finally {
        showLoading(false);
    }
}
//search training
async function searchTraining(form) {
    const formData = new FormData(form);
    const params = new URLSearchParams();
    
    for (const [key, value] of formData.entries()) {
        if (value) params.append(key, value);
    }

    showLoading(true);
    
    try {
        const response = await fetch(`/search/training?${params}`);
        const data = await response.json();
        
        if (data.success) {
            displayResults(data.data, 'training');
        } else {
            showError('Search failed: ' + data.error);
        }
    } catch (error) {
        showError('Network error: ' + error.message);
    } finally {
        showLoading(false);
    }
}
//display all results
function displayResults(results, type) {
    const resultsContainer = document.getElementById('searchResults');
    const resultCount = document.getElementById('resultCount');
    
    resultCount.textContent = `${results.length} ${type}(s) found`;
    
    if (results.length === 0) {
        resultsContainer.innerHTML = `
            <div class="text-center text-muted py-5">
                <p>No ${type}s found matching your criteria</p>
                <small>Try adjusting your search filters</small>
            </div>
        `;
        return;
    }
    
    let html = '';
    
    results.forEach(item => {
        if (type === 'internship') {
            html += createInternshipCard(item);
        } else {
            html += createTrainingCard(item);
        }
    });
    
    resultsContainer.innerHTML = html;
}
//create intenship card
function createInternshipCard(internship) {
    return `
        <div class="card mb-3 opportunity-card">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-start">
                    <div>
                        <h6 class="card-title mb-1">${internship.title}</h6>
                        <p class="card-text mb-1">
                            <small class="text-muted">🏢 ${internship.company}</small>
                        </p>
                        <p class="card-text mb-1">
                            <small class="text-muted">📍 ${internship.location}</small>
                        </p>
                        <p class="card-text mb-2">
                            <small class="text-muted">📊 ${internship.salary}</small>
                        </p>
                    </div>
                    <span class="badge bg-primary">Internship</span>
                </div>
                <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">Deadline: ${internship.posted}</small>
                    <a href="${internship.apply_url}" target="_blank" class="btn btn-sm btn-primary">
                        Apply Now
                    </a>
                </div>
            </div>
        </div>
    `;
}
//create training form
function createTrainingCard(course) {
    const freeBadge = course.is_free ? '<span class="free-badge">FREE</span>' : '';
    
    return `
        <div class="card mb-3 training-card">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-start">
                    <div>
                        <h6 class="card-title mb-1">${course.title} ${freeBadge}</h6>
                        <p class="card-text mb-1">
                            <small class="text-muted">🏫 ${course.provider}</small>
                        </p>
                        <p class="card-text mb-1">
                            <small class="text-muted">⏱️ ${course.duration} • ${course.level}</small>
                        </p>
                        <p class="card-text mb-2">
                            <small class="text-muted">⭐ ${course.rating}/5.0</small>
                        </p>
                    </div>
                    <span class="badge bg-success">Training</span>
                </div>
                <p class="card-text small">${course.description}</p>
                <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">Instructor: ${course.instructor}</small>
                    <a href="${course.enroll_url}" target="_blank" class="btn btn-sm btn-success">
                        Enroll Now
                    </a>
                </div>
            </div>
        </div>
    `;
}
//show search loading
function showLoading(show) {
    const buttons = document.querySelectorAll('button[type="submit"]');
    buttons.forEach(button => {
        if (show) {
            button.disabled = true;
            button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Searching...';
        } else {
            button.disabled = false;
            if (button.closest('#internshipSearchForm')) {
                button.textContent = 'Search Internships';
            } else {
                button.textContent = 'Search Courses';
            }
        }
    });
}
//if error occur it display what exactly is the problem
function showError(message) {
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = `
        <div class="alert alert-danger">
            <strong>Error:</strong> ${message}
        </div>
    `;
}