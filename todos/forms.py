from todos.models import TodoItem
from django.forms import ModelForm


class CreateTodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title"]
