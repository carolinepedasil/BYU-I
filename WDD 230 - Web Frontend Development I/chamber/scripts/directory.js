const url = 'data/members.json';
const directory = document.getElementById('directory');
const gridBtn = document.getElementById('grid-view');
const listBtn = document.getElementById('list-view');

async function getMembers() {
    const response = await fetch(url);
    const members = await response.json();
    displayMembers(members);
}

function displayMembers(members) {
    directory.innerHTML = '';
    members.forEach(member => {
        const card = document.createElement('div');
        card.classList.add('member');

        card.innerHTML = `
            <img src="images/${member.image}" alt="${member.name}">
            <h3>${member.name}</h3>
            <p>${member.address}</p>
            <p>${member.phone}</p>
            <a href="${member.website}" target="_blank">${member.website}</a>
            <p><strong>${member.membership}</strong></p>
            <p>${member.description}</p>
        `;

        directory.appendChild(card);
    });
}

gridBtn.addEventListener('click', () => {
    directory.classList.add('grid-view');
    directory.classList.remove('list-view');
});

listBtn.addEventListener('click', () => {
    directory.classList.add('list-view');
    directory.classList.remove('grid-view');
});

getMembers();
