from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a home page or any other page
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'register/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })
        if form.is_valid():
            user = form.save()
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
        else:
            return render(request, 'register/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})

def home(request):
    return render(request,'home.html')

def dash(request):
    return render(request,'dashboard.html')

def questionaire_page(request):
    return render(request,'questionaire.html')

def results(request):
        # Assuming you're retrieving mood from query parameters
        mood = request.GET.get('mood', 'neutral')
        print(mood)
        if mood == 'good':
            context = {
                'title': 'Happy!',
                'image_src': 'mood/happy.jpg',
                'message': 'You are doing well! Keep up the positive outlook.',
                'background_image': 'good_mood_background.jpeg'
            }
        elif mood == 'bad':
            context = {
                'title': 'You gotta improve :)',
                'image_src': 'mood/sad.jpg',
                'message': 'Feeling down? It\'s okay. Take some time for self-care.',
                'background_image': 'bad_mood_background.jpeg'
            }
        else:
            context = {
                'title': 'On Balance',
                'image_src': 'mood/smily.png',
                'message': 'Your mood is average. Reflect on what could improve.',
                'background_image': 'neutral_mood_background.jpeg'
            }
        return render(request, 'result.html', context)

def ques(request):
    return render(request,'ques.html')

from django.shortcuts import render
from django.http import JsonResponse

def mood_evaluation(request):
    if request.method == 'POST':
        total_score = 0
        for index, question_text in enumerate(QUESTIONS):
            selected_option = request.POST.get(f'question_{index}', '')  # Assuming form field names are 'question_0', 'question_1', etc.
            MoodEvaluation.objects.create(user=request.user, question=question_text, selected_option=selected_option)
            # Calculate score if needed based on selected_option and update total_score

        # Classify mood based on total_score
        if total_score >= 10:
            mood_category = "Good"
        elif total_score >= 0:
            mood_category = "Average"
        else:
            mood_category = "Bad"

        return render(request, 'mood_evaluation_result.html', {'mood_category': mood_category})

    return render(request, 'mood_evaluation.html', {'questions': enumerate(QUESTIONS), 'options': OPTIONS})

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
        {"text": "A person laughing with friends", "image": "laughing.png"},
        {"text": "A person calmly meditating", "image": "meditating.png"},
        {"text": "A person looking worried with furrowed brow", "image": "worried.png"},
        {"text": "A person with a blank expression", "image": "blank.png"}
    ],
    [
        {"text": "A person looking well-rested and smiling getting out of bed", "image": "well-rested.png"},
        {"text": "A person tossing and turning in bed at night", "image": "tossing.png"},
        {"text": "A person hitting the snooze button on their alarm clock", "image": "snooze.png"},
        {"text": "A person yawning during the day", "image": "yawning.png"}
    ],
    [
        {"text": "A person running energetically outdoors", "image": "running.png"},
        {"text": "A person walking briskly with a determined look", "image": "brisk-walk.png"},
        {"text": "A person slowly dragging themselves through the day", "image": "dragging.png"},
        {"text": "A person slumped on a couch feeling drained", "image": "slumped.png"}
    ],
    [
        {"text": "A group of friends laughing and having fun together", "image": "friends-laughing.png"},
        {"text": "A person enjoying a quiet coffee date with one friend", "image": "coffee-date.png"},
        {"text": "A person scrolling through social media alone", "image": "scrolling.png"},
        {"text": "An empty park bench", "image": "empty-bench.png"}
    ],
    [
        {"text": "A person taking deep breaths and focusing on their meditation", "image": "deep-breaths.png"},
        {"text": "A person listening to calming music with headphones on", "image": "calming-music.png"},
        {"text": "A person yelling into a pillow", "image": "yelling.png"},
        {"text": "A person clenching their fists in frustration", "image": "clenching-fists.png"}
    ],
    [
        {"text": "A person looking at a vision board with a determined expression", "image": "vision-board.png"},
        {"text": "A person climbing a mountain with a sense of accomplishment", "image": "climbing-mountain.png"},
        {"text": "A person looking lost and unsure in a forest", "image": "lost-in-forest.png"},
        {"text": "A person crumpling up a piece of paper with frustration", "image": "crumpling-paper.png"}
    ],
    [
        {"text": "A person enjoying a healthy and balanced meal", "image": "healthy-meal.png"},
        {"text": "A person skipping a meal and feeling hungry", "image": "skipping-meal.png"},
        {"text": "A person mindlessly snacking", "image": "snacking.png"},
        {"text": "A person looking at food with a lack of interest", "image": "lack-interest-food.png"}
    ],
    [
        {"text": "A person smiling and confidently looking in the mirror", "image": "confident-mirror.png"},
        {"text": "A person exercising and taking care of their physical health", "image": "exercising.png"},
        {"text": "A person hiding their body under baggy clothes", "image": "baggy-clothes.png"},
        {"text": "A person on a scale looking down with disappointment", "image": "disappointed-scale.png"}
    ],
    [
        {"text": "A beautiful sunrise with a hopeful message", "image": "sunrise.png"},
        {"text": "A path leading up a hilltop with a bright future ahead", "image": "bright-future.png"},
        {"text": "A dark and stormy sky", "image": "stormy-sky.png"},
        {"text": "A dead end with nowhere to go", "image": "dead-end.png"}
    ],
    [
        {"text": "A person talking to a therapist and feeling listened to", "image": "talking-therapist.png"},
        {"text": "A person holding hands with a supportive friend", "image": "supportive-friend.png"},
        {"text": "A person sitting alone with a question mark above their head", "image": "question-mark.png"},
        {"text": "A phone with a helpline number displayed on the screen", "image": "helpline.png"}
    ]
]
