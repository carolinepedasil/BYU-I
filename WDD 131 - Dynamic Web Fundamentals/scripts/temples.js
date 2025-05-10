document.getElementById('year').textContent = new Date().getFullYear();
document.getElementById('last-modified').textContent = document.lastModified;

document.getElementById('menu-toggle').addEventListener('click', function() {
    const navMenu = document.getElementById('nav-menu');
    navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
});