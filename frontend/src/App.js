import React, { useEffect, useState } from "react";

function App() {
  const [appliances, setAppliances] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/get_appliances")
      .then((response) => response.json())
      .then((data) => setAppliances(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Smart Home Assistant</h1>
      <table border="1">
        <thead>
          <tr>
            <th>Appliance</th>
            <th>Power Usage (W)</th>
            <th>Temperature (°C)</th>
            <th>AI Predicted Maintenance</th>
          </tr>
        </thead>
        <tbody>
          {appliances.map((appliance) => (
            <tr key={appliance.id}>
              <td>{appliance.appliance}</td>
              <td>{appliance.power} W</td>
              <td>{appliance.temperature}°C</td>
              <td>{appliance.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
