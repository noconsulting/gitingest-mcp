from src.server import mcp

@mcp.prompt()
async def repository_weather(repository_url: str):
    """
        If the user is asking about the weather for a repository, use this prompt.
    """
    return (
        f"Give only summary of {repository_url} repository and only if the token count is lower than 10000 ingest the "
        f"whole repository"
    )