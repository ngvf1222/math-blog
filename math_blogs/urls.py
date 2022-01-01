from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main),
    path('views_writing/<int:question_id>/', views.views_writing),
    path('answer/create/<int:question_id>/', views.answer_create),
    path('Plus_point/<int:question_id>/', views.Plus_point),
    path('Minus_point/<int:question_id>/', views.Minus_point),
    path('Search_writing/<Search_value>', views.Search_writing),
    path('new_question_from', views.new_question_from),
    path('new_question', views.new_question),
    path('login/', auth_views.LoginView.as_view(template_name='v/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('user_addr_from', views.user_addr_from),
    path('user_addr', views.user_addr),
    path('Modify_question_from/<int:question_id>/', views.Modify_question_from),
    path('Modify_question/<int:question_id>/', views.Modify_question),
    path('Modify_answer_from/<int:answer_id>/', views.Modify_answer_from),
    path('Modify_answer/<int:answer_id>/', views.Modify_answer),
    path('delete_question/<int:question_id>/',views.question_from),
    path('delete_answer/<int:answer_id>/', views.answer)
]