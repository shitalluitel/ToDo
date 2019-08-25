from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.todo.api.v1.serializers import ToDoSerializer, CheckListSerializer
from apps.todo.models import ToDo, CheckList


class ToDoView(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backend = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['status',]
    
    def get_serializer(self, *args, **kwargs):        
        if not self.request.method.lower() == 'get':                   
            kwargs.update(
                {
                    'exclude_fields': ['description', 'due_date', 'checklist_title']
                }
            ) if self.request.method.lower() == 'post' else kwargs.update(
                                {
                                    'exclude_fields': ['checklist_title']
                                })
                
        return super().get_serializer(*args, **kwargs)

class CheckListMixins:
    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx.update(self.kwargs)
        return ctx

class CheckListView(CheckListMixins, ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    filter_backend = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['completed']

    def get_queryset(self):
        return super().get_queryset().filter(todo_id=self.kwargs['todo_id'])
    
    def get_serializer(self, *args, **kwargs):      
        if self.request.method == "POST":
            kwargs.update({'exclude_fields': ['completed']})
        return super().get_serializer(*args, **kwargs)