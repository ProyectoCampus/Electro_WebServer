function controlRelay(state) {
    fetch('/' + state)
    .then(response => response.json())
    .then(data => {
        updateStatus(data.status);
    })
    .catch(error => console.error('Error:', error));
}

function updateStatus(status) {
    document.getElementById("status").innerText = "Estado: " + (status === "on" ? "Encendido" : "Apagado");
}

function fetchStatus() {
    fetch('/status')
    .then(response => response.json())
    .then(data => {
        updateStatus(data.status);
    })
    .catch(error => console.error('Error al obtener estado:', error));
}

// Obtener estado inicial al cargar la página
window.onload = fetchStatus;

// Actualizar estado cada 3 segundos
setInterval(fetchStatus, 3000);
