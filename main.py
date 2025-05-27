from mcp.server.fastmcp import FastMCP
from gitingest import ingest_async
from gitingest import Tokenizer

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
        include_patterns: Optional patterns to include (comma separated) e.g.: ".java,.ts,.js,.xml"
        exclude_patterns: Optional patterns to exclude (comma separated) e.g.: ".jpeg,.gif,.jpg,.png,.svg,.mp4,.bin"

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
        source: str = "http://github.com/cyclotruc/gitingest",
        include_patterns: str | None = None,
        exclude_patterns: str | None = None
) -> str:
    """
    Show only the tree structure of a git repository.

    Args:
        repo_path_or_url: A GitHub URL or local path
        include_patterns: Optional patterns to include (comma separated) e.g.: ".java,.ts,.js,.xml"
        exclude_patterns: Optional patterns to exclude (comma separated) e.g.: ".jpeg,.gif,.jpg,.png,.svg,.mp4,.bin"

    Returns:
        str: Tree structure of the repository
    """
    assert source
    _, tree, _ = await ingest_async(source=source,
                                    include_patterns=include_patterns,
                                    exclude_patterns=exclude_patterns)
    return tree


@mcp.tool()
async def gitingest_summary(
        source: str = "http://github.com/cyclotruc/gitingest",
        include_patterns: str | None = None,
        exclude_patterns: str | None = None,
        model_tokenizer: str = "GEMINI_1_5_PRO"
) -> str:
    """
    Show a summary of the repository content (repository name, number of files analyzed and estimated token number)

    Args:
        repo_path_or_url: A GitHub URL or local path
        include_patterns: Optional patterns to include (comma separated) e.g.: ".java,.ts,.js,.xml"
        exclude_patterns: Optional patterns to exclude (comma separated) e.g.: ".jpeg,.gif,.jpg,.png,.svg,.mp4,.bin"
        model_tokenizer: Optional string representing the name of the used tokenizer to evaluate the context length. Possible Values: "GEMINI_1_5_PRO" OR "OPEN_AI"

    Returns:
        str: Summary and Tree structure of the repository
    """
    assert source

    summary, _, _ = await ingest_async(source=source,
                                       include_patterns=include_patterns,
                                       exclude_patterns=exclude_patterns,
                                       model_tokenizer=Tokenizer[model_tokenizer])
    return summary

if __name__ == "__main__":
    mcp.run(transport="streamable-http")