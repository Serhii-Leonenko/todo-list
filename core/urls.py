from django.urls import path

from core.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "core"
