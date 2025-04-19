# BLPAPI-MCP

A MCP server providing financial data from Bloomberg's blpapi.

Note: A Bloomberg Terminal must be running (BBComm must be accessible) for data access.

## Installation
### Using [UV](https://docs.astral.sh/uv/getting-started/installation/)


```bash
uv add git+https://github.com/djsamseng/blpapi-mcp
```

## Run the MCP Server
```bash
uv run blpapi-mcp --sse --host 127.0.0.1 --port 8000
```

## Using blpapi-cmp from [Cursor](https://docs.cursor.com/context/model-context-protocol)
- For project only: create .cursor/mcp.json in your project directory
- For global: create `~/.cursor/mcp.json`
- Replace the host and port with the MCP server running from above
```json
{
  "mcpServers": {
    "server-name": {
      "url": "http://127.0.0.1:8000/sse",
    }
  }
}
```

## Using blpapi-mcp from [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp)
- Replace the url with the MCP server running from above
```bash
claud mcp add --transport sse blpapi-mcp http://127.0.0.1:8000/sse
```
- [Remote hosts for Claude Desktop is still in development](https://modelcontextprotocol.io/quickstart/user#1-download-claude-for-desktop)

## Using blpapi-mcp from [Aider](https://aider.chat/)
- [Pull request pending](https://github.com/Aider-AI/aider/pull/3672)

## Development
### Requirements
1. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Clone this repository
```bash
git clone https://github.com/djsamseng/blpapi-mcp
```
3. Setup the venv
```bash
uv venv
source .venv/bin/activate
```
4. Run the MCP server
```bash
uv run blpapi-mcp --sse --host 127.0.0.1 --port 8000
```
5. Run a test client that starts up it's own server in stdio mode
```bash
uv run examples/clients/blp_stdio_client.py
```
6. Run a test client that uses an existing running sse server
```bash
uv run examples/clients/blp_sse_client.py --host http://127.0.0.1 --port 8000
```

## Trademark Note
This project not affiliated with Bloomberg Finance L.P. The use of the name Bloomberg is only descriptive as towards what this package is used with.
