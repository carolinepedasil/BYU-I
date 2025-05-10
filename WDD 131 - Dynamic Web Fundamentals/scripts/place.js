const currentYear = new Date().getFullYear();
document.getElementById("year").textContent = currentYear;
document.getElementById("lastModified").textContent = document.lastModified;

function calculateWindChillCelsius(tempC, windSpeedKmh) {
  return (
    13.12 +
    0.6215 * tempC -
    11.37 * Math.pow(windSpeedKmh, 0.16) +
    0.3965 * tempC * Math.pow(windSpeedKmh, 0.16)
  ).toFixed(1);
}

const temperature = parseFloat(document.getElementById("temperature").textContent);
const windSpeed = parseFloat(document.getElementById("windspeed").textContent);

let windChill = "N/A";

if (temperature <= 10 && windSpeed > 4.8) {
  windChill = `${calculateWindChillCelsius(temperature, windSpeed)} °C`;
}

document.getElementById("windchill").textContent = windChill;
