## 🗂 Python Interview Q&A

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is Python? | Python is a high-level, interpreted programming language known for its simple and readable syntax. |
| Q2 | Why is Python popular? | Python is popular because it is easy to learn, versatile, and widely used in many fields. |
| Q3 | What are the key features of Python? | Python is simple, platform-independent, object-oriented, and has a large collection of libraries. |
| Q4 | Is Python compiled or interpreted? | Python is an interpreted language that executes code line by line. |
| Q5 | What are variables in Python? | Variables are used to store and manage data in a program. |
| Q6 | What are data types in Python? | Data types define the kind of value a variable can store. |
| Q7 | What is an integer (int)? | An integer is a whole number without a decimal point. |
| Q8 | What is a float? | A float is a number that contains a decimal point. |
| Q9 | What is a string? | A string is a sequence of characters enclosed in quotes. |
| Q10 | What is a boolean? | A boolean represents either True or False. |
| Q11 | What is a list? | A list is an ordered and mutable collection of items. |
| Q12 | What is a tuple? | A tuple is an ordered and immutable collection of items. |
| Q13 | What is a set? | A set is an unordered collection of unique values. |
| Q14 | What is a dictionary? | A dictionary stores data as key-value pairs. |
| Q15 | What is None in Python? | None represents the absence of a value. |
| Q16 | What is type casting? | Type casting is the process of converting one data type into another. |
| Q17 | What is the difference between List and Tuple? | Lists can be modified, while tuples cannot be changed after creation. |
| Q18 | What is the difference between List and Set? | Lists allow duplicate values, while sets store only unique values. |
| Q19 | What is the type() function? | The type() function is used to find the data type of a value or variable. |
| Q20 | What are Python keywords? | Keywords are reserved words that have special meanings in Python. |
| Q21 | What is an operator? | An operator is a symbol used to perform operations on values and variables. |
| Q22 | What is an if statement? | An if statement is used to execute code only when a condition is true. |
| Q23 | What is an if-else statement? | An if-else statement executes one block of code if a condition is true and another if it is false. |
| Q24 | What is an elif statement? | An elif statement is used to check multiple conditions after an if statement. |
| Q25 | What is a for loop? | A for loop is used to iterate over a sequence of items. |
| Q26 | What is a while loop? | Repeatedly executes code as long as a condition remains true. |
| Q27 | What is the break statement? | Immediately exits a loop. |
| Q28 | What is the continue statement? | Skips the current iteration and moves to the next one. |
| Q29 | What is a function? | A reusable block of code that performs a specific task. |
| Q30 | Why are functions used? | To organize code, reduce repetition, and improve readability. |
| Q31 | What are function arguments? | Values passed to a function when it is called. |
| Q32 | What is a return statement? | A return statement sends a value back from a function. |
| Q33 | What is a lambda function? | A lambda function is a small anonymous function written in a single line. |
| Q34 | What is recursion? | Recursion is a technique where a function calls itself. |
| Q35 | What is a module? | A module is a Python file that contains reusable code. |
| Q36 | What is a package? | A package is a collection of related Python modules. |
| Q37 | What is PIP? | PIP is Python's package manager used to install and manage libraries. |
| Q38 | What is an exception? | An exception is an error that occurs during program execution. |
| Q39 | What is exception handling? | Exception handling is the process of managing errors without stopping the program. |
| Q40 | What is a class? | A class is a blueprint used to create objects. |
| Q41 | What is an object? | An object is an instance of a class. |
| Q42 | What is a constructor? | A constructor is a special method that runs automatically when an object is created. |
| Q43 | What is inheritance? | Inheritance allows one class to acquire properties and methods from another class. |
| Q44 | What is polymorphism? | Polymorphism allows the same method name to perform different actions. |
| Q45 | What is encapsulation? | Encapsulation is the process of bundling data and methods into a single unit. |
| Q46 | What is abstraction? | Abstraction hides implementation details and shows only essential features. |
| Q47 | What is a decorator? | A decorator is a function used to modify the behavior of another function. |
| Q48 | What is a generator? | A generator is a function that produces values one at a time instead of all at once. |
| Q49 | What is a virtual environment? | A virtual environment is an isolated workspace used to manage project dependencies. |

### Chroma

**What it is:** Chroma (ChromaDB) is an open-source, AI-native **vector database**. It stores text as embeddings (numeric vectors that capture meaning) alongside the original documents and metadata, and lets you query by semantic similarity instead of exact keyword matches.

**How we use it:**
1. Take source documents (PDFs, docs, chat history, etc.) and split them into chunks.
2. Pass each chunk through an embedding model to generate a vector.
3. Store the vector + original text + metadata in a Chroma collection.
4. At query time, embed the user's question and ask Chroma for the most similar stored vectors (semantic search).
5. Feed those retrieved chunks into an LLM as context — this is the retrieval step in **RAG (Retrieval-Augmented Generation)**.

**Why we use it:**
- **Rapid prototyping** — zero setup; installs locally with `pip install chromadb`, no Docker or cloud account required.
- **Built-in convenience** — handles tokenization, embedding generation, and indexing for you.
- **Hybrid search** — combines vector similarity with metadata filtering and full-text search.
- **Framework friendly** — integrates natively with LangChain, LlamaIndex, and similar tools.
- **Scalable** — runs locally for small projects, with serverless/cloud options for production.

**When we use it:**
- Local RAG projects
- AI prototypes
- Document retrieval / semantic search over private data

**Interview Q&A:**

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is Chroma? | An open-source, AI-native vector database used to store and query document embeddings for LLM applications. |
| Q2 | What problem does a vector database solve? | Traditional databases match on exact values; a vector database finds items that are semantically similar by comparing embedding vectors, enabling "search by meaning." |
| Q3 | What is an embedding? | A numeric vector representation of text (or other data) produced by a model, positioned so that semantically similar items are close together in vector space. |
| Q4 | How does Chroma fit into a RAG pipeline? | It stores document embeddings and retrieves the most relevant chunks for a query, which are then passed to an LLM as context so it can generate a grounded answer. |
| Q5 | Is Chroma suitable for production at scale? | It's ideal for local/prototype use out of the box, and also offers a hosted/cloud option for scaling in production. |

### FastAPI

**What it is:** A modern Python web framework for building high-performance APIs, built on top of Starlette (for the web layer) and Pydantic (for data validation).

**Why we use it:**
- **Blazing fast** — performance on par with NodeJS and Go, thanks to Starlette and Pydantic under the hood.
- **Rapid development** — minimizes boilerplate code, reportedly increasing development speed by 200–300%.
- **Type-safe validation** — uses standard Python type hints to automatically validate incoming data and catch bugs early.
- **Auto-generated docs** — automatically creates interactive API documentation (Swagger UI and ReDoc) for instant testing.
- **Async native** — supports `async`/`await` out of the box to handle concurrent operations efficiently.

**When we use it:**
- Backend services and microservices
- Machine learning model deployment / inference endpoints
- Any API that needs strong typing, speed, and automatic docs

**Interview Q&A:**

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is FastAPI? | A Python web framework for building APIs quickly with high performance, built on Starlette and Pydantic. |
| Q2 | Why is FastAPI fast? | It's built on Starlette (an ASGI framework) for the networking layer and Pydantic for validation, and it's designed around Python's native `async`/`await` for concurrency. |
| Q3 | How does FastAPI validate request data? | Through Python type hints — you declare the expected types in function signatures/Pydantic models, and FastAPI validates incoming data against them automatically, returning clear errors if it doesn't match. |
| Q4 | How do you get API documentation with FastAPI? | It's generated automatically — Swagger UI is available at `/docs` and ReDoc at `/redoc` with no extra setup. |
| Q5 | How is FastAPI different from Flask? | FastAPI is async-first, uses type hints for automatic validation/serialization, and auto-generates interactive docs; Flask is synchronous by default and requires extra libraries for validation and docs. |

### LangGraph

**What it is:** A library built on top of LangChain for building **stateful, multi-step, and multi-agent LLM applications**, modeled as a graph. Nodes represent steps (an LLM call, a tool call, custom logic) and edges define how control flows between them — including branches, loops, and conditional paths that plain linear chains can't express.

**Why we use it:**
- **Cycles and branching** — supports loops and conditional logic (e.g., "retry until valid," "route to different tools"), which linear LangChain chains don't support well.
- **Persistent state** — built-in state object is passed between nodes and can be checkpointed, so an agent can pause, resume, or recover from failure.
- **Human-in-the-loop** — graphs can pause execution to wait for human approval/input before continuing.
- **Multi-agent orchestration** — makes it straightforward to coordinate multiple specialized agents that hand off work to each other.

**When we use it:**
- Building autonomous or semi-autonomous agents
- Workflows that need retries, branching, or approval steps
- Multi-agent systems where different agents own different sub-tasks

**Interview Q&A:**

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is LangGraph? | A LangChain-based library for building LLM applications as a graph of nodes and edges, supporting stateful, cyclic, and multi-agent workflows. |
| Q2 | How is LangGraph different from a plain LangChain chain? | Chains are linear (A → B → C); LangGraph supports cycles, conditional branching, and persistent state, which is needed for agents that loop, retry, or make decisions about what to do next. |
| Q3 | What is "state" in LangGraph? | A shared object passed between nodes in the graph that each node can read and update, representing the current context/progress of the workflow. |
| Q4 | What does "human-in-the-loop" mean in LangGraph? | The ability to pause graph execution at a defined point and wait for a human to review or approve before the workflow continues. |

### LangChain

**What it is:** An open-source framework for building applications powered by LLMs. It provides standardized abstractions — prompts, chains, memory, agents, document loaders, and retrievers — plus integrations with LLM providers (OpenAI, Anthropic, Ollama, etc.) and vector stores (like Chroma) so you don't have to wire everything together from scratch.

**Why we use it:**
- **Standardized interfaces** — swap between LLM providers or vector stores with minimal code changes.
- **Composable building blocks** — chains let you combine prompts, models, parsers, and tools into a pipeline.
- **Retrieval integration** — first-class support for connecting to vector databases (e.g., Chroma) for RAG.
- **Agent tooling** — built-in patterns for giving an LLM access to tools/functions it can call.
- **Large ecosystem** — extensive library of pre-built loaders, integrations, and community components.

**When we use it:**
- Prototyping LLM-powered apps without reinventing common plumbing
- RAG pipelines (loading, chunking, embedding, retrieving)
- Simple, mostly-linear LLM workflows (for more complex control flow, pair it with LangGraph)

**Interview Q&A:**

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is LangChain? | A framework that provides reusable abstractions (prompts, chains, memory, agents, retrievers) for building applications on top of LLMs. |
| Q2 | What is a "chain" in LangChain? | A sequence of calls (e.g., prompt → LLM → output parser) composed together so data flows through each step automatically. |
| Q3 | How does LangChain relate to Chroma? | LangChain provides a standard interface for vector stores, so it can use Chroma (or another vector DB) as the retrieval backend in a RAG pipeline with minimal integration code. |
| Q4 | When would you choose LangGraph over plain LangChain? | When the workflow needs branching, loops, persistent state, or multiple coordinating agents rather than a simple linear sequence of steps. |

### Ollama

**What it is:** A tool for running open-source LLMs (Llama, Mistral, Gemma, and others) **locally** on your own machine. It packages model weights, configuration, and a runtime behind a simple CLI and local REST API, similar in spirit to how Docker packages containers.

**Why we use it:**
- **Local, private inference** — data never leaves your machine, useful for sensitive data or offline development.
- **No API costs** — no per-token charges since the model runs on local hardware.
- **Simple interface** — pull and run a model with one command (`ollama run llama3`); exposes a local REST API for apps to call.
- **Easy integration** — works as a drop-in LLM provider in frameworks like LangChain and LangGraph.

**When we use it:**
- Local development and testing without cloud API costs
- Privacy-sensitive use cases where data can't leave the machine
- Offline or air-gapped environments
- Quickly experimenting with different open-source models

**Interview Q&A:**

| # | Question | Answer |
|---|----------|--------|
| Q1 | What is Ollama? | A tool for downloading and running open-source LLMs locally, exposing them through a simple CLI and REST API. |
| Q2 | Why use Ollama instead of a cloud LLM API? | For local/offline development, data privacy (nothing leaves the machine), and avoiding per-token API costs. |
| Q3 | How does Ollama fit into a LangChain/LangGraph app? | It can be used as the LLM provider — LangChain and LangGraph both have integrations that let you point chains/agents at a locally running Ollama model instead of a cloud API. |
| Q4 | What's a tradeoff of using Ollama locally? | You're limited by local hardware (CPU/GPU/RAM), so response speed and the size/quality of models you can run are capped compared to large cloud-hosted models. |
