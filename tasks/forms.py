from django import forms
from django.core.exceptions import ValidationError

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


class AddTaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        empty_label="Без категорії",
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'category', 'deadline', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-input", "placeholder": "Введіть назву задачі"}),
            'description': forms.Textarea(attrs={"class": "form-input", "placeholder": "Опишіть задачу", "rows": 4}),
            'priority': forms.Select(attrs={"class": "form-input"}),
            'deadline': forms.DateInput(attrs={"class": "form-input", "type": "date"}),
        }
        labels = {
            'title': 'Назва задачі:',
            'description': 'Опис:',
            'category': 'Категорія:',
            'deadline': 'Дедлайн:',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.user = user

        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

        self.fields['category'].widget.attrs.update({"class": "form-input"})

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        if self.user and category and category.user != self.user:
            raise ValidationError('Завдання не може бути в категорії другого користувача')

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 250:
            raise forms.ValidationError("Ого-го! Назва задачі може бути не більше 250 символів.")
        return title

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category and self.user and category.user != self.user:
            raise forms.ValidationError("Категорія не належить цьому користувачу")
        return category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-input","placeholder": "Введіть назву категорії"}),
        }
        labels = {
            'name': 'Назва категорії:',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.user and Category.objects.filter(user=self.user, name=name).exists():
            raise forms.ValidationError('Категорія з такою назвою вже існує.')
        return name

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл")
