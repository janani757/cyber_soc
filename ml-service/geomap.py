import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

export default function GeoMap({ alerts }) {
  return (
    <MapContainer center={[20, 78]} zoom={2} style={{ height: "100%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      {alerts.map((a, i) => (
        <Marker key={i} position={[20 + i, 78 + i]}>
          <Popup>
            IP: {a.ip} <br />
            Severity: {a.severity}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}