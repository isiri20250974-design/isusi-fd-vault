import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Initialize FastAPI App
app = FastAPI(title="ISUSI AI Agent Backend")

# Endpoint Input Schema
class AgentRequest(BaseModel):
    agent: str

@app.post("/run")
async def run_agent(req: AgentRequest):
    """
    Executes the requested agent and converts stringified JSON outputs 
    into true JSON objects before responding.
    """
    try:
        # Dummy Agent output simulating OpenAI Agents SDK / Groq response
        # Replace this placeholder block with your actual `Runner.run()` logic
        raw_agent_output = '{"advice": [{"id": "722a2ffe-979e-46bc-a205-6c794b16103a", "action": "HOLD", "reason": "Interest rate is locked at optimal 7.2%."}]}'
        session_id = "3757353f-be2f-417e-9e58-7899127e55f4"

        # 🟢 FIX: Convert raw JSON string into a native Python dict/list
        if isinstance(raw_agent_output, str):
            try:
                final_result = json.loads(raw_agent_output)
            except json.JSONDecodeError:
                final_result = raw_agent_output
        else:
            final_result = raw_agent_output

        return {
            "result": final_result,
            "session_id": session_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve HTML Page directly
@app.get("/")
async def serve_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)