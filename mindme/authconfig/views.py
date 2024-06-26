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
    context = {
        'title': 'On Balance',
        'image_src': 'mood/smily.png',
        'message': 'Doing well, but consider exploring support resources.',
        'background_image': 'res_bck.jpeg'
    }
    return render(request,'result.html', context)

from django.shortcuts import render, redirect
from .forms import ResponseForm
from .data import QUESTIONS, OPTIONS

def question_view(request, question_id):
    question_id = int(question_id)
    question = QUESTIONS[question_id]
    options = OPTIONS[question_id]
    
    if request.method == 'POST':
        form = ResponseForm(request.POST, options=options)
        if form.is_valid():
            if 'choices' not in request.session:
                request.session['choices'] = []
            request.session['choices'].append(form.cleaned_data['selected_choice'])
            next_question_id = question_id + 1
            if next_question_id < len(QUESTIONS):
                return redirect('question', question_id=next_question_id)
            else:
                return redirect('submit_responses')
    else:
        form = ResponseForm(options=options)
    return render(request, 'question.html', {'form': form, 'question': question, 'options': options})

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
        "A phone with a helpline number displayed on the screen": 1,
    }

    total_score = sum(scores[choice] for choice in choices)

    if total_score >= 10:
        return "Good"
    elif total_score >= 0:
        return "Average"
    else:
        return "Bad"

def submit_responses(request):
    choices = request.session.get('choices', [])
    mood = evaluate_mood(choices)
    request.session.pop('choices', None)  # Clear the session data after evaluation
    return render(request, 'submit.html', {'mood': mood})