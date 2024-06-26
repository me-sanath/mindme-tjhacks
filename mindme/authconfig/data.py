# data.py
QUESTIONS = [
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

OPTIONS = [
    [
        {"text": "A person laughing with friends", "image": "asthetic1.png", "score": 2},
        {"text": "A person calmly meditating", "image": "asthetic2.png", "score": 2},
        {"text": "A person looking worried with furrowed brow", "image": "asthetic3.png", "score": -1},
        {"text": "A person with a blank expression", "image": "asthetic4.png", "score": 0},
    ],
    [
        {"text": "A person looking well-rested and smiling getting out of bed", "image": "asthetic1.png", "score": 2},
        {"text": "A person tossing and turning in bed at night", "image": "asthetic2.png", "score": -1},
        {"text": "A person hitting the snooze button on their alarm clock", "image": "asthetic3.png", "score": 0},
        {"text": "A person yawning during the day", "image": "asthetic4.png", "score": -1},
    ],
    # Add the rest of the questions and options similarly
]
