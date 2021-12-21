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
    return render(request, 'v/m_v.html', context)
# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'v/r_v.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user=='AnonymousUser':
        question.answer_set.create(ids='익명',content=request.POST.get('content'), create_date=timezone.now())
    else:
        question.answer_set.create(ids=request.user,content=request.POST.get('content'), create_date=timezone.now())
    return redirect('/../../v/'+str(question_id)+'/')
def pp(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.point+=1
    question.save()
    return redirect('/../../v/'+str(question_id)+'/')
def mp(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.point-=1
    question.save()
    return redirect('/../../v/'+str(question_id)+'/')
def q(request, sodyd):
    qs = Question.objects.filter(subject__contains=sodyd)
    context = {'qs': qs}
    return render(request, 'v/q_v.html', context)
def nqf(request):
    return render(request, 'v/nqf.html')
def nq(request):
    if request.user=='AnonymousUser':
        q=Question(ids='익명', subject=request.POST.get('s'), content=request.POST.get('c'), series=request.POST.get('sc'), point=0, create_date=timezone.now())
    else:
        q=Question(ids=request.user, subject=request.POST.get('s'), content=request.POST.get('c'), series=request.POST.get('sc'), point=0, create_date=timezone.now())
    q.save()
    return redirect('/../../v/'+str(q.id)+'/')
def gs(request):
    return render(request, 'v/gsf.html')
def gss(request):
    user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
    user.save()
    return redirect('/')
def dq(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'v/dq.html', context)
def dqs(request, question_id):
    q=get_object_or_404(Question,pk=question_id)
    if q.ids==str(request.user):
        q.subject=request.POST.get('s')
        q.content=request.POST.get('c')
        q.series=request.POST.get('sc')
        q.create_date=timezone.now()
    q.save()
    return redirect('/v/'+str(q.id)+'/')
def da(request, a_id):
    a = get_object_or_404(Answer,pk=a_id)
    context = {'a': a}
    return render(request, 'v/da.html', context)
def das(request, a_id):
    ass=get_object_or_404(Answer,pk=a_id)
    print(ass)
    if ass.ids==str(request.user):
        ass.content=request.POST.get('c')
        ass.create_date=timezone.now()
        print(ass.content)
    ass.save()
    return redirect('/v/'+str(ass.question.id)+'/')
def ddq(request, question_id):
    q=get_object_or_404(Question,pk=question_id)
    if q.ids==str(request.user):
        q.delete()
    return redirect('/')

def dda(request, a_id):
    a=get_object_or_404(Answer,pk=a_id)
    if a.ids==str(request.user):
        a.delete()
    return redirect('/v/'+str(a.question.id)+'/')
