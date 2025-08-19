from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import faiss


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Memory for context persistence
memory = ConversationBufferMemory()

