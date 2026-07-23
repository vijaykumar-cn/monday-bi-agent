from app.services.monday_service import MondayService
from app.services.analytics import Analytics
from app.services.llm_service import LLMService


class AgentService:

    def __init__(self):
        self.monday = MondayService()
        self.llm = LLMService()

    def chat(self, question: str):

        question_lower = question.lower()

        # Decide which board to use
        if "work order" in question_lower or "workorder" in question_lower:
            df = self.monday.get_workorders()
            board_name = "Work Orders"
        else:
            df = self.monday.get_deals()
            board_name = "Deals"

        # Run analytics
        summary = Analytics.dashboard_summary(df)

        prompt = f"""
You are an expert Business Intelligence Analyst.

The following data comes from the Monday.com "{board_name}" board.

User Question:
{question}

Business Data:
{summary}

Instructions:
- Answer ONLY using the provided data.
- Never invent numbers.
- Be concise and professional.
- Structure your response as:

Executive Summary

Key Insights

Recommendations
"""

        answer = self.llm.ask(prompt)

        return answer