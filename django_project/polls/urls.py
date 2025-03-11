from django.urls import path

from . import views


app_name = "polls"  # This is the namespace for the app. it will be used to differentiate between different apps in the project.
urlpatterns = [
    # (name=) "identify" the view in the template. 
    # views is a class, index is a method in the class. views.index is the view function inside views.py class. 
    # this mean that when the user goes to the root URL, the index view will be called.
    path("", views.index, name="index"), # name="index" is the name of the URL that will be used to identify the view in the template
    
    path("<int:question_id>/", views.detail, name="detail"), #<int:question_id> is a placeholder for the question_id. It will be replaced by the actual question_id when the URL is called.
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]