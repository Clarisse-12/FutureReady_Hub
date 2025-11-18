// training.js
import CONFIG from "./trainingconfig.js";

document.addEventListener("DOMContentLoaded", () => {
    const trainingForm = document.getElementById("trainingSearchForm");
    const trainingResults = document.getElementById("trainingResults");

    trainingForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const query = document.getElementById("trainingQuery").value.trim();
        const level = document.querySelector("select[name='level']").value;
        const location = document.querySelector("select[name='location']").value;
        const freeOnly = document.getElementById("freeOnly").checked;
        const withCertification = document.getElementById("withCertification").checked;

        trainingResults.innerHTML = "<p>Searching courses...</p>";

        try {
            const courses = await fetchCourses();
            const filtered = filterCourses(courses, freeOnly, withCertification, level, location, query);
            displayCourses(filtered);
        } catch (error) {
            console.error("Error fetching courses:", error);
            trainingResults.innerHTML = `<p class='text-danger'>Failed to load courses: ${error.message}</p>`;
        }
    });

    // Fetch courses from udemy-free-courses API
    async function fetchCourses() {
        const params = new URLSearchParams({
            id: 288,         // Default category ID (Development)
            pagination: 1
        });

        const url = `https://udemy-free-courses.p.rapidapi.com/courses/?${params}`;

        const options = {
            method: "GET",
            headers: {
                "x-rapidapi-key": CONFIG.API_KEY,
                "x-rapidapi-host": "udemy-free-courses.p.rapidapi.com"
            }
        };

        const response = await fetch(url, options);
        if (!response.ok) throw new Error(`API request failed: ${response.status}`);

        const data = await response.json();

        return data.courses || [];
    }

    // Filter courses
    function filterCourses(courses, freeOnly, withCertification, level, location, query) {
        return courses.filter(course => {
            const isFree = course.is_paid === false;

            if (freeOnly && !isFree) return false;

            // Udemy courses have certificate by default, so skip this
            if (withCertification && false) return false;

            if (level && course.instructional_level_simple.toLowerCase() !== level.toLowerCase()) return false;

            if (location && location !== "remote") return false;

            if (query && !course.title.toLowerCase().includes(query.toLowerCase())) return false;

            return true;
        });
    }

    // Display courses
    function displayCourses(courses) {
        trainingResults.innerHTML = "";

        if (!courses.length) {
            trainingResults.innerHTML = "<p>No courses found. Try different keywords.</p>";
            return;
        }

        const row = document.createElement("div");
        row.className = "row g-4";

        courses.forEach(course => {
            const col = document.createElement("div");
            col.className = "col-md-4";

            col.innerHTML = `
                <div class="card h-100 shadow-sm">
                    <img src="${course.image_480x270 || course.image_url}" class="card-img-top" alt="Course Image">
                    <div class="card-body">
                        <h5 class="card-title">${course.title || "Untitled Course"}</h5>
                        <p><strong>Price:</strong> ${course.is_paid ? "Paid" : "Free"}</p>
                        <p><strong>Rating:</strong> ⭐ ${course.rating || course.avg_rating || "N/A"}</p>
                        <p><strong>Level:</strong> ${course.instructional_level_simple || "All Levels"}</p>
                        <p><strong>Duration:</strong> ${course.content_info_short || "N/A"}</p>
                        <a href="${course.course_url || course.url}" target="_blank" class="btn btn-success w-100">View Course</a>
                    </div>
                </div>
            `;

            row.appendChild(col);
        });

        trainingResults.appendChild(row);
    }
});
