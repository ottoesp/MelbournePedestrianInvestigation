export async function loadSensorPlot(sensor) {
    const container = document.getElementById('sensor_plot_container');
    
    // Add spinners to existing children
    for (const child of container.children) {
        const spinnerWrapper = document.createElement('div');
        spinnerWrapper.className = 'position-absolute top-50 start-50 translate-middle z-2';
        
        const spinner = document.createElement('div');
        spinner.className = 'spinner-border';
        spinner.setAttribute('role', 'status');
        spinner.innerHTML = '<span class="visually-hidden">Loading...</span>';
        
        spinnerWrapper.appendChild(spinner);
        child.classList.add('position-relative');
        child.prepend(spinnerWrapper);

        const card = child.querySelector('.card');
        card.classList.add('loading')
    }
    
    // Source new content
    const sensor_plot = await createCountsPlot(sensor);
    const days_plot = await createDaysPlot(sensor)
    const fit_plot = await createFitPlot(sensor)
    // Replace old content
    container.replaceChildren(sensor_plot, days_plot, fit_plot);

    // Add indicator that new stuff has happened
    for (const child of container.children) {
        const card = child.querySelector('.card');
        card.classList.add('highlight-ring');
        setTimeout(() => card.classList.remove('highlight-ring'), 1000);
    }

    sensor_plot.scrollIntoView({block: 'center', behavior: "smooth" })
}

function createCountsPlot(sensor) {
    return new Promise((resolve) => {
        const col = document.createElement('div')
        col.className = 'col-12 col-lg-8';

        const card = document.createElement('div');
        card.className = 'card h-100 pt-3 loading';
        
        const img = document.createElement('img');
        img.src = `${import.meta.env.BASE_URL}sensorplots/${sensor.sensor_id}_sensor_plot.svg`;
        img.className = 'card-img-bottom img-fluid';
        img.alt = `Sensor plot for ${sensor.sensor_description}`;
        img.decoding = 'async';
        
        const body = document.createElement('div');
        body.className = 'card-body'

        const footer = document.createElement('div');
        footer.className = 'card-footer text-center';
        footer.innerHTML = '<p class="card-text text-secondary">Figure X</p>';
        
        card.appendChild(img);
        card.appendChild(body);
        card.appendChild(footer);
        col.appendChild(card);
        
        // Resolve when image loads
        img.onload = () => {
            card.classList.remove('loading');
            resolve(col);
        };
        img.onerror = () => {
            card.classList.remove('loading');
            resolve(col);
        };
    });
}

function createDaysPlot(sensor) {
    return new Promise((resolve) => {
        const col = document.createElement('div')
        col.className = 'col-12 col-md-6 col-lg-4';

        const card = document.createElement('div');
        card.className = 'card h-100 pt-3 loading';
        
        const img = document.createElement('img');
        img.src = `${import.meta.env.BASE_URL}sensordays/${sensor.sensor_id}_sensordays.svg`;
        img.className = 'card-img-bottom img-fluid';
        img.alt = `Days plot for ${sensor.sensor_description}`;
        img.decoding = 'async';
        
        const body = document.createElement('div');
        body.className = 'card-body'

        const footer = document.createElement('div');
        footer.className = 'card-footer text-center';
        footer.innerHTML = '<p class="card-text text-secondary">Figure X</p>';
        
        card.appendChild(img);
        card.appendChild(body);
        card.appendChild(footer);
        col.appendChild(card);
        
        // Resolve when image loads
        img.onload = () => {
            card.classList.remove('loading');
            resolve(col);
        };
        img.onerror = () => {
            card.classList.remove('loading');
            resolve(col);
        };
    });
}

function createFitPlot(sensor) {
    return new Promise((resolve) => {
        const col = document.createElement('div')
        col.className = 'col-12 col-md-12';

        const card = document.createElement('div');
        card.className = 'card h-100 pt-3 loading';
        
        const img = document.createElement('img');
        img.src = `${import.meta.env.BASE_URL}sensorfits/${sensor.sensor_id}_sensor_fit.svg`;
        img.className = 'card-img-bottom img-fluid';
        img.alt = `Comparison of model fit vs counts for ${sensor.sensor_description}`;
        img.decoding = 'async';
        
        const body = document.createElement('div');
        body.className = 'card-body'

        const footer = document.createElement('div');
        footer.className = 'card-footer text-center';
        footer.innerHTML = '<p class="card-text text-secondary">Figure X<br>Note that pedestrian counts shown are a 2-week rolling average</p>';
        
        card.appendChild(img);
        card.appendChild(body);
        card.appendChild(footer);
        col.appendChild(card);
        
        // Resolve when image loads
        img.onload = () => {
            card.classList.remove('loading');
            resolve(col);
        };
        img.onerror = () => {
            card.classList.remove('loading');
            resolve(col);
        };
    });
}
