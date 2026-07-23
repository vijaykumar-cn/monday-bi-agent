from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.agent_service import AgentService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

agent = AgentService()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = agent.chat(request.message)

    return ChatResponse(answer=answer)