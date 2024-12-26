import React from "react";
import DynamicForm from "./components/DynamicForm";
import MarkdownViewer from "./components/MarkdownViewer";
import GraphViewer from "./components/GraphViewer";

function App() {
  return (
    <div className="App">
      <header>
        <h1>Welcome to PyFormExec</h1>
      </header>
      <main>
        <DynamicForm />
        <MarkdownViewer />
        <GraphViewer />
      </main>
    </div>
  );
}

export default App;
