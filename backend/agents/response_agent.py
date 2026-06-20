from agents.chat_generation import ChatGenerationAgent

class ResponseAgent:
    def generate_response(self, query, context):
        ChatAgent = ChatGenerationAgent()
        response = ChatAgent.generate_response(query, context)
        return response

