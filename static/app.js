// -------------------- Funciones para controlar el relé ----------------------------

function controlRelay(state) {
    fetch('/' + state)
        .then(response => response.json())
        .then(data => updateStatus(data.status))
        .catch(error => console.error('Error:', error));
}

function updateStatus(status) {
    document.getElementById("status").innerText = `Estado: ${status === "on" ? "Encendido" : "Apagado"}`;
}

function fetchStatus() {
    fetch('/status')
        .then(response => response.json())
        .then(data => updateStatus(data.status))
        .catch(error => console.error('Error al obtener estado:', error));
}

// Obtener estado inicial al cargar la página y actualizar cada 3s
window.onload = () => {
    fetchStatus();
    fetchButtonsStatus();
    setInterval(fetchStatus, 3000); // Actualiza cada 3 segundos
    setInterval(fetchButtonsStatus, 1000); // Actualiza cada 1 segundo
};

// -------------------- LDR Sensor --------------------
// -------------------- WebSocket LDR --------------------

// Configuración del WebSocket para escuchar datos de los sensores
window.addEventListener("load", initializeSocket);

function initializeSocket() {
    // WebSocket para el LDR
    const ldrSocket = new WebSocket(`ws://${location.host}/ws/ldr`);
    ldrSocket.onmessage = function(event) {
        const lightPercentage = parseFloat(event.data);
        updateChart(lightPercentage);
        updateValues(lightPercentage);
    };
}

// Actualiza los valores mostrando solo los últimos 20
function updateValues(data) {
    sensorValues.value = `${data}\n${sensorValues.value}`.split("\n").slice(0, 20).join("\n");
}

// Referencias en el DOM
const sensorValues = document.querySelector("#sensor-values");
const sensorChartDiv = document.getElementById("sensor-chart");

// Configuración del gráfico con Plotly.js
const sensorTrace = {
    x: [],
    y: [],
    name: "LDR/Photoresistor",
    mode: "lines+markers",
    type: "scatter"
};

const sensorLayout = {
    autosize: false,
    width: 800,
    height: 500,
    colorway: ["#05AD86"],
    margin: { t: 40, b: 40, l: 80, r: 80, pad: 0 },
    xaxis: { gridwidth: "2", autorange: true },
    yaxis: { gridwidth: "2", autorange: true }
};

const config = { responsive: true };

Plotly.newPlot(sensorChartDiv, [sensorTrace], sensorLayout, config);

// Variables para graficar los datos en tiempo real
let newSensorXArray = [];
let newSensorYArray = [];
const MAX_GRAPH_POINTS = 50;
let ctr = 0;

function updateChart(sensorRead) {
    if (newSensorXArray.length >= MAX_GRAPH_POINTS) newSensorXArray.shift();
    if (newSensorYArray.length >= MAX_GRAPH_POINTS) newSensorYArray.shift();

    newSensorXArray.push(ctr++);
    newSensorYArray.push(sensorRead);

    Plotly.update(sensorChartDiv, { x: [newSensorXArray], y: [newSensorYArray] });
}


//------------------------- Button -------------------------------
//--------------- WebSocket para los botones ---------------------

const buttonsSocket = new WebSocket(`ws://${location.host}/ws/buttons`);

buttonsSocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateButtonsDisplay(data.button_pull_up, data.button_pull_down);
};

function fetchButtonsStatus() {
    fetch('/buttons_status')
    .then(response => response.json())
    .then(data => updateButtonsDisplay(data.button_pull_up, data.button_pull_down))
    .catch(error => console.error('Error al obtener estado de los botones:', error));
}

function updateButtonsDisplay(pullUp, pullDown) {
    // Solo actualiza el texto dentro del <span>
    document.querySelector("#button-pull-up span").textContent = pullUp ? "Presionado" : "No presionado";
    document.querySelector("#button-pull-down span").textContent = pullDown ? "Presionado" : "No presionado";
}


//--------------------- Control de los botones Pull-Up y Pull-Down ---------------------------------

function toggleButton(buttonType) {
    const button = document.querySelector(`button.${buttonType}`);
    const span = button.querySelector("span");
    button.classList.toggle('active'); // Alternar el estado "activo"
    
    const statusText = button.classList.contains('active') ? 'Presionado' : 'No presionado';
    span.textContent = statusText;
}

// Uso de funciones para cambiar el estado
function controlPullUp() {
    toggleButton('pullup');
}

function controlPullDown() {
    toggleButton('pulldown');
}