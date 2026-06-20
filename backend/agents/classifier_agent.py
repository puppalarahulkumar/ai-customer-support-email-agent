

from typing import Literal

from langchain_protocol import TypedDict
from chat_generation import ChatGenerationAgent

class EmailClassification(TypedDict):
    intent: Literal["question", "bug", "billing", "feature", "complex"]
    urgency: Literal["low", "medium", "high", "critical"]
    topic: str
    summary: str


# this classifies the Email by invoking the llm.

class ClassifierAgent:

    def __init__(self):
        print("******in the classifier agent********")
        self.model=ChatGenerationAgent().model
        self.model_w_structured_output=self.model.with_structured_output(
            EmailClassification
        )



    def classify(self,email_content):

        prompt = f"""
                You are a customer support classification agent.

                Possible intents:
                - question
                - bug
                - billing
                - feature_request
                - complex

                Possible urgency:
                - low
                - medium
                - high
                - critical

                Rules:
                - Billing disputes -> high
                - API failures -> critical
                - Feature requests -> low
                - Password reset questions -> low

                Customer Email:
                {email_content}
                """

        return self.model_w_structured_output.invoke(prompt)