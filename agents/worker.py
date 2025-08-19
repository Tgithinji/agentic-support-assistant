from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .memory import memory

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Worker Agent (responds to tickets)
response_prompt = PromptTemplate(
    input_variables=["ticket", "category"],
    template="""
    You are a worker agent handling {category} issues.
    Based on the ticket below, generate a helpful reply.

    Ticket: {ticket}
    """
)

worker_chain = LLMChain(
    llm=llm, prompt=response_prompt, memory=memory
)

def handle_response(ticket_text: str, category: str) -> str:
    return worker_chain.run(ticket=ticket_text, category=category)
