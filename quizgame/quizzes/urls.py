from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name =  'quizzes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='quizzes/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='quizzes/logout.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile,  name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/password/', views.change_password, name="change_password"),
    path('<int:question_id>/', views.quiz, name='quiz'),
    path('<int:question_id>/check_answer/', views.check_answer, name='check_answer')
]
