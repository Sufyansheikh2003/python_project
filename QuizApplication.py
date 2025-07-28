quiz = {
    "What is the chemical symbol for water?": {
        "1": "H2O",
        "2": "O2",
        "3": "CO2",
        "4": "NaCl",
        "answer": "1"
    },
    "Which gas do plants absorb from the atmosphere?": {
        "1": "Oxygen",
        "2": "Nitrogen",
        "3": "Carbon Dioxide",
        "4": "Hydrogen",
        "answer": "3"
    },
    "Which planet is known as the Red Planet?": {
        "1": "Earth",
        "2": "Mars",
        "3": "Jupiter",
        "4": "Venus",
        "answer": "2"
    },
    "What is the boiling point of water?": {
        "1": "50°C",
        "2": "90°C",
        "3": "100°C",
        "4": "150°C",
        "answer": "3"
    },
    "Which part of the plant conducts photosynthesis?": {
        "1": "Root",
        "2": "Stem",
        "3": "Flower",
        "4": "Leaf",
        "answer": "4"
    },
    "Which vitamin is produced when the human skin is exposed to sunlight?": {
        "1": "Vitamin A",
        "2": "Vitamin B",
        "3": "Vitamin C",
        "4": "Vitamin D",
        "answer": "4"
    },
    "How many bones are in the adult human body?": {
        "1": "206",
        "2": "210",
        "3": "201",
        "4": "198",
        "answer": "1"
    },
    "Which gas is essential for human respiration?": {
        "1": "Hydrogen",
        "2": "Oxygen",
        "3": "Nitrogen",
        "4": "Carbon Dioxide",
        "answer": "2"
    },
    "Which instrument is used to measure temperature?": {
        "1": "Thermometer",
        "2": "Barometer",
        "3": "Hygrometer",
        "4": "Telescope",
        "answer": "1"
    },
    "What force keeps us on the ground?": {
        "1": "Friction",
        "2": "Magnetism",
        "3": "Gravity",
        "4": "Electricity",
        "answer": "3"
    }
}

score = 0
print("\n🧪 Welcome to the General Science Quiz (10 Questions) 🧪\n")

for question, data in quiz.items():
    print(f"Q: {question}")
    print(f"  1. {data['1']}")
    print(f"  2. {data['2']}")
    print(f"  3. {data['3']}")
    print(f"  4. {data['4']}")

    user_input = input("Your answer (1-4): ").strip()

    if user_input == data["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        correct = data[data["answer"]]
        print(f"❌ Incorrect. The correct answer is: {correct}\n")

print("🎯 Quiz Completed!")
print(f"Your final score is: {score} out of {len(quiz)}\n")