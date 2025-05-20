from mcp.server.fastmcp import FastMCP
from gitingest import ingest_async

mcp: FastMCP = FastMCP("GitIngest")

@mcp.tool()
async def gitingest_repo(
        source: str = "http://github.com/cyclotruc/gitingest",
        include_patterns: str | None = None,
        exclude_patterns: str | None = None
) -> str:
    """
    Get a digest of a git repository or local path.

    Args:
        repo_path_or_url: A GitHub URL or local path
        include_patterns: Optional patterns to include (comma separated)
        exclude_patterns: Optional patterns to exclude (comma separated)

    Returns:
        str: Content digest of the repository
    """
    assert source
    _, _, content = await ingest_async(
        source=source,
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns
    )
    return content


@mcp.tool()
async def gitingest_tree(
        source: str = "http://github.com/cyclotruc/gitingest"
) -> str:
    """
    Show only the tree structure of a git repository.

    Args:
        repo_path_or_url: A GitHub URL or local path

    Returns:
        str: Summary and tree structure of the repository
    """
    assert source
    _, tree, _ = await ingest_async(source=source)
    return f"{tree}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")