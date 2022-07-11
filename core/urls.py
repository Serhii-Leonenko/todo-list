from django.urls import path

from core.views import (
    TaskListView,
    TaskUpdateView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "core"
