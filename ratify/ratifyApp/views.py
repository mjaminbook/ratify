from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def questions(request):
	return HttpResponse("Question Page")

def vote(request, question_id):
	return HttpResponse("Vote page for question #%s" %question_id)