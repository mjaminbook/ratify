from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Answer, Question

# Create your views here.
def questions(request):
	questionList = []
	questions = Question.objects.all()
	for question in questions:
		total_votes = 0
		answers = Answer.objects.filter(question=question)
		for answer in answers:
			total_votes += answer.num_votes
		question_context = {"text" : question.question_text, "num_votes" : total_votes, "id" : question.pk}
		questionList.append(question_context)
	context = {"questions" : questionList}
	return render(request, "question_page.html", context)

def answer(request, question_id):
	question = Question.objects.get(pk=question_id)
	answers = Answer.objects.filter(question_id=question_id)
	context = {"question_text" : question.question_text, "answers" : answers}
	return render(request,"answer_page.html", context)

#The next three functions all expect POST requests
def vote(request):
	answerId = request.POST.get("answer_id")
	answer = Answer.objects.get(pk=answer_id)
	answer.num_votes += 1
	answer.save(update_fields=["num_votes"])
	response = {"status" : 200, "answer_id" : answerId, "total_votes" : answer.num_votes}
	return HttpResponse(json.dumps(response), content_type="application/json")

def add_answer(request):
	questionId = request.POST.get("question_id")
	answerText = request.POST.get("answer_text")
	question = Question.objects.get(pk=questionId)
	newAnswer = Answer(question, answerText, 1) #Should we assume someone adding an answer is a vote
	newAnswer.save()

	response = {"status" : 200, "answer_id" : newAnswer.pk, "answer_text" : answerText}
	return HttpResponse(json.dumps(response), content_type="application/json")

def add_question(request):
	questionText = request.POST.get("question_text")
	newQuestion = Question(questionText)
	newQuestion.save()

	response = {"status" : 200, "question_id" : newQuestion.pk, "question_text" : questionText}
	return HttpResponse(json.dumps(response), content_type="application/json")