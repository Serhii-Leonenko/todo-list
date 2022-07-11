from django.shortcuts import render
from django.views import generic

from core.forms import TaskForm
from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    pass


class TagUpdateView(generic.UpdateView):
    pass


class TagDeleteView(generic.UpdateView):
    pass
