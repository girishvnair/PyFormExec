import React, { useState } from "react";
import "../App.css"; // Add custom styles if needed
import { renderMarkdown } from "../services/api";

const MarkdownViewer = () => {
  const [markdownText, setMarkdownText] = useState("");
  const [renderedHtml, setRenderedHtml] = useState("");

  // Handle input change
  const handleInputChange = (e) => {
    setMarkdownText(e.target.value);
  };

  // Render Markdown
  const handleRenderMarkdown = async () => {
    const html = await renderMarkdown(markdownText);
    setRenderedHtml(html);
  };

  return (
    <div className="markdown-viewer">
      <h2>Markdown Viewer</h2>
      <textarea
        value={markdownText}
        onChange={handleInputChange}
        placeholder="Enter Markdown here..."
        rows="10"
        cols="50"
      ></textarea>
      <div>
        <button onClick={handleRenderMarkdown}>Render Markdown</button>
      </div>
      <h3>Rendered Output:</h3>
      <div
        className="rendered-markdown"
        dangerouslySetInnerHTML={{ __html: renderedHtml }}
      ></div>
    </div>
  );
};

export default MarkdownViewer;
