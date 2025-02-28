def kbc_game():
    # List of questions, options, answers, and prize money
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai"],
            "answer": 2,
            "prize": 1000,
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": 3,
            "prize": 10000,
        },
        {
            "question": "Who is known as the 'Missile Man of India'?",
            "options": ["1. Mahatma Gandhi", "2. APJ Abdul Kalam", "3. Vikram Sarabhai", "4. Homi Bhabha"],
            "answer": 2,
            "prize": 100000,
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["1. China", "2. Japan", "3. Korea", "4. Thailand"],
            "answer": 2,
            "prize": 1000000,
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["1. O2", "2. CO2", "3. H2O", "4. NaCl"],
            "answer": 3,
            "prize": 10000000,
        },
        {
            "question": "Who wrote the Indian National Anthem?",
            "options": ["1. Rabindranath Tagore", "2. Bankim Chandra Chatterjee", "3. Sarojini Naidu", "4. Subhash Chandra Bose"],
            "answer": 1,
            "prize": 50000000,
        },
        {
            "question": "Which is the longest river in the world?",
            "options": ["1. Nile", "2. Amazon", "3. Ganges", "4. Yangtze"],
            "answer": 1,
            "prize": 70000000,
        },
    ]

    print("Welcome to Kaun Banega Crorepati!")
    total_prize = 0

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        # Get user's answer
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == q['answer']:
                total_prize = q['prize']
                print(f"Correct! You have won INR {total_prize} so far.")
            else:
                print("Wrong answer. Game over!")
                break
        except ValueError:
            print("Invalid input. Game over!")
            break

    # Display the final prize amount
    print("\nThank you for playing Kaun Banega Crorepati!")
    if total_prize == 70000000:
        print("Congratulations! You are a Crorepati! You won INR 7 Crore!")
    else:
        print(f"You won a total of INR {total_prize}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    kbc_game()
