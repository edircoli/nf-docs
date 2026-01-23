"""
Git utilities for extracting repository information.

Used to build source code links to remote repositories like GitHub, GitLab, etc.
"""

import logging
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class GitInfo:
    """Git repository information."""

    remote_url: str | None = None
    commit: str | None = None
    branch: str | None = None
    is_pushed: bool = False
    base_url: str | None = None  # Base URL for source links (e.g., https://github.com/org/repo)
    ref: str | None = None  # The ref to use in URLs (commit if pushed, branch otherwise)


def get_git_info(workspace_path: str | Path) -> GitInfo | None:
    """
    Extract git repository information from a workspace.

    Args:
        workspace_path: Path to the git repository

    Returns:
        GitInfo object with repository details, or None if not a git repo
    """
    workspace = Path(workspace_path)

    # Check if it's a git repository
    if not (workspace / ".git").exists():
        logger.debug(f"Not a git repository: {workspace}")
        return None

    info = GitInfo()

    try:
        # Get remote URL (prefer 'origin')
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=workspace,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            info.remote_url = result.stdout.strip()
        else:
            # Try to get any remote
            result = subprocess.run(
                ["git", "remote"],
                cwd=workspace,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0 and result.stdout.strip():
                remote = result.stdout.strip().split("\n")[0]
                result = subprocess.run(
                    ["git", "remote", "get-url", remote],
                    cwd=workspace,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    info.remote_url = result.stdout.strip()

        # Get current commit hash
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=workspace,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            info.commit = result.stdout.strip()

        # Get current branch
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=workspace,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            info.branch = result.stdout.strip()
            if info.branch == "HEAD":
                # Detached HEAD state
                info.branch = None

        # Check if current commit is pushed to remote
        if info.commit and info.remote_url:
            result = subprocess.run(
                ["git", "branch", "-r", "--contains", info.commit],
                cwd=workspace,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0 and result.stdout.strip():
                info.is_pushed = True

        # Build base URL for source links
        if info.remote_url:
            info.base_url = _parse_remote_url(info.remote_url)

        # Determine the ref to use in URLs
        if info.is_pushed and info.commit:
            # Use commit hash for permalink if pushed
            info.ref = info.commit
        elif info.branch:
            # Fall back to branch name
            info.ref = info.branch

        logger.debug(f"Git info: {info}")
        return info

    except Exception as e:
        logger.warning(f"Failed to get git info: {e}")
        return None


def _parse_remote_url(remote_url: str) -> str | None:
    """
    Parse a git remote URL and return a base HTTPS URL for the repository.

    Supports:
    - GitHub: git@github.com:org/repo.git or https://github.com/org/repo.git
    - GitLab: git@gitlab.com:org/repo.git or https://gitlab.com/org/repo.git
    - Bitbucket: git@bitbucket.org:org/repo.git or https://bitbucket.org/org/repo.git

    Args:
        remote_url: Git remote URL

    Returns:
        Base HTTPS URL (e.g., https://github.com/org/repo) or None
    """
    # SSH format: git@github.com:org/repo.git
    ssh_match = re.match(r"git@([^:]+):(.+?)(?:\.git)?$", remote_url)
    if ssh_match:
        host = ssh_match.group(1)
        path = ssh_match.group(2)
        return f"https://{host}/{path}"

    # HTTPS format: https://github.com/org/repo.git
    https_match = re.match(r"https?://([^/]+)/(.+?)(?:\.git)?$", remote_url)
    if https_match:
        host = https_match.group(1)
        path = https_match.group(2)
        return f"https://{host}/{path}"

    logger.debug(f"Could not parse remote URL: {remote_url}")
    return None


def build_source_url(
    git_info: GitInfo,
    file_path: str,
    start_line: int | None = None,
    end_line: int | None = None,
) -> str | None:
    """
    Build a URL to view a file in the remote repository.

    Args:
        git_info: GitInfo object with repository details
        file_path: Relative path to the file within the repository
        start_line: Optional starting line number (1-based)
        end_line: Optional ending line number (1-based)

    Returns:
        URL to view the file, or None if cannot be built
    """
    if not git_info or not git_info.base_url or not git_info.ref:
        return None

    base_url = git_info.base_url
    ref = git_info.ref

    # Determine the host to format line numbers correctly
    if "github.com" in base_url:
        # GitHub: /blob/ref/path#L1-L10
        url = f"{base_url}/blob/{ref}/{file_path}"
        if start_line:
            url += f"#L{start_line}"
            if end_line and end_line != start_line:
                url += f"-L{end_line}"
    elif "gitlab.com" in base_url or "gitlab" in base_url.lower():
        # GitLab: /-/blob/ref/path#L1-10
        url = f"{base_url}/-/blob/{ref}/{file_path}"
        if start_line:
            url += f"#L{start_line}"
            if end_line and end_line != start_line:
                url += f"-{end_line}"
    elif "bitbucket.org" in base_url:
        # Bitbucket: /src/ref/path#lines-1:10
        url = f"{base_url}/src/{ref}/{file_path}"
        if start_line:
            url += f"#lines-{start_line}"
            if end_line and end_line != start_line:
                url += f":{end_line}"
    else:
        # Generic fallback - just link to file
        url = f"{base_url}/blob/{ref}/{file_path}"
        if start_line:
            url += f"#L{start_line}"

    return url
