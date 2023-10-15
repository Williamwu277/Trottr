import type Poi from "./models/poi.model";

const db = sessionStorage;

function addLocation(poi: Poi) {
    let pois = getLocations();
    pois = [...pois, poi];
    setLocations(pois);
}

function setLocations(pois: Poi[]) {
    db.setItem("pois", JSON.stringify(pois));
}

function getLocations() {
    const points: string|null = db.getItem("pois");
    if (points == null) return [];

    const pois: Poi[] = JSON.parse(points);

    return pois;

}

function clear() {
    setLocations([]);
}

function setItem(key: string, value: string) {
    db.setItem(key, value);
}

export {addLocation, setLocations, getLocations, clear, setItem };