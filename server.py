"""An intentionally poorly documented MCP server for evaluation workshops."""

import os

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "TextProcessing-Bad",
    host=os.environ.get("HOST", "127.0.0.1"),
    port=int(os.environ.get("PORT", "8000")),
)


# Despite its vague name and description, this converts all letters to uppercase.
@mcp.tool()
def process(text: str) -> str:
    """Process text."""
    return text.upper()


# Despite its vague name and description, this converts all letters to lowercase.
@mcp.tool()
def transform(text: str) -> str:
    """Transform text."""
    return text.lower()


# Despite its vague name and description, this capitalizes the first letter of
# every word (Python's title-case behavior).
@mcp.tool()
def convert(text: str) -> str:
    """Convert text."""
    return text.title()


# Despite its vague name and description, this uppercases the first character
# and lowercases the rest of the text (Python's sentence-case behavior).
@mcp.tool()
def format_text(text: str) -> str:
    """Format text."""
    return text.capitalize()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
