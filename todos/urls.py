from django.urls import path

from todos.views import (
    index,
    action_add_new_todo,
    action_toggle_todo,
    action_delete_todo,
)

urlpatterns = [
    path("", index, name="index"),
    path("action_add_new_todo", action_add_new_todo, name="action_add_new_todo"),
    path(
        "action_toggle_todo/<int:item_id>",
        action_toggle_todo,
        name="action_toggle_todo",
    ),
    path(
        "action_delete_todo/<int:item_id>",
        action_delete_todo,
        name="action_delete_todo",
    ),
]
