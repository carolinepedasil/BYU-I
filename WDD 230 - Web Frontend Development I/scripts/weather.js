const weatherURL = "https://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid=543d3f62405fa2cb4984446af0d28a4c&units=metric";

async function fetchWeather() {
    try {
        const response = await fetch(weatherURL);
        const data = await response.json();

        const weatherCard = document.querySelector(".card:nth-of-type(2)");
        const icon = `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
        const description = data.weather[0].description;
        const temp = Math.round(data.main.temp);

        weatherCard.innerHTML = `
            <h2>Information</h2>
            <p id="weather">
                Weather:<br>
                ${temp}&deg;C<br>
                ${description}<br>
                <img src="${icon}" width="30">
            </p>
            <p>Page Visits: <span id="visit-counter">0</span></p>
        `;
    } catch (error) {
        console.error("Weather fetch error:", error);
    }
}

fetchWeather();
