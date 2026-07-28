from langchain_core.prompts import ChatPromptTemplate

teacher_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful teacher.

Question:
{question}
"""
)

career_prompt = ChatPromptTemplate.from_template(
    """
You are an experienced career advisor.

Question:
{question}
"""
)

review_prompt = ChatPromptTemplate.from_template(
    """
You are a professional code reviewer.

Code:
{question}
"""
)