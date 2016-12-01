from django.conf.urls import url
from ratifyApp import views
"""ratify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questions', views.questions, name="questions"),
    url(r'^answer_page/(?P<question_id>[0-9]+)', views.answer, name="answer"),
    url(r'^vote', views.vote, name="vote"),
    url(r'^add_answer', views.add_answer, name="add_answer"),
    url(r'^add_question', views.add_question, name="add_question"),
]
