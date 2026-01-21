const { ColumnLayer, DeckGL, MapView, Deck } = deck;

async function loadData() {
    const response = await fetch("resources/pedestrian_data.json");
    return response.json();
}

loadData().then(data => {

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
                console.log("clicked column:", info.object);
            }
        },
        mapStyle: 'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
        layers: [
            columns
        ],
        getTooltip: ({ object }) =>
            object && `${object.sensor_description}\nChange: ${object.percentage_change}%`
    });
});
