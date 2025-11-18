// internship.js
import CONFIG from "./config.js";

document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.getElementById("internshipSearchForm");
    const internshipResults = document.getElementById("internshipResults");

    searchForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const category = document.getElementById("category").value || "";
        const location = document.getElementById("location").value || "remote";

        internshipResults.innerHTML = "<p>Searching internships...</p>";

        try {
            const internships = await fetchInternships(category, location);
            displayInternships(internships);
        } catch (error) {
            console.error("Error fetching internships:", error);
            internshipResults.innerHTML = `<p class='text-danger'>Failed to load internships: ${error.message}</p>`;
        }
    });

    async function fetchInternships(category, location) {
        // Build query to include "internship" explicitly
        const query = `${category} internship in ${location}`;

        const params = new URLSearchParams({
            query: query,
            page: '1',
            num_pages: '1',
            country: 'us',
            date_posted: 'all'
        });

        const url = `https://jsearch.p.rapidapi.com/search?${params.toString()}`;

        const options = {
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': CONFIG.API_KEY,
                'X-RapidAPI-Host': 'jsearch.p.rapidapi.com'
            }
        };

        const response = await fetch(url, options);
        if (!response.ok) throw new Error(`API request failed: ${response.status}`);

        const data = await response.json();

        // Filter only results where employment type includes "Internship"
        return data?.data?.filter(job =>
            job.job_employment_type?.toLowerCase().includes("internship") ||
            job.job_title?.toLowerCase().includes("internship")
        ) || [];
    }

    function displayInternships(internships) {
        internshipResults.innerHTML = "";

        if (!internships.length) {
            internshipResults.innerHTML = "<p>No internships found. Try another search.</p>";
            return;
        }

        const row = document.createElement("div");
        row.className = "row g-4";

        internships.forEach(job => {
            const col = document.createElement("div");
            col.className = "col-md-4";
            col.innerHTML = `
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">${job.job_title || "No title"}</h5>
                        <p class="mb-1"><strong>Company:</strong> ${job.employer_name || "Unknown"}</p>
                        <p class="mb-1"><strong>Location:</strong> ${job.job_city || ""}, ${job.job_country || ""}</p>
                        <p class="mb-2"><strong>Type:</strong> ${job.job_employment_type || "Internship"}</p>
                        <a href="${job.job_apply_link || "#"}" target="_blank" class="btn btn-primary w-100">Apply Now</a>
                    </div>
                </div>
            `;
            row.appendChild(col);
        });

        internshipResults.appendChild(row);
    }
});
