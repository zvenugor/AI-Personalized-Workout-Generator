import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_workout(user_info):
    prompt = f"Based on the following user information: {user_info}, generate a personalized weekly workout plan with daily exercises and rest days."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a personal trainer expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    info = input("Enter your workout preferences, goals, and limitations: ")
    workout_plan = generate_workout(info)
    print("Personalized Workout Plan:\n", workout_plan)
