import { loadSensorPlot } from "./load_sensor_plots";

const { ColumnLayer, DeckGL, MapView, Deck } = deck;

async function loadData() {
    const response = await fetch(`${import.meta.env.BASE_URL}pedestrian_data.json`);
    return response.json();
}

const active_controller = {
    dragPan: false,
    scrollZoom: false,
    doubleClickZoom: false,
    touchZoom: false,
    keyboard: false,
    dragRotate: true,
    touchRotate: false,
    dragMode: "rotate",
    interia: true
}

const inactive_controller = {
    dragPan: false,
    scrollZoom: false,
    doubleClickZoom: false,
    touchZoom: false,
    keyboard: false,
    dragRotate: false,
    touchRotate: false,
    dragMode: "rotate",
    interia: true
}

function enableMapInteraction(deckgl) {
    mapInteractionEnabled = true;
    deckgl.setProps({
        controller: active_controller
    });

    const hint = document.getElementById('map-interaction-hint');
    if (hint) hint.classList.add('d-none');
}

function disableMapInteraction(deckgl) {
    mapInteractionEnabled = false;
    deckgl.setProps({
        controller: inactive_controller
    });
    
    const hint = document.getElementById('map-interaction-hint');
    if (hint) hint.classList.remove('d-none');
}

const viewportWidth = window.innerWidth;
const isMobile = viewportWidth < 768;
const zoom = viewportWidth < 768 ? 13.5 : 14.2;

let mapInteractionEnabled = false;

export async function initMap() {
    const data = await loadData();
    const container = document.getElementById('deck-container');

    const columns = new ColumnLayer({
        id: "columns",
        data,
        diskResolution: 12,
        radius: 20,
        extruded: true,
        elevationScale: 0.03,
        pickable: true,

        getPosition: d => [d.longitude, d.latitude],
        getElevation: d => d.absolute_change,
        getFillColor: d => d.colour
    });

    const deckgl = new DeckGL({
        container: container,
        views: new MapView({
            repeat: true,
        }),
        initialViewState: {
            longitude: 144.96,
            latitude: -37.813,
            zoom: zoom,
            pitch: 60,
            bearing: -60,
        },
        controller: isMobile ? inactive_controller : active_controller,
        onClick: (info) => {
            if (info.object) {
                loadSensorPlot(info.object);
                document.getElementById('sensor_plot_container')
                    ?.scrollIntoView({ behavior: "smooth" });
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
                        Change: ${object.count_difference_2025_2019 > 0 ? '+' : ''}${Math.round(object.count_difference_2025_2019).toLocaleString()} pedestrians per day
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

    // Initialize mobile interaction state and set up double-click listener
    if (isMobile) {
        // Show hint initially
        disableMapInteraction(deckgl);
        
        let lastClickTime = 0;
        container.addEventListener('click', () => {
            const now = Date.now();
            if (now - lastClickTime < 300) {
                // Double-click detected
                if (mapInteractionEnabled) {
                    disableMapInteraction(deckgl);
                } else {
                    enableMapInteraction(deckgl);
                }
            }
            lastClickTime = now;
        });
    }
}

