from django.urls import path
from . import views

app_name = 'pollss'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    # index.html에서 /polls/1또는 2를 받고오면! view파일에 있는detail 함수실행!
    path('<int:question_id>/', views.detail, name='detail'),


    # question.id arg로 받지만 주소에서는 . 대신 _ 를 사용하여 이어준다!
    # ex: /polls/5/results/
    path('<int:question_id>/resultshaha/', views.results, name='results'),

    # detail.html에서 여기로 오게 된다! 즉 view.vote를 보자!
    # 왜 <int:question_id>/vote/는 안나오냐면 vote에서
    # reverse로 바로 주소값을 result로 준다!
    # 주소창에 실험해본다고 polls/2/vote해도 안됨 어짜피.. 왜냐하면 post방식이라
    # url로 choice값이 들어오지 않음.. 그래서 null이라 오류남!
    # ex: /polls/5/vote/
    path('<int:question_id>/vote22aaa/', views.vote2233, name='vote2277'),
]  # 패스뒤에 붙는건 vote22aaa // resultshaha 내맘임.. 결과에 영향 안미침
# 중요한건 탬플릿이나 뷰에서 app_name:name 과 views안에있는 함수이름임!!
