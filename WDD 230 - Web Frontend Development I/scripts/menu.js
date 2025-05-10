document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menu");
    
    menuToggle.addEventListener("click", function () {
        menu.classList.toggle("open");
        menuToggle.textContent = menu.classList.contains("open") ? "✖" : "☰";
    });
});