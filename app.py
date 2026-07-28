from model import llm
from prompts import teacher_prompt, career_prompt, review_prompt

print("===== LangChain AI Assistant =====")

while True:
    print("\n1. Teacher")
    print("2. Career Advisor")
    print("3. Code Reviewer")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        break

    question = input("Enter your question: ")

    if choice == "1":
        chain = teacher_prompt | llm
    elif choice == "2":
        chain = career_prompt | llm
    elif choice == "3":
        chain = review_prompt | llm
    else:
        print("Invalid choice")
        continue

    response = chain.invoke({"question": question})

    print("\nAI Response:\n")
    print(response.content)