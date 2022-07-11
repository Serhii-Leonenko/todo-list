from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True, )
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-creation_date"]
