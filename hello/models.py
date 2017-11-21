from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Question(models.Model):
    section = models.CharField(max_length=255)
    question_text = models.TextField(max_length=500)
    question_type = models.CharField(max_length=255)
    question_id = models.CharField(max_length=255, default='')
    user_id = models.CharField(max_length=1001)
    marks = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.question_text

class MultipleChoice(models.Model):
    user_id = models.CharField(max_length=1001)
    question_id = models.CharField(max_length=1001)
    answer_field_1 = models.CharField(max_length=255)
    answer_field_2 = models.CharField(max_length=255)
    answer_field_3 = models.CharField(max_length=255)
    answer_field_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255, default='A')

    def __str__(self):
        return self.question_id
    
    class Meta:
        verbose_name = 'Multiple Choice Question'
        verbose_name_plural = 'Multiple Choice Questions'

class Exam(models.Model):
    user_id = models.CharField(max_length=255)
    exam_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    question_picking = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    candidates = models.CharField(max_length=255)
    number_of_questions = models.IntegerField()

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'    

class Candidates(models.Model):
    admin_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    candidate_group = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

class ExamQuestions(models.Model):
    exam_id = models.CharField(max_length=255)
    question_section = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    question_id = models.CharField(max_length=255)

    def __str__(self):
        return self.question_id
    
    class Meta:
        verbose_name = 'Exam Question'
        verbose_name_plural = 'Exam Questions'
