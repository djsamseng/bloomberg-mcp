# Bloomberg MCP

A MCP server providing financial data from Bloomberg blpapi

## Installation
### Using [UV](https://docs.astral.sh/uv/getting-started/installation/)
```bash
uv add git+https://github.com/djsamseng/bloomberg-mcp
```

### Using PIP
```bash
pip3 install git+https://github.com/djsamseng/bloomberg-mcp
```


## Run the MCP Server
```bash
python3 -m bloomberg_mcp
```


## Development
### Requirements
1. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Clone this repository
```bash
git clone https://github.com/djsamseng/bloomberg-mcp
```
3. Setup the venv
```bash
uv venv
source .venv/bin/activate
```
4. Run the MCP server
```bash
uv run bloomberg-mcp
```
