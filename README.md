# LangGraph Lab 🔗

This repository contains my learning experiments with **LangGraph**, focusing on building dynamic AI workflows using nodes, edges, and shared state.

---

##  What I Learned

* Graph-based workflows (nodes & edges)
* State management (shared memory between nodes)
* How AI tasks can flow and transform step-by-step
* Difference between linear flows (CrewAI) and graph-based systems (LangGraph)

---

## ⚙️ Project Overview

This project demonstrates a simple **2-node LangGraph system**:

### 🔹 Nodes

* **Researcher Node** → takes a question and generates a response
* **Writer Node** → simplifies and improves the response

### 🔹 Flow

Question → Researcher → Writer → Final Answer

---

##  Key Concepts

* **Node** → a function that performs a task
* **Edge** → defines the flow between nodes
* **State** → shared data passed between nodes
* **Graph** → controls execution order and logic

---

## 🛠️ Tech Stack

* Python
* LangGraph
* Groq API (via langchain-groq)
* LangChain

---

##  How to Run

1. Install dependencies:

```bash
pip install langgraph langchain-groq python-dotenv
```

2. Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

3. Run the script:

```bash
python app.py
```

---

## 🎯 Goal

To understand how to build more advanced AI systems that can:

* make decisions
* loop through tasks
* dynamically control execution flow

---

More advanced graph-based AI systems coming soon 🚀
