// Canvas Sine Wave
const canvas = document.getElementById('graphCanvas'); //<canvas id="graphCanvas" width="600" height="200"></canvas>
const ctx = canvas.getContext('2d');
const axisColor = '#000';
const waveColor = 'blue';
// const waveAmplitude = 70;
let waveAmplitude = 70;

let waveFrequency = 0.02; // Initial frequency of the sine wave
let phase = 0; // Initial phase of the sine wave
let defaultPhase = 5;

// Get input value for Sine Wave
const waveFrequencyInput = document.getElementById('waveFrequencyInput');
const waveFrequencyValue = document.getElementById('waveFrequencyValue');

const waveAmplitudeInput = document.getElementById('waveAmplitudeInput');
const waveAmplitudeValue = document.getElementById('waveAmplitudeValue');


// Modify Amplitude
waveAmplitudeInput.addEventListener('input', function() {
    waveAmplitude = parseFloat(waveAmplitudeInput.value);
    // console.log(waveAmplitude)
    waveAmplitudeValue.textContent = waveAmplitude.toFixed();
    drawGraph();
});

// Modify Frequency
waveFrequencyInput.addEventListener('input', function() {
    waveFrequency = parseFloat(waveFrequencyInput.value);
    // console.log(waveFrequency)
    waveFrequencyValue.textContent = waveFrequency.toFixed(2);
    drawGraph();
});

function drawAxes() {
    // ... (same as before) ...
    // Draw X axis
    ctx.beginPath();
    ctx.strokeStyle = axisColor;
    ctx.moveTo(0, canvas.height / 2);
    ctx.lineTo(canvas.width, canvas.height / 2);
    ctx.stroke();

    // Draw Y axis
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.stroke();
}

function plotSineWave() {
    ctx.beginPath();
    ctx.strokeStyle = waveColor;
    ctx.fillStyle = 'lightblue'; // Set the fill color

    // Set the dashed line pattern (5 pixels on, 5 pixels off)
    // ctx.setLineDash([5, 5]);

    // Set the line width to make the sine wave thicker
    ctx.lineWidth = 3; // Adjust the thickness as needed


    // Start from the left bottom corner
    ctx.moveTo(0, canvas.height);

    for (let x = 0; x < canvas.width; x++) {
        const y = canvas.height / 2 + waveAmplitude * Math.sin((x + phase) * waveFrequency);
        ctx.lineTo(x, y);
    }

    // Draw a straight line to the right bottom corner
    ctx.lineTo(canvas.width, canvas.height);

    // Close the path
    ctx.closePath();

    // Fill the area below the sine wave with the fill color
    ctx.fill();

    // Stroke the sine wave path
    ctx.stroke();
}


function drawGraph() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // drawAxes();
    plotSineWave();
}

// Function to generate a random phase between 0 and 2π
// function getRandomPhase() {
//     return Math.random() * 2 * Math.PI;
// }


function animate() {
    
    
    
    // Update the phase to create movement

    phase += defaultPhase; // Adjust the speed of movement as needed

    // Draw the graph
    drawGraph();

    // Call the animation loop recursively
    requestAnimationFrame(animate);
}


animate();