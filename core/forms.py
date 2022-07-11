from datetime import datetime

from django import forms

from core.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    deadline = forms.DateField(
        widget=forms.widgets.DateTimeInput(
            attrs={'type': 'datetime-local'}
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
