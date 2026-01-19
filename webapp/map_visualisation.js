const { Deck } = deck;
const { ColumnLayer } = deck;
const { TileLayer } = deck;

async function loadData() {
    const response = await fetch("resources/pedestrian_data.json");
    return response.json();
}

loadData().then(data => {

    const tiles = new TileLayer({
        id: "osm-tiles",
        data: "https://basemaps.cartocdn.com/dark_all/{z}/{x}/{y}@2x.png",
        minZoom: 0,
        maxZoom: 19,
        tileSize: 256,
        renderSubLayers: props => {
            const {
                bbox: { west, south, east, north }
            } = props.tile;

            return new deck.BitmapLayer(props, {
                data: null,
                image: props.data,
                bounds: [
                    west,
                    south,
                    east,
                    north
                ]
            });
        }
    });

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
        getFillColor: d => d.colour,
    });

    new Deck({
        parent: document.getElementById("deck-container"),
        useDevicePixels: true,
        
        initialViewState: {
            longitude: 144.96,
            latitude: -37.813,
            zoom: 14.3,
            pitch: 55,
            bearing: -60
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

        layers: [tiles, columns],

        getTooltip: ({ object }) =>
            object && `${object.sensor_description}\nChange: ${object.percentage_change}%`
    });
});
