from rest_framework.routers import DefaultRouter

from apps.todo.api.v1.views import ToDoView, CheckListView

app_name = "todo"

router = DefaultRouter()
router.register('', ToDoView, base_name='')
router.register('(?P<todo_id>\d+)/checklist', CheckListView, base_name='check-list')

urlpatterns = router.urls
