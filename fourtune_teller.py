import random
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def fortune_teller(roll):
    if roll == 1:
        prompt = "Create a 1 sentence laughable fortune very bad and evil and make it sound like a fortune."
    elif roll == 2:
        prompt = "Create a 1 sentence laughable fortune very good and make it sound like a fortune."
    
    else:
        prompt = "Create a 1 sentence confusing, weird, or neutral fortune and make it sound like a fortune."

    # Use the correct, official OpenAI API method for text generation
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    print("\nFORTUNE:", response.choices.message.content.strip(), "\n")


print("Welcome to your fortune teller!\n")

while True:
    user_input = input("Press enter to roll the dice for your future! Or type 'quit' to exit: ").strip().lower()
    
    # Single, case-insensitive exit point
    if user_input == "quit":
        print("Thanks for playing! Goodbye.")
        break

    # Triggers the dice roll and function
    roll = random.randint(1, 3)
    fortune_teller(roll)