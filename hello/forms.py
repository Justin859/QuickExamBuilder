from django import forms

QUESTION_TYPES = (('Select', 'Select'), ('MultipleChoice', 'Multiple Choice'))
SECTIONS = (('Select', 'Select'), ('Default', 'Default'))
CORRECT = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))
QUESTION_PICKING = (('Select', 'Select'), ('AutoPick', 'Auto Pick (different questions for all candidates)'), ('AutoPickDiff', 'Auto Pick (same questions for all candidates)'))
AVAILABILITY = (('AlwaysAvailable', 'Always available'), ('AvailableOnSpecificTime', 'Available on specific time'))

class QuestionForm(forms.Form):
    question_type = forms.ChoiceField(required=True, choices=QUESTION_TYPES)
    section = forms.CharField(required=True, max_length=255)
    question_text = forms.CharField(widget=forms.Textarea, max_length=500, required=True)
    answer_field_1 = forms.CharField(label='A', max_length=255, required=True)
    answer_field_2 = forms.CharField(label='B', max_length=255, required=True)
    answer_field_3 = forms.CharField(label='C', max_length=255, required=True)
    answer_field_4 = forms.CharField(label='D', max_length=255, required=True)
    correct_answer = forms.ChoiceField(choices=CORRECT, required=True)
    marks = forms.IntegerField(required=True, min_value=0, max_value=327)

class ExamForm(forms.Form):
    exam_name = forms.CharField(required=True, max_length=255)
    duration = forms.CharField(required=True, max_length=255)
    question_picking = forms.ChoiceField(choices=QUESTION_PICKING)
    availability = forms.ChoiceField(choices=AVAILABILITY, required=True)
    start_date = forms.DateField(label="start date", required = False)
    start_time = forms.TimeField(label="time", required = False)
    end_date = forms.DateField(label="end date", required = False)
    end_time = forms.TimeField(label="time", required = False)
    candidates = forms.CharField(label='Who can take this exam', required=True)
    number_of_questions = forms.IntegerField(required=True, min_value=1)
    from_section = forms.CharField(required=True)

class AddCandidate(forms.Form):
    firstname = forms.CharField(label="First name", required=True, max_length=255)
    lastname = forms.CharField(label="Last name", required=True, max_length=255)
    email = forms.EmailField(label="Email address", required=True, max_length=255)
    password = forms.CharField(label="Password", required=True, max_length=255)
    candidate_group = forms.CharField(label="Candidate group", required=True, max_length=255) 

class QuestionSectionForm(forms.Form):
    section_name = forms.CharField(label="Name for new question section", max_length=255)

class CandidateGroupForm(forms.Form):
    group_name = forms.CharField(label="Name for new candidate group", max_length=255)