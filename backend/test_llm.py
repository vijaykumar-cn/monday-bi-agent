from app.services.llm_service import LLMService

llm = LLMService()

print("Sending request...")

answer = llm.ask("Explain what business intelligence means in 3 lines.")

print(answer)