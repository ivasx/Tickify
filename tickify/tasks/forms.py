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
    # class Meta:
    #     model = Task
    #     fields = '__all__'
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.user:
    #         self.fields['category'].queryset = Category.objects.filter(user=self.user)
    #         self.fields['category'].empty_label = "Без категорії"
    #     else:
    #         self.fields['category'].queryset = Category.objects.none()
    title = forms.CharField(max_length=255, label="Назва:")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Опис:")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="Без категорії", label="Категорія:")
    deadline = forms.DateField(required=False, label="Дедлайн:")