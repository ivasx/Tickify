from django import forms
from tasks.models import Task, Category


class TaskAdminForm(forms.ModelForm):
    """
    Метод для відображення в адмін панелі тільки категорій, які відповідають власнику завдання.
    """
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and getattr(self.instance, "user_id", None):
            self.fields['category'].queryset = Category.objects.filter(user=self.instance.user)
        else:
            self.fields['category'].queryset = Category.objects.none()


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    deadline = forms.DateField(required=False)