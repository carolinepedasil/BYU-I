const baseURL = "https://carolinepedasil.github.io/wdd230/";
const linksURL = `${baseURL}data/links.json`;

async function getLinks() {
    try {
        const response = await fetch(linksURL);
        if (!response.ok) throw new Error("Erro ao buscar JSON");
        const data = await response.json();
        displayLinks(data.weeks);
    } catch (error) {
        console.error("Erro ao carregar os links:", error);
    }
}

function displayLinks(weeks) {
    const list = document.querySelector("#learning-activities");
    list.innerHTML = "";

    weeks.forEach(week => {
        const weekItem = document.createElement("li");
        weekItem.textContent = week.week;

        const subList = document.createElement("ul");
        week.links.forEach(link => {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = baseURL + link.url;
            a.textContent = link.title;
            li.appendChild(a);
            subList.appendChild(li);
        });

        weekItem.appendChild(subList);
        list.appendChild(weekItem);
    });
}

getLinks();
