import React, { useState } from "react";
import { generateGraph } from "../services/api";

const GraphViewer = () => {
  const [graphData, setGraphData] = useState({
    type: "line", // Default graph type
    x: "",
    y: "",
    title: "Sample Graph",
    xlabel: "X-Axis",
    ylabel: "Y-Axis",
  });
  const [graphImage, setGraphImage] = useState(null);

  // Handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setGraphData({ ...graphData, [name]: value });
  };

  // Generate graph
  const handleGenerateGraph = async () => {
    try {
      // Convert X and Y values to arrays
      const xValues = graphData.x.split(",").map(Number);
      const yValues = graphData.y.split(",").map(Number);

      const payload = {
        ...graphData,
        x: xValues,
        y: yValues,
      };

      const graphBlob = await generateGraph(payload);
      if (graphBlob) {
        const url = URL.createObjectURL(new Blob([graphBlob]));
        setGraphImage(url);
      } else {
        alert("Failed to generate graph.");
      }
    } catch (error) {
      console.error("Error generating graph:", error);
      alert("Invalid input data. Ensure X and Y values are comma-separated numbers.");
    }
  };

  return (
    <div className="graph-viewer">
      <h2>Graph Viewer</h2>
      <div className="form-field">
        <label>Graph Type:</label>
        <select name="type" value={graphData.type} onChange={handleInputChange}>
          <option value="line">Line</option>
          <option value="bar">Bar</option>
        </select>
      </div>
      <div className="form-field">
        <label>X Values (comma-separated):</label>
        <input
          type="text"
          name="x"
          value={graphData.x}
          onChange={handleInputChange}
        />
      </div>
      <div className="form-field">
        <label>Y Values (comma-separated):</label>
        <input
          type="text"
          name="y"
          value={graphData.y}
          onChange={handleInputChange}
        />
      </div>
      <div className="form-field">
        <label>Title:</label>
        <input
          type="text"
          name="title"
          value={graphData.title}
          onChange={handleInputChange}
        />
      </div>
      <div className="form-field">
        <label>X-Axis Label:</label>
        <input
          type="text"
          name="xlabel"
          value={graphData.xlabel}
          onChange={handleInputChange}
        />
      </div>

