#================================================
import openai
import random
import os

OpenAI_API_Key = "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"
openai.api_key = OpenAI_API_Key

def generate_question(topic_name):
    user_message = f"Generate a one-line interview level leetcode question on {topic_name}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

def get_existing_questions(file_path):
    try:
        with open(file_path, "r") as file:
            existing_questions = file.read().splitlines()
        return existing_questions
    except FileNotFoundError:
        return []

def main(class_name, subject_name, unit_name, topic_name):
    # Create directory structure
    directory = os.path.join("Assengment_Data", class_name, subject_name, unit_name)
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{topic_name}_questions.txt")


    # Get existing questions
    existing_questions = get_existing_questions(file_path)

    if len(existing_questions) < 10:
        # Generate a new question
        new_question = generate_question(topic_name)

        # Append the new question to the file
        with open(file_path, "a") as file:
            file.write(f"{new_question}\n")
        return new_question
        # print(f"New question appended to: {file_path}: {new_question}")
    else:
        # Randomly select and print a question from the existing questions
        random_question = random.choice(existing_questions)
        # print(f"Random question from: {file_path}: {random_question}")
        return random_question

# if _name_ == "_main_":
#     main()