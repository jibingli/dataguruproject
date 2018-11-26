from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Question, Choice, User
import json


# Create your views here.

# 展示所有问题
# def index(request):
#     question_list=Question.objects.all()
#     return render(request,'index.html',{'q':question_list})

def index(request):
    question_list = Question.objects.all()
    datas = {}
    re = {}
    if question_list:
        for q in question_list:
            datas[q.id] = q.question_text
        re['status'] = '200'
        re['message'] = 'success'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)
    else:
        re['status'] = '10021'
        re['message'] = 'null'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)


# 显示某个问题下的选项

# def detail(request,question_id):
#     q = get_object_or_404(Question,pk=question_id)
#     return render(request, 'detail.html', {'question': q})

def detail(request, question_id):
    choices = Choice.objects.filter(question_id=question_id)
    datas = {}
    re = {}
    if choices:
        for q in choices:
            datas[q.id] = q.choice_text
        re['status'] = '200'
        re['message'] = 'success'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)
    else:
        re['status'] = '10021'
        re['message'] = 'null'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)


# 投票
# def vote(request,question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     choiceid=request.POST.get("choice")
#     selectchoice=q.choice_set.get(pk=choiceid)
#     print(selectchoice)
#     selectchoice.votes+=1
#     selectchoice.save()
#     return render(request, 'result.html', {'question': q})

def vote(request, question_id):
    try:
        q = get_object_or_404(Question, pk=question_id)
        choiceid = request.POST.get("choice")
        selectchoice = q.choice_set.get(pk=choiceid)
        selectchoice.votes += 1
        selectchoice.save()

        choices = Choice.objects.filter(question_id=question_id)
        datas = {}
        re = {}
        for choice in choices:
            datas[choice.choice_text] = choice.votes
        re['status'] = '200'
        re['message'] = 'success'
        re['data'] = datas
        return HttpResponse(json.dumps(re))
    except Exception:
        re = {}
        re['status'] = '10021'
        re['message'] = 'fail'
        re['data'] = None
        return HttpResponse(json.dumps(re))


# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not (username and password):
            return HttpResponse(json.dumps({"status": 10023, 'message': '参数错误'}))
        user = User.objects.filter(username=username, password=password)
        resp = {}
        if user:
            resp['status'] = 200
            resp['message'] = '登录成功'
            return HttpResponse(json.dumps(resp))
        else:
            resp['status'] = 10021
            resp['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(resp))
    else:
        return HttpResponse(json.dumps({"status": 10022, 'message': 'error method'}))
