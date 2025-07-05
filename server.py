from mcp.server.fastmcp import FastMCP
import subprocess
from typing import Optional

mcp = FastMCP("Kubescape CLI Server")

# SECURITY NOTE: Executing shell commands from user input can be dangerous.
# Always validate and sanitize inputs to avoid command injection vulnerabilities.
# Only expose safe, well-defined parameters to the CLI.

@mcp.tool()
def kubescape_scan(args: Optional[str] = None) -> str:
    """Run 'kubescape scan' with optional arguments (e.g., resource type, file, or directory)."""
    cmd = ["kubescape", "scan"]
    if args:
        cmd += args.split()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr or str(e)}"

@mcp.tool()
def kubescape_scan_framework(framework: str, args: Optional[str] = None) -> str:
    """Run 'kubescape scan framework <framework>' with optional extra arguments."""
    cmd = ["kubescape", "scan", "framework", framework]
    if args:
        cmd += args.split()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr or str(e)}"

@mcp.tool()
def kubescape_scan_workload(workload: str, namespace: Optional[str] = None, args: Optional[str] = None) -> str:
    """Run 'kubescape scan workload <workload>' with optional namespace and extra arguments."""
    cmd = ["kubescape", "scan", "workload", workload]
    if namespace:
        cmd += ["--namespace", namespace]
    if args:
        cmd += args.split()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr or str(e)}"

@mcp.tool()
def kubescape_scan_image(image: str, args: Optional[str] = None) -> str:
    """Run 'kubescape scan image <image>' with optional extra arguments."""
    cmd = ["kubescape", "scan", "image", image]
    if args:
        cmd += args.split()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr or str(e)}"

if __name__ == "__main__":
    mcp.run("stdio")
