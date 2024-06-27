from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('',views.home,name='home'),
    path('dashboard/',views.dash,name='dashboard'),
    path('question/',views.questionaire_page,name="questionnaire_view"),
    path('result/',views.results,name='result'),
    
]
