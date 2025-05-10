document.addEventListener("DOMContentLoaded", () => {
    const visitCounter = document.getElementById("visit-counter");
    let visits = localStorage.getItem("pageVisits");

    if (visits === null) {
        visits = 1;
    } else {
        visits = parseInt(visits) + 1;
    }

    localStorage.setItem("pageVisits", visits);
    visitCounter.textContent = visits;
});
