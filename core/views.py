from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.forms import TaskForm
from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    pass


class TagUpdateView(generic.UpdateView):
    pass


class TagDeleteView(generic.UpdateView):
    pass
