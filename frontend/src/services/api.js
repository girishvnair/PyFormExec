import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000";

export const executeCode = async (code) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/execute`, { code });
    return response.data;
  } catch (error) {
    console.error("Error executing code:", error);
    return { error: "Error executing code." };
  }
};

export const installLibraries = async (libraries) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/install`, { libraries });
    return response.data;
  } catch (error) {
    console.error("Error installing libraries:", error);
    return { success: [], errors: ["Error installing libraries."] };
  }
};

export const generateGraph = async (graphData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/generate-graph`, graphData, {
      responseType: "blob",
    });
    return response.data;
  } catch (error) {
    console.error("Error generating graph:", error);
    return null;
  }
};

export const renderMarkdown = async (text) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/render-markdown`, { text });
    return response.data.html;
  } catch (error) {
    console.error("Error rendering markdown:", error);
    return "<p>Error rendering markdown.</p>";
  }
};

export const saveForm = async (formData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/save-form`, formData, {
      responseType: "blob",
    });
    return response.data;
  } catch (error) {
    console.error("Error saving form:", error);
    return null;
  }
};
