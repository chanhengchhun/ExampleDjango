# django.http is a module that contains classes and functions to handle HTTP requests and responses.
from django.http import HttpResponse #still needed because of having details, results, and vote functions

from django.shortcuts import render # render is a shortcut function that combines the template loading and rendering process into one step.
from django.template import loader

from .models import Question


# index(request) is a view function that takes a web request and returns a web response.
# This view function returns an HttpResponse object that contains the text "Hello, world. You're at the polls index."
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list,}
    # How this works:
    # 1. The view function index() is called when the user accesses the URL mapped to it.
    # 2. It queries the database for the latest 5 questions using the Question model.
    # 3. It loads the template "polls/index.html" using the loader.get_template() function.
    # loader.get_template() is a function that loads a template from the filesystem.
    return render(request, "polls/index.html", context) 



# detail(request, question_id) is a view function that takes a web request and a question ID as arguments.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

# results(request, question_id) is a view function that takes a web request and a question ID as arguments.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# vote(request, question_id) is a view function that takes a web request and a question ID as arguments.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)