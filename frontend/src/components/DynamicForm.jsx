import React, { useState } from "react";
import "../App.css"; // Add custom styles if needed
import { saveForm } from "../services/api";

const DynamicForm = () => {
  const [fields, setFields] = useState([]);
  const [formData, setFormData] = useState({});

  // Add a new field
  const addField = () => {
    setFields([
      ...fields,
      { type: "text", label: `Field ${fields.length + 1}`, placeholder: "" },
    ]);
  };

  // Remove a field
  const removeField = (index) => {
    const newFields = fields.filter((_, i) => i !== index);
    setFields(newFields);

    // Remove corresponding data
    const newData = { ...formData };
    delete newData[`Field ${index + 1}`];
    setFormData(newData);
  };

  // Handle input change
  const handleInputChange = (index, value) => {
    const fieldName = fields[index].label;
    setFormData({ ...formData, [fieldName]: value });
  };

  // Save the form as HTML
  const saveFormAsHtml = async () => {
    const formConfig = { fields };
    const file = await saveForm(formConfig);

    if (file) {
      const url = window.URL.createObjectURL(new Blob([file]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "dynamic_form.html");
      document.body.appendChild(link);
      link.click();
      link.remove();
    } else {
      alert("Failed to save the form.");
    }
  };

  return (
    <div className="dynamic-form">
      <h2>Dynamic Form</h2>

      {/* Render dynamic fields */}
      {fields.map((field, index) => (
        <div key={index} className="form-field">
          <label>{field.label}</label>
          <input
            type={field.type}
            placeholder={field.placeholder}
            onChange={(e) => handleInputChange(index, e.target.value)}
          />
          <button onClick={() => removeField(index)}>Remove</button>
        </div>
      ))}

      <div className="form-actions">
        <button onClick={addField}>Add Field</button>
        <button onClick={saveFormAsHtml}>Save Form</button>
      </div>

      <h3>Form Data:</h3>
      <pre>{JSON.stringify(formData, null, 2)}</pre>
    </div>
  );
};

export default DynamicForm;
