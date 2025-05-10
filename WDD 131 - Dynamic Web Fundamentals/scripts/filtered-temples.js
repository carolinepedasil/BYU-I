const temples = [
    {
      templeName: "Aba Nigeria",
      location: "Aba, Nigeria",
      dedicated: "2005, August, 7",
      area: 11500,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/aba-nigeria/400x250/aba-nigeria-temple-lds-273999-wallpaper.jpg"
    },
    {
      templeName: "Manti Utah",
      location: "Manti, Utah, United States",
      dedicated: "1888, May, 21",
      area: 74792,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/manti-utah/400x250/manti-temple-768192-wallpaper.jpg"
    },
    {
      templeName: "Payson Utah",
      location: "Payson, Utah, United States",
      dedicated: "2015, June, 7",
      area: 96630,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/payson-utah/400x225/payson-utah-temple-exterior-1416671-wallpaper.jpg"
    },
    {
      templeName: "Yigo Guam",
      location: "Yigo, Guam",
      dedicated: "2020, May, 2",
      area: 6861,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/yigo-guam/400x250/yigo_guam_temple_2.jpg"
    },
    {
      templeName: "Washington D.C.",
      location: "Kensington, Maryland, United States",
      dedicated: "1974, November, 19",
      area: 156558,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/washington-dc/400x250/washington_dc_temple-exterior-2.jpeg"
    },
    {
      templeName: "Lima Perú",
      location: "Lima, Perú",
      dedicated: "1986, January, 10",
      area: 9600,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/lima-peru/400x250/lima-peru-temple-evening-1075606-wallpaper.jpg"
    },
    {
      templeName: "Mexico City Mexico",
      location: "Mexico City, Mexico",
      dedicated: "1983, December, 2",
      area: 116642,
      imageUrl: "https://content.churchofjesuschrist.org/templesldsorg/bc/Temples/photo-galleries/mexico-city-mexico/400x250/mexico-city-temple-exterior-1518361-wallpaper.jpg"
    },
    {
      templeName: "Campinas Brazil",
      location: "Campinas, Brazil",
      dedicated: "2002, May, 17",
      area: 48800,
      imageUrl: "https://www.churchofjesuschrist.org/imgs/c9a81a6f86750d7d9ade3499d3df52e2f7f726a7/full/500%2C/0/default"
    },
    {
      templeName: "São Paulo Brazil",
      location: "São Paulo, Brazil",
      dedicated: "1978, October, 30",
      area: 59864,
      imageUrl: "https://www.churchofjesuschrist.org/imgs/940f3e201364433a3d5d3dc14b0cacee38d41d1d/full/500%2C/0/default"
    },
    {
      templeName: "Rome Italy",
      location: "Rome, Italy",
      dedicated: "2019, March, 10",
      area: 40000,
      imageUrl: "https://www.churchofjesuschrist.org/imgs/17e2c70d687fffedfe115197e57fa8f5d1d369bb/full/500%2C/0/default"
    }
  ];
  
  const gallery = document.querySelector(".gallery");
  
  function displayTemples(templesArray) {
    gallery.innerHTML = "";
    templesArray.forEach(temple => {
      const card = document.createElement("figure");
  
      const img = document.createElement("img");
      img.src = temple.imageUrl;
      img.alt = temple.templeName;
      img.loading = "lazy";
  
      const caption = document.createElement("figcaption");
      caption.innerHTML = `
        <h3>${temple.templeName}</h3>
        <p>${temple.location}</p>
        <p>Dedicated: ${temple.dedicated}</p>
        <p>Area: ${temple.area.toLocaleString()} sq ft</p>
      `;
  
      card.appendChild(img);
      card.appendChild(caption);
      gallery.appendChild(card);
    });
  }
  
  function filterTemples(criteria) {
    let filtered = [];
    switch (criteria) {
      case "old":
        filtered = temples.filter(t => new Date(t.dedicated) < new Date("1900-01-01"));
        break;
      case "new":
        filtered = temples.filter(t => new Date(t.dedicated) > new Date("2000-01-01"));
        break;
      case "large":
        filtered = temples.filter(t => t.area > 90000);
        break;
      case "small":
        filtered = temples.filter(t => t.area < 10000);
        break;
      default:
        filtered = temples;
    }
    displayTemples(filtered);
  }
  
  document.querySelectorAll("nav a").forEach(link => {
    link.addEventListener("click", event => {
      event.preventDefault();
      const text = event.target.textContent.toLowerCase();
      filterTemples(text);
      document.querySelector("main h2").textContent = event.target.textContent;
    });
  });
  
  document.getElementById('year').textContent = new Date().getFullYear();
  document.getElementById('last-modified').textContent = document.lastModified;
  
  document.getElementById('menu-toggle').addEventListener('click', function () {
    const navMenu = document.getElementById('nav-menu');
    navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
  });
  
  displayTemples(temples);
  