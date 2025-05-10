const messageEl = document.getElementById('visit-message');
const lastVisit = localStorage.getItem('lastVisit');
const now = Date.now();

if (!lastVisit) {
    messageEl.textContent = "Welcome! Let us know if you have any questions.";
} else {
    const difference = now - Number(lastVisit);
    const days = Math.floor(difference / (1000 * 60 * 60 * 24));

    if (days === 0) {
        messageEl.textContent = "Back so soon! Awesome!";
    } else {
        messageEl.textContent = `You last visited ${days} day${days > 1 ? 's' : ''} ago.`;
    }
}

localStorage.setItem('lastVisit', now);
