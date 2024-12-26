import matplotlib.pyplot as plt
import os
import uuid

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../uploads/images")

def generate_graph(graph_data):
    """
    Generates a graph based on the provided data and saves it as an image.

    Args:
        graph_data (dict): Dictionary containing data for the graph.
                           Example format:
                           {
                               "type": "line",  # or "bar"
                               "x": [1, 2, 3, 4],
                               "y": [10, 20, 25, 30],
                               "title": "Sample Graph",
                               "xlabel": "X-Axis",
                               "ylabel": "Y-Axis"
                           }

    Returns:
        str: Path to the saved graph image.
    """
    # Create the uploads directory if it doesn't exist
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    try:
        # Extract data from the input
        graph_type = graph_data.get("type", "line")
        x = graph_data.get("x", [])
        y = graph_data.get("y", [])
        title = graph_data.get("title", "Graph")
        xlabel = graph_data.get("xlabel", "X-Axis")
        ylabel = graph_data.get("ylabel", "Y-Axis")

        # Create the graph
        plt.figure()
        if graph_type == "line":
            plt.plot(x, y)
        elif graph_type == "bar":
            plt.bar(x, y)
        else:
            raise ValueError(f"Unsupported graph type: {graph_type}")

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Generate a unique filename for the graph
        file_name = f"{uuid.uuid4()}.png"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        # Save the graph
        plt.savefig(file_path)
        plt.close()

        return file_path

    except Exception as e:
        raise RuntimeError(f"Error generating graph: {str(e)}")
