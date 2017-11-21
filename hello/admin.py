from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(MultipleChoice)
admin.site.register(Exam)
admin.site.register(Candidates)
admin.site.register(ExamQuestions)