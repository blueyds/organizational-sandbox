from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request format

class AgentRequest(BaseModel):
    question: str


# Simulated organizational knowledge

purchase_orders = {
    "PO123": {
        "status": "Delayed",
        "reason": "Vendor tax information missing"
    }
}


@app.get("/")
def home():
    return {
        "organization": "Contoso Test Company",
        "status": "Online"
    }


@app.post("/agent/procurement")
def procurement_agent(request: AgentRequest):

    if "PO123" in request.question:

        po = purchase_orders["PO123"]

        return {
            "agent": "Procurement Specialist",
            "status": po["status"],
            "answer": po["reason"]
        }

    return {
        "agent": "Procurement Specialist",
        "answer": "No information found."
    }
