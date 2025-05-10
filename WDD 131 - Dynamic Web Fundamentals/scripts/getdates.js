document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("currentyear").textContent = new Date().getFullYear();
    let lastModifiedElement = document.getElementById("lastModified");
    lastModifiedElement.textContent = "Last Modification: " + document.lastModified;
    lastModifiedElement.style.color = "yellow";
});
