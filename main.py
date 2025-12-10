from fastapi import FastAPI
from mcp_server import MCPServer

app = FastAPI()
mcp = MCPServer()

@app.get("/")
def root():
    return {"status": "Rycrawl MCP Server running"}

@app.get("/scan")
async def scan(asset: str = "default"):
    result = mcp.run_scan(asset)
    return {"asset": asset, "result": result}

@app.post("/mcp/message")
async def mcp_message(data: dict):
    response = mcp.handle_message(data)
    return response
