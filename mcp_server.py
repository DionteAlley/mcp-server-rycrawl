class MCPServer:
    def __init__(self):
        self.version = "1.0.0"

    def run_scan(self, asset: str):
        return {
            "asset": asset,
            "critical_vulns": 1,
            "high_vulns": 4,
            "medium_vulns": 2,
            "low_vulns": 7,
            "message": f"Scan completed for {asset}"
        }

    def handle_message(self, data):
        msg_type = data.get("type")

        if msg_type == "PING":
            return {"type": "PONG", "server_version": self.version}

        if msg_type == "SCAN":
            asset = data.get("asset", "unknown")
            return self.run_scan(asset)

        return {"error": "Unknown MCP message type"}
