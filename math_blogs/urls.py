from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main),
    path('v/<int:question_id>/', views.detail),
    path('answer/create/<int:question_id>/', views.answer_create),
    path('pp/<int:question_id>/', views.pp),
    path('mp/<int:question_id>/', views.mp),
    path('q/<sodyd>', views.q),
    path('nqf', views.nqf),
    path('nq', views.nq),
    path('login/', auth_views.LoginView.as_view(template_name='v/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('ghldnjs', views.gs),
    path('ghldnjss', views.gss),
    path('dq/<int:question_id>/', views.dq),
    path('dqs/<int:question_id>/', views.dqs),
    path('da/<int:a_id>/', views.da),
    path('das/<int:a_id>/', views.das),
    path('ddq/<int:question_id>/',views.ddq),
    path('dda/<int:a_id>/', views.dda)
]