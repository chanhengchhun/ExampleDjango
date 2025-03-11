# everytime you make changes to the models, you need to run the following commands:
# python manage.py makemigrations -- this will create a migration file in the migrations directory.
# python manage.py migrate -- this will apply the migration to the database.
# python manage.py sqlmigrate polls 0001 -- this will show the SQL commands that will be run on the database.
# python manage.py shell -- this will open the Django shell.
#---------------------------------------------------------


# django.db is a module that contains the Django object-relational mapping (ORM) system.
# An ORM is a tool that allows you to interact with a database using an object-oriented programming language.
# In this case, Django provides a way to define database models using Python classes, which are then translated into database tables.
# The models module contains the base class for all Django models, django.db.models.Model.
from django.db import models

# Question and Choice are subclasses of django.db.models.Model – they inherit all the methods and attributes of Model.
# Each model has a number of class variables, each of which represents a database field in the model.
# Question(models.Model) is a class that has 2 fields: Fields are defined by class attributes. 
# models(lowercase) is a module within the Django package that contains a collection of classes representing database objects.
# Models(uppercase) is a class that is a subclass of django.db.models.Model.
# question_text is a CharField, which is a character field for storing text data.
# pub_date is a DateTimeField, which is a field for storing date and time data.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# Choice(models.Model) is a class that has 3 fields:
# ForeignKey tells Django each Choice is related to a single Question. 
# Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
# Many-to-one means that each record in the table with the foreign key can only appear once in the table with the primary key. 
# each Choice is related to a single Question(one), and each Question can have any number of Choices(many).
# question is a ForeignKey. That tells Django each Choice is related to a single Question.
# question(ForeignKey: foreign key) -  for defining many-to-one relationships.
# choice_text(CharField: character field) -  for storing text data.
# votes(IntegerField: integer field) - for storing integer data.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
