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
    title = forms.CharField(
        max_length=255,
        label="Назва:",
        widget=forms.TextInput(attrs={
            "class": "form-input",
            "placeholder": "Введіть назву задачі"
        }),
        error_messages={
            "required": "Кожному завданню потрібна назва",
            "max_length": "Ого-го! Назва задачі може бути не більше 255 символів."
        }
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-input",
            "placeholder": "Опишіть задачу",
            "rows": 4
        }),
        required=False,
        label="Опис:"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Без категорії",
        label="Категорія:",
        widget=forms.Select(attrs={
            "class": "form-input"
        })
    )
    deadline = forms.DateField(
        required=False,
        label="Дедлайн:",
        widget=forms.DateInput(attrs={
            "class": "form-input",
            "type": "date"
        })
    )