from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 0~5까지 불러오는데 pub_date 이면 만든지 오래된거부터 -pub_date 이면 최근거 부터!
    print("A")
    print(latest_question_list)
    # Question은 결국 QuerySet을 반환한다!
    print("B")  # pipenv shell에서 콘솔 확인가능!
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', {'latest_question_list__': latest_question_list})
    # context를 넣어도 되고 직접 넣어도됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # latest_question_list__ 을 index.html로 보내줌!

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# /polls/1또는 2를 받고 url에서 주소타고 view.detail이 실행되면!
# 1또는 2가 아이디로 question_id적용되서 들어간다!
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # model의 Question을 가서 pk를이용해 row를 가져온다!
    # get_object_or_404 이미정의된 함수이다! import했음..
    # 값이 있으면 가져오고 없으면 404에러를 일으킨다!
    print(question)
    return render(request, 'polls/detail.html', {'question': question})
    # 여기서 다시 탬플릿 파일안에 polls 속의 detail.html을 실행할것임!


def vote2233(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # detail의 choice의 value 값이 post에 들어감
        # post를 request해서 choice된값을 pk에 넣겠음!
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pollss:results', args=(question.id,)))
        # reverse는 args 형식으로 넘겨줘야한다!
        # reverse는 appname : urls'name으로 화면을 열고
        # render은 바로 html형식을 연다!
        # 왜 <int:question_id>/vote/는 안나오냐면 reverse로 바로 주소값을 result로 준다!


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
