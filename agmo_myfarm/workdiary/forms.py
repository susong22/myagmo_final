# workdiary/forms.py
from django import forms
from .models import WorkDiary

class WorkDiaryForm(forms.ModelForm):
    class Meta:
        model = WorkDiary
        fields = ['selected_date', 'work']
        widgets = {
            'selected_date': forms.DateInput(attrs={'type': 'date'}),
        }
def __init__(self, *args, **kwargs):
        super(WorkDiaryForm, self).__init__(*args, **kwargs)
        # selected_date 필드의 기본값을 오늘 날짜로 설정
        self.fields['selected_date'].initial = timezone.now().date()