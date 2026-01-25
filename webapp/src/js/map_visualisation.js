const { ColumnLayer, DeckGL, MapView, Deck } = deck;

async function loadData() {
    const response = await fetch(`${import.meta.env.BASE_URL}pedestrian_data.json`);
    return response.json();
}

async function loadSensorPlot(sensorId, description) {
    const svgPath = `${import.meta.env.BASE_URL}sensorplots/${sensorId}_sensor_plot.svg`;
    const img = document.getElementById('sensor-plot-image');
    if (img) {
        img.src = svgPath;
        img.alt = `Sensor plot for ${description}`;
        img.style.display = 'block';
    }
}

export async function initMap() {
    const data = await loadData();

    const columns = new ColumnLayer({
        id: "columns",
        data,
        diskResolution: 12,
        radius: 20,
        extruded: true,
        elevationScale: 5,
        pickable: true,

        getPosition: d => [d.longitude, d.latitude],
        getElevation: d => d.absolute_change,
        getFillColor: d => d.colour
    });

    new DeckGL({
        // canvas: document.getElementById('deck-canvas'),
        container: document.getElementById('deck-container'),
        views: new MapView({
            repeat: true,
        }),
        initialViewState: {
            longitude: 144.96,
            latitude: -37.813,
            zoom: 14.2,
            pitch: 60,
            bearing: -60,
        },
        controller: {
            dragPan: false,
            scrollZoom: false,
            doubleClickZoom: false,
            touchZoom: false,
            keyboard: false,
            dragRotate: true,
            touchRotate: true,
            dragMode: "rotate",
            interia: true
        },
        onClick: (info) => {
            if (info.object) {
                const sensorId = info.object.sensor_id;
                const sensorDescripition = info.object.sensor_description;
                loadSensorPlot(sensorId, sensorDescripition).then(() => {
                    document.getElementById('sensor_plot_card')
                    ?.scrollIntoView({ behavior: "smooth" });
                })
            }
        },
        mapStyle: 'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
        layers: [
            columns
        ],
        getTooltip: ({ object }) => {
            return object && {
                html: `
                    <div style="padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5;">
                        <strong>${object.sensor_description}</strong><br>
                        Change: ${object.percentage_change > 0 ? '+' : ''}${object.percentage_change}%
                    </div>
                `,
                style: {
                    'background-color': 'var(--bs-tooltip-bg, rgba(255, 255, 255, 0.9))',
                    'color': '#000',
                    'border-radius': 'var(--bs-tooltip-border-radius, 0.375rem)',
                    'font-family': 'var(--bs-body-font-family, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif)',
                    'max-width': '200px',
                    'text-align': 'left',
                    'box-shadow': '0 0.5rem 1rem rgba(0, 0, 0, 0.15)',
                    'z-index': '1080'
                }
            }
            
        }
    });

}

