export async function loadSensorPlot(sensor) {
    const container = document.getElementById('sensor_plot_container');
    
    const col = await createCountsPlot(sensor);
    container.replaceChildren(col); // Single atomic operation, no flash
}

function createCountsPlot(sensor) {
    return new Promise((resolve) => {
        const col = document.createElement('div')
        col.className = 'col-12'

        const card = document.createElement('div');
        card.className = 'card h-100';
        card.style.minHeight = '400px';
        
        const img = document.createElement('img');
        img.src = `${import.meta.env.BASE_URL}sensorplots/${sensor.sensor_id}_sensor_plot.svg`;
        img.className = 'card-img-bottom img-fluid';
        img.alt = `Sensor plot for ${sensor.sensor_description}`;
        img.decoding = 'async';
        
        const footer = document.createElement('div');
        footer.className = 'card-footer text-center';
        footer.innerHTML = '<p class="card-text text-secondary">Figure X</p>';
        
        card.appendChild(img);
        card.appendChild(footer);
        col.appendChild(card);
        
        // Resolve when image loads
        img.onload = () => resolve(col);
        img.onerror = () => resolve(col);
    });
}