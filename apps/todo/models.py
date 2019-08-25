from django.db import models
from apps.commons.models import BaseModel
from apps.commons.choices import TODO_STATUS, TODO, DOING, DONE


class ToDo(BaseModel):
    content = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    checklist_title  = models.CharField(max_length=32, default="Untitled")
    status = models.CharField(choices=TODO_STATUS, default=TODO, max_length=6)
    
    class Meta:
        ordering = ['modified_at']

    def __str__(self):
        return f'{self.content[:30]}...'

    @property
    def todo(self):
        return ToDo.objects.filter(status=TODO)

    @property
    def doing(self):
        return ToDo.objects.filter(status=DOING)

    @property
    def done(self):
        return ToDo.objects.filter(status=DONE)

    @property
    def checklist(self):
        return self.todo_checklists.all()


class CheckList(BaseModel):
    todo = models.ForeignKey(ToDo, related_name='todo_checklists', on_delete=models.CASCADE)
    item = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.item}'