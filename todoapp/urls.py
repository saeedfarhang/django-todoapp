from django.urls import path
from .views import home_view, todo_list_view,todo_item_create ,delete_todo_item


app_name = 'todoapp'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', todo_list_view, name='todo_list'),
    path('create/', todo_item_create, name='todo_item_create'),
    path('<id>/delete/', delete_todo_item, name='todo_item_delete'),
]
