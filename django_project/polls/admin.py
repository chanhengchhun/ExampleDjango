from django.contrib import admin
from .models import Question

# I need admin.site.register(Question) to register the Question model with the admin site.
admin.site.register(Question)
