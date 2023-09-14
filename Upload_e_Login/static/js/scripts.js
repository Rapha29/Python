function toggleFullScreen(videoId) {
    const video = document.getElementById(videoId);

    if (!document.fullscreenElement) {
        video.requestFullscreen().catch(err => {
            alert(`Erro ao entrar em tela cheia: ${err.message}`);
        });
    } else {
        document.exitFullscreen();
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const fileCategories = document.querySelectorAll(".file-category");

    categoryFilter.addEventListener("change", function () {
        const selectedCategory = categoryFilter.value;

        fileCategories.forEach(function (category) {
            if (selectedCategory === "all" || category.classList.contains(selectedCategory)) {
                category.style.display = "block";
            } else {
                category.style.display = "none";
            }
        });
    });
});

function getWeatherInfo(location) {
    fetch(`https://wttr.in/${location}?format=%C+%t`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Não foi possível obter informações de clima.');
            }
            return response.text();
        })
        .then(data => {
            const weatherInfo = `Clima: ${data}`;
            document.getElementById('weather-info').textContent = weatherInfo;
        })
        .catch(error => {
            console.error('Erro ao obter informações de clima:', error);
            document.getElementById('weather-info').textContent = 'Não foi possível obter informações de clima.';
        });
}

// Função para obter informações de localidade com base no IP do usuário
function getLocationInfo(ip) {
    fetch(`https://ip-api.com/json/${ip}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Não foi possível obter informações de localidade.');
            }
            return response.json();
        })
        .then(data => {
            const locationInfo = `Localidade: ${data.city}, ${data.regionName}, ${data.country}, Bairro: ${data.org}`;
            document.getElementById('location-info').textContent = locationInfo;
            getWeatherInfo(data.city); // Chama a função para obter informações de clima com base na cidade
        })
        .catch(error => {
            console.error('Erro ao obter informações de localidade:', error);
            document.getElementById('location-info').textContent = 'Não foi possível obter informações de localidade.';
        });
}

// Obtém o IP do usuário usando a API ipify.org
fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => {
        const userIP = data.ip;
        document.getElementById('ip-info').textContent = `Seu IP: ${userIP}`;
        getLocationInfo(userIP);
    })
    .catch(error => {
        console.error('Erro ao obter o IP do usuário:', error);
        document.getElementById('ip-info').textContent = 'Não foi possível obter o IP do usuário.';
    });