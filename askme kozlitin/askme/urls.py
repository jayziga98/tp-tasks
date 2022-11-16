"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('<int:user_id>', views.index, name='index'),
    path('', views.index, name='index'),

    path('question/<int:user_id>/<int:question_id>', views.question, name='question'),
    path('question/<int:question_id>', views.question, name='question'),

    path('questions_by_tag/<int:tag_id>/<int:user_id>', views.questions_by_tag, name='questions_by_tag'),
    path('questions_by_tag/<int:tag_id>', views.questions_by_tag, name='questions_by_tag'),

    path('settings/<int:user_id>', views.settings, name='settings'),
    path('settings/', views.settings, name='settings'),

    path('register/<int:user_id>', views.register, name='register'),
    path('register/', views.register, name='register'),

    path('ask/<int:user_id>', views.ask, name='ask'),
    path('ask/', views.ask, name='ask'),

    path('login/<int:user_id>', views.login, name='login'),
    path('login/', views.login, name='login'),
]
