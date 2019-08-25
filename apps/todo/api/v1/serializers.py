from rest_framework import serializers
from apps.commons.mixins.serializers import DynamicFieldsModelSerializer

from apps.todo.models import ToDo, CheckList


class ToDoSerializer(DynamicFieldsModelSerializer):
    checklist = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = [
            'id', 'content', 'status', 
            'created_at', 'modified_at', 'checklist_title' ,
            'checklist', 'description', 'due_date'
        ]        
        read_only_field = ['created_at', 'modified_at']

    def get_checklist(self, obj):
        return CheckListSerializer(obj.checklist, many=True).data


class CheckListSerializer(DynamicFieldsModelSerializer):   
    title = serializers.CharField(max_length=32, write_only=True)

    class Meta:
        model = CheckList
        fields = ['id', 'item', 'completed', 'title']       

    def validate(self,attrs):
        todo = self._get_todo()

        checklist_title = attrs.pop('title')
        todo.checklist_title = checklist_title
        todo.save()

        attrs.update(
            {'todo': todo}
        )

        return attrs

    def _get_todo(self):
        try:
            return ToDo.objects.get(id=self.context['todo_id'])
        except ToDo.DoesNotExist:
            raise serializers.ValidationError('Invalid todo.')

    def save(self, **kwargs):
        checklist_data = {
            'todo': self.validated_data['todo'],
            'item': self.validated_data['item'],        
        }

        checklist, created = CheckList.objects.get_or_create(**checklist_data)
        if not created:
            checklist.completed = created or self.validate_data.get('completed', True)
            checklist.save()
        return checklist

        self.context['todo_id']