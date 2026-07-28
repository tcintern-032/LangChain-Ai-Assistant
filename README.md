# LangChain-Ai-Assistant
A simple AI Assistant built using **LangChain** and **OpenAI**. This project demonstrates the core concepts of LangChain, including Chat Models, Prompt Templates, model invocation, and the basic LangChain workflow.
## Project Objective
The objective of this project is to build a simple AI assistant that:
- Accepts user input
- Uses LangChain Prompt Templates
- Sends prompts to an OpenAI Chat Model
- Returns AI-generated responses
- Demonstrates different AI roles using prompt templates
## Features
- Interactive command-line application
- Multiple AI assistant roles
  -  Teacher
  -  Career Advisor
  -  Code Reviewer
- Uses LangChain Chat Models
- Uses Prompt Templates
- Environment variables with `.env`
- Organized project structure
- Direct OpenAI API comparison
# Project Structure
```text
langchain-ai-assistant/
│
├── app.py
├── config.py
├── models.py
├── prompts.py
├── compare_direct_api.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
# Technologies Used
- Python 3.10+
- LangChain
- LangChain OpenAI
- OpenAI API
- Python Dotenv
# Configure API Key

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key_here
```
# Run the Application
```bash
python app.py
```
# Application Workflow
```
===============================
LangChain AI Assistant
===============================

1. Teacher
2. Career Advisor
3. Code Reviewer
4. Exit

Choose an option:

Enter your question:

AI Response:
```
# Prompt Templates
The project contains three different prompt templates.
### Teacher
Explains concepts in a simple and easy-to-understand way.
Example:

```
Explain Artificial Intelligence
```
### Career Advisor
Provides career guidance and learning recommendations.
Example:

```
How can I become an AI Engineer?
```
### Code Reviewer

Reviews code and suggests improvements.
Example:

```python
def add(a,b):
 return a+b
```
# LangChain Workflow

```
User Input
      │
      ▼
Prompt Template
      │
      ▼
Chat Model
      │
      ▼
AI Response
```
# Project Files

## app.py

Main application that accepts user input and invokes the LangChain model.

---

## config.py

Loads environment variables and configuration.

---

## models.py

Creates the LangChain Chat Model.

---

## prompts.py

Contains all Prompt Templates.

---

## compare_direct_api.py

Demonstrates the previous implementation using the OpenAI API directly for comparison.

---

## requirements.txt

Contains all required Python packages.

---

## .env

Stores the OpenAI API Key.

---

# Direct API vs LangChain

| Direct OpenAI API | LangChain |
|-------------------|------------|
| Manual prompt creation | Prompt Templates |
| Manual API calls | Chat Model abstraction |
| Less reusable | Highly reusable |
| More boilerplate code | Cleaner code |
| Harder to scale | Easy to scale |
# Sample Output

```
==================================
LangChain AI Assistant
==================================

1. Teacher
2. Career Advisor
3. Code Reviewer
4. Exit

Choose an option: 1

Enter your question:

What is Machine Learning?

AI Response:

Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions without being explicitly programmed.
```
# Requirements

- Python 3.10 or later
- OpenAI API Key
- Internet Connection

---
# Dependencies

```
langchain
langchain-openai
openai
python-dotenv
```
# Learning Outcomes
After completing this project, you will understand:
- What LangChain is
- How Chat Models work
- How Prompt Templates simplify prompting
- How to invoke an LLM using LangChain
- How LangChain differs from direct OpenAI API calls
- How to organize a basic LangChain application
# Future Improvements
- Add Conversation Memory
- Build a Web Interface using FastAPI or Streamlit
- Add More Prompt Templates
- Support Multiple LLM Providers
- Store Chat History
- Add Streaming Responses
# Author
**Devolped By M Zeeshan**
