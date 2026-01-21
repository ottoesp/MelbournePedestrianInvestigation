const { ColumnLayer, DeckGL, MapView, Deck } = deck;

async function loadData() {
    const response = await fetch("/pedestrian_data.json");
    return response.json();
}

async function loadSensorPlot(sensorId, description) {
    const svgPath = `/sensorplots/${sensorId}_sensor_plot.svg`;
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
            touchRotate: true
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
                html: `<p>${object.sensor_description}</p><p>Change: ${object.percentage_change}%</p>`,
                style: {
                    'background-color': '#f8f9fa',
                    'border' : '1px solid #868E96',
                    'border-radius': '.25rem',
                    'opacity' : '0.95',
                    'color' : '#000'
                }

            }
            
        }
    });

}

