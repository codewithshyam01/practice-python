import random
import time

# 🧑‍🤝‍🧑 User Profiles (Multiple User Interaction)
user_profiles = {}

def greet_user():
    print("Welcome to the ultimate user interaction script!")
    print("This will ask you many questions, get to know you, and offer personalized responses.")
    
    name = input("What's your name? ")
    if name not in user_profiles:
        print(f"Hello {name}! Let's get started.")
        age = int(input(f"How old are you, {name}? "))
        favorite_color = input(f"What's your favorite color, {name}? ").lower()
        hobby = input(f"What's your favorite hobby, {name}? ")
        city = input(f"Where do you live, {name}? ")
        user_profiles[name] = {'age': age, 'favorite_color': favorite_color, 'hobby': hobby, 'city': city}
    else:
        print(f"Welcome back, {name}! I remember you!")
    
    print(f"\nNice to meet you, {name}! Here's your profile: ")
    for key, value in user_profiles[name].items():
        print(f"{key.capitalize()}: {value}")

# 🧑‍🎨 Avatar Creation
def avatar_creation():
    print("\nLet's create your custom avatar!")
    avatar_name = input("What will your avatar’s name be? ")
    avatar_gender = input("What gender would you like your avatar to be? (Male/Female/Other) ").lower()
    avatar_hair_color = input("Choose a hair color for your avatar: ").lower()
    avatar_eye_color = input("Choose an eye color for your avatar: ").lower()
    avatar_style = input("What style does your avatar prefer? (Casual, Sporty, Elegant, etc.) ").lower()

    print(f"\nAvatar Created: {avatar_name}")
    print(f"Gender: {avatar_gender.capitalize()}")
    print(f"Hair Color: {avatar_hair_color.capitalize()}")
    print(f"Eye Color: {avatar_eye_color.capitalize()}")
    print(f"Style: {avatar_style.capitalize()}")

# 🎮 AI-Powered Trivia Game
def trivia_game():
    print("\nWelcome to the trivia game!")
    category = input("Choose a category: (e.g., History, Science, Movies): ").lower()
    level = input("Choose difficulty: (easy, medium, hard): ").lower()

    questions = {
        "history": {
            "easy": [("Who was the first president of the USA?", "George Washington")],
            "medium": [("What year did World War II end?", "1945")],
            "hard": [("Who was the first emperor of China?", "Qin Shi Huang")]
        },
        "science": {
            "easy": [("What is the chemical symbol for water?", "H2O")],
            "medium": [("What is the powerhouse of the cell?", "Mitochondria")],
            "hard": [("What is the most abundant gas in Earth's atmosphere?", "Nitrogen")]
        }
    }

    print(f"\nStarting {category} trivia at {level} difficulty!")
    selected_questions = questions.get(category, {}).get(level, [])
    score = 0
    for question, answer in selected_questions:
        user_answer = input(f"Question: {question} ").lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"\nYour score: {score}/{len(selected_questions)}")

# 🏋️‍♂️ Fitness Challenge
def fitness_challenge():
    print("\nReady for a fitness challenge?")
    activity = input("What type of exercise do you prefer? (e.g., Cardio, Strength, Yoga): ").lower()
    time_available = int(input("How much time do you have? (in minutes): "))

    if activity == "cardio":
        if time_available >= 30:
            print(f"\nGreat! Do a 30-minute jog or cycling session.")
        else:
            print(f"\nHow about a quick 15-minute high-intensity interval training (HIIT) session?")
    elif activity == "strength":
        print(f"\nFocus on bodyweight exercises like squats, push-ups, and planks.")
    elif activity == "yoga":
        print(f"\nA 15-minute yoga flow could be a perfect way to de-stress.")
    else:
        print(f"\nThat sounds like a good choice! Keep moving and stay healthy!")

# 🌌 Time Travel Adventure
def time_travel():
    print("\nTime travel adventure!")
    era = input("Which time period would you like to visit? (e.g., Medieval, Future, Ancient Egypt): ").lower()
    if era == "medieval":
        print("You step into the Medieval Era and see knights, castles, and dragons! What do you do next?")
    elif era == "future":
        print("You find yourself in the year 2200, surrounded by flying cars and robots! Where do you go?")
    elif era == "ancient egypt":
        print("You’re in Ancient Egypt, walking among the pyramids and pharaohs! What secrets will you uncover?")
    else:
        print("Time travel to this era is not available. Choose another one!")

# 🎤 Dream Interpretation
def dream_interpretation():
    print("\nLet’s interpret your dream!")
    dream = input("Describe your dream: ")
    print("\nHere’s an interpretation based on dream symbols:")
    if "flying" in dream:
        print("Flying often symbolizes freedom or escape from reality.")
    elif "falling" in dream:
        print("Falling can indicate feelings of insecurity or loss of control.")
    else:
        print("Every dream is unique. This one seems to be full of mystery and potential!")

# 📝 Personal Journal & Mood Tracker
def journal_entry():
    print("\nLet’s write a journal entry!")
    mood = input("How are you feeling today? (e.g., Happy, Sad, Excited): ").lower()
    entry = input(f"Write your journal entry for today ({mood}): ")
    
    print(f"\nYour entry has been saved. Here’s your reflection:")
    print(f"Mood: {mood.capitalize()}")
    print(f"Journal Entry: {entry}")

# 🎶 Mood-Based Music Playlist
def mood_music():
    print("\nLet’s pick the perfect music for your mood!")
    mood = input("How are you feeling today? (e.g., Happy, Relaxed, Energetic, Sad): ").lower()
    
    playlists = {
        "happy": ["Pharrell Williams - Happy", "Katy Perry - Firework", "Justin Timberlake - Can't Stop the Feeling"],
        "relaxed": ["John Mayer - Gravity", "Norah Jones - Don't Know Why", "Coldplay - Fix You"],
        "energetic": ["Avicii - Wake Me Up", "Sia - Chandelier", "Imagine Dragons - Radioactive"],
        "sad": ["Adele - Someone Like You", "Sam Smith - Stay With Me", "Bill Withers - Lean on Me"]
    }

    selected_playlist = playlists.get(mood, ["Sorry, I don't have a playlist for that mood."])
    print(f"\nHere are some songs for your {mood} mood:")
    for song in selected_playlist:
        print(f"- {song}")

# 📜 Main Menu: Ask User for Choices
def ask_for_choices():
    print("\nWhat would you like to explore next?")
    print("1. Create Custom Avatar")
    print("2. Time Travel Adventure")
    print("3. AI-Powered Trivia Game")
    print("4. Fitness Challenge")
    print("5. Dream Interpretation")
    print("6. Personal Journal & Mood Tracker")
    print("7. Mood-Based Music Playlist")
    print("8. Exit")
    
    try:
        choice = int(input("Enter the number of your choice: "))
        return choice
    except ValueError:
        print("Invalid choice. Please select a number between 1 and 8.")
        return None

# 🌟 Main Function to Drive Interaction
def main():
    print("Welcome to our interactive world!")
    name = input("Please tell me your name: ")

    if name in user_profiles:
        print(f"\nWelcome back, {name}! Let's pick up where we left off.")
    else:
        greet_user()

    while True:
        choice = ask_for_choices()

        if choice == 1:
            avatar_creation()
        elif choice == 2:
            time_travel()
        elif choice == 3:
            trivia_game()
        elif choice == 4:
            fitness_challenge()
        elif choice == 5:
            dream_interpretation()
        elif choice == 6:
            journal_entry()
        elif choice == 7:
            mood_music()
        elif choice == 8:
            print("Goodbye! Have a wonderful day ahead!")
            break
        else:
            print("Invalid option. Please select from the menu.")

if __name__ == "__main__":
    main()
