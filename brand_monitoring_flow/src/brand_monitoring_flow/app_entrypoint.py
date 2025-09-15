from bedrock_agentcore.runtime import BedrockAgentCoreApp
from brand_monitoring_flow.brand_monitoring_flow.main import BrandMonitoringFlow


app = BedrockAgentCoreApp()


@app.entrypoint
def app_entry(payload, context):
    try:
        flow = BrandMonitoringFlow()
        flow.kickoff()
        return {"result": "ok"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run()


