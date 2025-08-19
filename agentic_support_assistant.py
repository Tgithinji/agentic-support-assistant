from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import faiss


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

memory = ConversationBufferMemory()

# ----- SUPERVISOR AGENT -----
classification_prompt = PromptTemplate(
    input_variables=["ticket"],
    template="""
    You are a supervisor agent. 
    Classify the following ticket into one of: [Technical, Billing, General].
    Ticket: {ticket}
    Respond with just the category.
    """
)

supervisor_chain = LLMChain(
    llm=llm, prompt=classification_prompt, memory=memory
)

# ----- WORKER AGENT -----
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

