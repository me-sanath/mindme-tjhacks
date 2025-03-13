from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    path('dashboard/', views.dash, name='dashboard'),
    path('question/', views.questionaire_page, name="questionnaire_view"),
    path('result/', views.results, name='result'),
    path('ques/', views.ques_view, name='ques'),
    path('about/', views.about, name='about'),  # Add this line for the About Us page
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
