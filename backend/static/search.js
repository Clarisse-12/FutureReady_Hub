document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const cards = document.querySelectorAll(".sponsor-item");

    searchInput.addEventListener("input", function () {
        const searchValue = this.value.toLowerCase().trim();

        cards.forEach(card => {
            // get the title from the <p> that has data-title
            const titleElement = card.querySelector("[data-title]");
            const title = titleElement ? titleElement.getAttribute("data-title").toLowerCase() : "";

            if (title.includes(searchValue)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});
