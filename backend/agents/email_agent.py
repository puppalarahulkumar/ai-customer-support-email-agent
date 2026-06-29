from typing import Literal

from langchain.tools import tool

from langchain_protocol import TypedDict
from langgraph.graph import END, START, StateGraph

from classifier_agent import EmailClassification
from classifier_agent import ClassifierAgent

class EmailAgentState(TypedDict):
    # Raw email data
    email_content: str
    sender_email: str
    email_id: str

    # Classification result
    classification: EmailClassification | None

    # Raw search/API results
    search_results: list[str] | None  # List of raw document chunks
    customer_history: dict | None  # Raw customer data from CRM

    # Generated content
    draft_response: str | None
    messages: list[str] | None


# @tool
# def read_email(state: EmailAgentState):
#     state["email_content"] = "How do I reset my password?"
#     state["sender_email"] = "contact.rahulpuppala@gmail.com"
#     state["email_id"] = "email_12345"
    
# this logic is for langgraph, same meaning as above this code:


# def read_email(state: EmailAgentState):
#     print("reading the email")
#     return {
#         "email_content": "How do I reset my password?",
#         "sender_email": "contact.rahulpuppala@gmail.com",
#         "email_id": "email_12345"
#     }

class EmailAgent:   
    def classify_intent(state: EmailAgentState):
        classifier = ClassifierAgent()
        classification = classifier.classify(state["email_content"])
        
            
    
        return {
            "classification":classification
        }


    def should_call_search(state: EmailAgentState)-> Literal["search_documentation", "human_review"]:
        """this tool is used to call the search tool"""
        classification = state.get("classification")
        if classification["intent"] == "billing" or classification["urgency"] in ["high", "critical"]:
            return "human_review"
        return "search_documentation"


    def search_documentation(state: EmailAgentState):
        """This tool is used to call the search documentation feature"""
        from doc_agent import DocSearchAgent
        print("entered the search documentation")
        doc_search_agent = DocSearchAgent()
        search_results=doc_search_agent.search_docs(state["email_content"])

        print("searched the documentation ")
        return {
            "search_result" : search_results
        }

    @tool
    def draft_response(state: EmailAgentState):
        """Draft the appropiate response for the mail"""

        from backend.agents.response_agent import ResponseAgent
        response_agent = ResponseAgent()
        context = state.get("search_results", [])
        response = response_agent.generate_response(state["email_content"], context)
        return {
            "draft_response": response
        }

    @tool
    def send_reply(state: EmailAgentState):
        """we will send responses to the customers here."""
        print("we have sent the reply")

    @tool
    def human_review(state: EmailAgentState):
        """This triggers and send the mail to the teams if any emergency situation is there"""
        from backend.agents.human_agent import HumanAgent
        human_agent = HumanAgent(state["sender_email"])
        print("human review")
        human_agent.send_mail(state["sender_email"], state["draft_response"])

    workflow = StateGraph(EmailAgentState)


    # Add nodes with appropriate error handling

    workflow.add_node("classify_intent", classify_intent)

    # Add retry policy for nodes that might have transient failures
    workflow.add_node(
        "search_documentation",
        search_documentation, 
    )
    # workflow.add_node("bug_tracking", bug_tracking)
    workflow.add_node("draft_response", draft_response)
    workflow.add_node("human_review", human_review)
    workflow.add_node("send_reply", send_reply)

    # Add only the essential edges
    workflow.add_edge(START,"classify_intent")
    workflow.add_conditional_edges(
        "classify_intent",
        should_call_search,
        ["search_documentation", "human_review"]
    )

    workflow.add_edge("search_documentation", "draft_response")
    workflow.add_edge("human_review",END )

    workflow.add_edge("draft_response", "send_reply")

    workflow.add_edge("send_reply", END)

    # Compile with checkpointer for persistence, in case run graph with Local_Server --> Please compile without checkpointer
    # memory = InMemorySaver()
    app = workflow.compile()

