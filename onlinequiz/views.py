from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request , 'Home.html', context)

def api_question(request, id):
    raw_questions = Question.objects.filter(course = id)[:10]
    questions =[]

    for raw_question in raw_questions:
        question = {}
        question['id'] = raw_question.id
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer

        options = []

        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        options.append(raw_question.option_three)
        options.append(raw_question.option_four)

        question['options'] = options

        questions.append(question)

    return JsonResponse(questions , safe= False)

def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score' : score}
    return render(request , 'score.html' , context)

def take_quiz(request, id):
    context = {'id' : id}
    return render(request , 'quiz.html' , context)

@csrf_exempt
def check_score(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({'message' : 'success' , 'status' : True})

    
