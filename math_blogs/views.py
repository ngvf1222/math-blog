from django.shortcuts import render,get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from django.contrib.auth.models import User

def main(request):
    question_list = Question.objects.order_by('-point')
    if len(question_list)>=5:
        context = {'question_list': question_list[0:4]}
    else:
        context = {'question_list': question_list}
    return render(request, 'views_/main_views.html', context)
# Create your views here.
def views_writing(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'views_/views_writing.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user=='AnonymousUser':
        question.answer_set.create(ids='익명',content=request.POST.get('content'), create_date=timezone.now())
    else:
        question.answer_set.create(ids=request.user,content=request.POST.get('content'), create_date=timezone.now())
    return redirect('/../../views_writing/'+str(question_id)+'/')
def Plus_point(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.point+=1
    question.save()
    return redirect('/../../views_writing/'+str(question_id)+'/')
def Minus_point(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.point-=1
    question.save()
    return redirect('/../../views_writing/'+str(question_id)+'/')
def Search_writing(request, Search_value):
    Search_writing_list = Question.objects.filter(subject__contains=Search_value)
    context = {'Search_writing_list': Search_writing_list}
    return render(request, 'views_/Search_writing.html', context)
def new_question_from(request):
    return render(request, 'views_/new_question_from.html')
def new_question(request):
    if request.user=='AnonymousUser':
        q=Question(ids='익명', subject=request.POST.get('Title'), content=request.POST.get('text'), series=request.POST.get('classification'), point=0, create_date=timezone.now())
    else:
        q=Question(ids=request.user, subject=request.POST.get('Title'), content=request.POST.get('text'), series=request.POST.get('classification'), point=0, create_date=timezone.now())
    q.save()
    return redirect('/../../views_writing/'+str(q.id)+'/')
def user_addr_from(request):
    return render(request, 'views_/user_addr_from.html')
def user_addr(request):
    user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
    user.save()
    return redirect('/')
def Modify_question_from(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'views_/Modify_question_from.html', context)
def Modify_question(request, question_id):
    q=get_object_or_404(Question,pk=question_id)
    if q.ids==str(request.user):
        q.subject=request.POST.get('Title')
        q.content=request.POST.get('text')
        q.series=request.POST.get('classification')
        q.create_date=timezone.now()
    q.save()
    return redirect('/views_writing/'+str(q.id)+'/')
def Modify_answer_from(request, answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    context = {'answer': answer}
    return render(request, 'views_/Modify_answer_from.html', context)
def Modify_answer(request, answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    if answer.ids==str(request.user):
        answer.content=request.POST.get('text')
        answer.create_date=timezone.now()
        print(answer.content)
    answer.save()
    return redirect('/views_writing/'+str(answer.question.id)+'/')
def question_from(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    if question.ids==str(request.user):
        question.delete()
    return redirect('/')

def answer(request, answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    if answer.ids==str(request.user):
        answer.delete()
    return redirect('/views_writing/'+str(answer.question.id)+'/')
