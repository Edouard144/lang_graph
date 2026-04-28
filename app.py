import os
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
from dotenv import load_dotenv


# loading the enviromental variables
load_dotenv()


#Creating the state that will be shared by all Agents
class State(TypedDict):
    question: str
    answer: str


#setting up the LLM model to use -- which is the brain of our agents
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key= os.getenv("GROQ_API_KEY"),
)


# NODES -- receives state and returns the updated state

   # researcher_node
def researcher_node(state: State):
    """Node 1 - Researches the questions"""
    question = state["question"]
    response = llm.invoke(f"Reasearch this topic briefly: {question}")
    return {"answer": response.content}

def writer_node(state: State):
    """Node 2 - Reads the research and writes the answer"""
    answer = state["answer"]
    response = llm.invoke(f"Write a summary from this answer: {answer}")
    return {"answer": response.content}



# GRAPH
graph = StateGraph(State)

graph.add_node("researcher", researcher_node)
graph.add_node("writer", writer_node)

graph.set_entry_point("researcher")

graph.add_edge("researcher", "writer")
graph.add_edge("writer", END)

app = graph.compile()



# RUNNING the thing
result = app.invoke({
    "question": "Why does a turtor live many years?",
    "answer" : ""
 })

print(result)

