def evaluate_mood(choices):
    scores = {
        "A person laughing with friends": 2,
        "A person calmly meditating": 2,
        "A person looking worried with furrowed brow": -1,
        "A person with a blank expression": 0,
        "A person looking well-rested and smiling getting out of bed": 2,
        "A person tossing and turning in bed at night": -1,
        "A person hitting the snooze button on their alarm clock": 0,
        "A person yawning during the day": -1,
        "A person running energetically outdoors": 2,
        "A person walking briskly with a determined look": 1,
        "A person slowly dragging themselves through the day": -1,
        "A person slumped on a couch feeling drained": -2,
        "A group of friends laughing and having fun together": 2,
        "A person enjoying a quiet coffee date with one friend": 1,
        "A person scrolling through social media alone": 0,
        "An empty park bench": -1,
        "A person taking deep breaths and focusing on their meditation": 2,
        "A person listening to calming music with headphones on": 1,
        "A person yelling into a pillow": -1,
        "A person clenching their fists in frustration": -2,
        "A person looking at a vision board with a determined expression": 2,
        "A person climbing a mountain with a sense of accomplishment": 2,
        "A person looking lost and unsure in a forest": -1,
        "A person crumpling up a piece of paper with frustration": -2,
        "A person enjoying a healthy and balanced meal": 2,
        "A person skipping a meal and feeling hungry": -1,
        "A person mindlessly snacking": 0,
        "A person looking at food with a lack of interest": -2,
        "A person smiling and confidently looking in the mirror": 2,
        "A person exercising and taking care of their physical health": 1,
        "A person hiding their body under baggy clothes": -1,
        "A person on a scale looking down with disappointment": -2,
        "A beautiful sunrise with a hopeful message": 2,
        "A path leading up a hilltop with a bright future ahead": 1,
        "A dark and stormy sky": -2,
        "A dead end with nowhere to go": -2,
        "A person talking to a therapist and feeling listened to": 2,
        "A person holding hands with a supportive friend": 1,
        "A person sitting alone with a question mark above their head": 0,
        "A phone with a helpline number displayed on the screen": 1
    }

    total_score = sum(scores[choice] for choice in choices)

    if total_score >= 10:
        return "Good"
    elif total_score >= 0:
        return "Average"
    else:
        return "Bad"

def ask_questions():
    questions = [
        "What is your current mood?",
        "How are you feeling about your sleep lately?",
        "How would you describe your energy level?",
        "What is your current social life like?",
        "How are you coping with stress lately?",
        "How do you feel about your current goals and aspirations?",
        "How would you describe your current appetite?",
        "How are you feeling about your body image?",
        "How would you describe your overall outlook on life?",
        "Do you feel comfortable reaching out for help if you need it?"
    ]

    options = [
        [
            "A person laughing with friends",
            "A person calmly meditating",
            "A person looking worried with furrowed brow",
            "A person with a blank expression"
        ],
        [
            "A person looking well-rested and smiling getting out of bed",
            "A person tossing and turning in bed at night",
            "A person hitting the snooze button on their alarm clock",
            "A person yawning during the day"
        ],
        [
            "A person running energetically outdoors",
            "A person walking briskly with a determined look",
            "A person slowly dragging themselves through the day",
            "A person slumped on a couch feeling drained"
        ],
        [
            "A group of friends laughing and having fun together",
            "A person enjoying a quiet coffee date with one friend",
            "A person scrolling through social media alone",
            "An empty park bench"
        ],
        [
            "A person taking deep breaths and focusing on their meditation",
            "A person listening to calming music with headphones on",
            "A person yelling into a pillow",
            "A person clenching their fists in frustration"
        ],
        [
            "A person looking at a vision board with a determined expression",
            "A person climbing a mountain with a sense of accomplishment",
            "A person looking lost and unsure in a forest",
            "A person crumpling up a piece of paper with frustration"
        ],
        [
            "A person enjoying a healthy and balanced meal",
            "A person skipping a meal and feeling hungry",
            "A person mindlessly snacking",
            "A person looking at food with a lack of interest"
        ],
        [
            "A person smiling and confidently looking in the mirror",
            "A person exercising and taking care of their physical health",
            "A person hiding their body under baggy clothes",
            "A person on a scale looking down with disappointment"
        ],
        [
            "A beautiful sunrise with a hopeful message",
            "A path leading up a hilltop with a bright future ahead",
            "A dark and stormy sky",
            "A dead end with nowhere to go"
        ],
        [
            "A person talking to a therapist and feeling listened to",
            "A person holding hands with a supportive friend",
            "A person sitting alone with a question mark above their head",
            "A phone with a helpline number displayed on the screen"
        ]
    ]

    choices = []

    for i, question in enumerate(questions):
        print(question)
        for j, option in enumerate(options[i]):
            print(f"{j+1}. {option}")
        choice = int(input("Choose an option (1-4): ")) - 1
        choices.append(options[i][choice])

    return choices

if __name__ == "__main__":
    choices = ask_questions()
    mood = evaluate_mood(choices)
    print(f"Your general mood is: {mood}")
