import markdown2

def render_markdown(markdown_text):
    """
    Converts Markdown text into HTML.

    Args:
        markdown_text (str): The Markdown text to convert.

    Returns:
        str: The rendered HTML.
    """
    try:
        # Convert Markdown to HTML
        html = markdown2.markdown(markdown_text)
        return html
    except Exception as e:
        raise RuntimeError(f"Error rendering Markdown: {str(e)}")
