import datetime
import random
import time

# Define the get_user_info, store_conversation, and share_conversation functions
def get_user_info():
    # Placeholder function to get user information
    return {"name": "User", "age": 25}

def store_conversation(user_info, feeling, answers, suggestions):
    # Placeholder function to store the conversation
    pass

def share_conversation(user_info, feeling, answers, suggestions):
    # Placeholder function to share the conversation
    pass

def get_user_feeling():
    feelings = ["happy", "sad", "anxious", "stressed", "neutral", "grateful", "excited", "lonely", "angry", "frustrated", "hopeful", "calm", "overwhelmed", "peaceful", "curious", "bored", "guilty", "ashamed"]
    while True:
        feeling = input("So, how are you feeling today? You can use words like happy, sad, anxious, stressed, or anything else that describes your mood. 😊 ").lower()
        if feeling:
            if feeling in feelings:
                return feeling
            else:
                print("I understand you might be feeling something unique. Just let me know in your own words. 😊")
                return feeling  # Allow user to describe their feeling
        else:
            print("Please tell me how you're feeling. I'm here to listen. 🤗")

def ask_questions():
    questions = [
        "How much sleep have you been getting lately? 😴",
        "Have you been engaging in any physical activity? 🏃‍♀️",
        "How would you rate your social interactions this week? 💬",
        "Have you been taking time for yourself to relax and de-stress? 🧘‍♀️",
        "How would you rate your diet recently? 🍎",
        "Have you experienced any significant life events recently (positive or negative)? 🤔",
        "Are there any specific stressors you'd like to talk about? 😟",
        "Have you been having any thoughts that are troubling you? 💭",
    ]
    answers = {}
    for question in questions:
        print("Let me ask you a few more questions to understand better... 😊")
        time.sleep(1)
        while True:
            answer = input(f"{question} (Please be as descriptive as you like): ").lower()
            if answer:
                answers[question] = answer
                break
            else:
                print("No worries if it's hard to talk about. Just let me know when you're ready. 🙏")
    return answers

def suggest_self_care(feeling, answers):
    # Suggestion lists
    happy_suggestions = ["Keep doing what makes you happy!", "Share your joy with others."]
    sad_suggestions = ["Talk to a friend or family member.", "Engage in a hobby you enjoy."]
    anxious_suggestions = ["Practice deep breathing exercises.", "Try some mindfulness meditation."]
    stressed_suggestions = ["Take a break and relax.", "Go for a walk in nature."]
    neutral_suggestions = ["Try something new.", "Reflect on your day."]
    grateful_suggestions = ["Write down things you're grateful for.", "Express your gratitude to someone."]
    excited_suggestions = ["Channel your excitement into a project.", "Share your excitement with others."]
    lonely_suggestions = ["Reach out to a friend.", "Join a social group or activity."]
    angry_suggestions = ["Take deep breaths.", "Write down your thoughts."]
    frustrated_suggestions = ["Take a break.", "Talk to someone you trust."]
    hopeful_suggestions = ["Set some goals.", "Visualize your future."]
    calm_suggestions = ["Enjoy the moment.", "Practice mindfulness."]
    overwhelmed_suggestions = ["Break tasks into smaller steps.", "Ask for help if needed."]
    peaceful_suggestions = ["Enjoy the tranquility.", "Share your peace with others."]
    curious_suggestions = ["Explore new topics.", "Ask questions and seek answers."]
    bored_suggestions = ["Try a new hobby.", "Read a book or watch a documentary."]
    guilty_suggestions = ["Forgive yourself.", "Make amends if possible."]
    ashamed_suggestions = ["Talk to someone you trust.", "Reflect on the situation."]
    other_suggestions = ["Take care of yourself.", "Do something you enjoy."]

    feeling = feeling.lower()
    personalized_suggestions = []

    if any(keyword in feeling for keyword in ["happy", "good", "joyful", "excited", "great"]):
        base_suggestions = happy_suggestions
    elif any(keyword in feeling for keyword in ["sad", "down", "upset", "unhappy", "miserable"]):
        base_suggestions = sad_suggestions
    elif any(keyword in feeling for keyword in ["anxious", "worried", "nervous", "fearful", "apprehensive"]):
        base_suggestions = anxious_suggestions
    elif any(keyword in feeling for keyword in ["stressed", "overwhelmed", "tired", "exhausted", "frustrated"]):
        base_suggestions = stressed_suggestions
    elif any(keyword in feeling for keyword in ["neutral", "okay", "fine", "indifferent", "so-so"]):
        base_suggestions = neutral_suggestions
    elif any(keyword in feeling for keyword in ["grateful", "thankful", "appreciative"]):
        base_suggestions = grateful_suggestions
    elif any(keyword in feeling for keyword in ["excited", "thrilled", "enthusiastic"]):
        base_suggestions = excited_suggestions
    elif any(keyword in feeling for keyword in ["lonely", "isolated", "alone"]):
        base_suggestions = lonely_suggestions
    elif any(keyword in feeling for keyword in ["angry", "furious", "irate"]):
        base_suggestions = angry_suggestions
    elif any(keyword in feeling for keyword in ["frustrated", "annoyed", "irritated"]):
        base_suggestions = frustrated_suggestions
    elif any(keyword in feeling for keyword in ["hopeful", "optimistic", "positive"]):
        base_suggestions = hopeful_suggestions
    elif any(keyword in feeling for keyword in ["calm", "relaxed", "serene"]):
        base_suggestions = calm_suggestions
    elif any(keyword in feeling for keyword in ["overwhelmed", "burdened", "stressed out"]):
        base_suggestions = overwhelmed_suggestions
    elif any(keyword in feeling for keyword in ["peaceful", "tranquil", "content"]):
        base_suggestions = peaceful_suggestions
    elif any(keyword in feeling for keyword in ["curious", "inquisitive", "intrigued"]):
        base_suggestions = curious_suggestions
    elif any(keyword in feeling for keyword in ["bored", "uninterested", "apathetic"]):
        base_suggestions = bored_suggestions
    elif any(keyword in feeling for keyword in ["guilty", "remorseful", "contrite"]):
        base_suggestions = guilty_suggestions
    elif any(keyword in feeling for keyword in ["ashamed", "embarrassed", "humiliated"]):
        base_suggestions = ashamed_suggestions
    else:
        base_suggestions = other_suggestions

    personalized_suggestions.extend(base_suggestions)

    # Personalization logic based on answers
    for question, answer in answers.items():
        if "sleep" in question and "bad" in answer:
            personalized_suggestions.append("Try to establish a regular sleep schedule.")
        if "physical activity" in question and "no" in answer:
            personalized_suggestions.append("Consider incorporating some physical activity into your routine.")
        if "social interactions" in question and "low" in answer:
            personalized_suggestions.append("Reach out to friends or family for a chat.")
        if "relax" in question and "no" in answer:
            personalized_suggestions.append("Take some time to relax and unwind.")
        if "diet" in question and "poor" in answer:
            personalized_suggestions.append("Try to eat a balanced diet.")
        if "life events" in question and "yes" in answer:
            personalized_suggestions.append("It's important to process significant life events. Consider talking to someone about it.")
        if "stressors" in question and "yes" in answer:
            personalized_suggestions.append("Identify your stressors and try to address them one by one.")
        if "thoughts" in question and "yes" in answer:
            personalized_suggestions.append("Consider talking to a mental health professional about your thoughts.")

    return personalized_suggestions

# Main function
def main():
    user_info = get_user_info()
    feeling = get_user_feeling()
    answers = ask_questions()
    suggestions = suggest_self_care(feeling, answers)
    store_conversation(user_info, feeling, answers, suggestions)
    share_conversation(user_info, feeling, answers, suggestions)
    print("Here are some personalized self-care suggestions for you:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

if __name__ == "__main__":
    main()