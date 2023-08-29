from django.contrib import admin
from Mylist.models import ToDoItem, ToDoList
admin.site.register(ToDoItem)
admin.site.register(ToDoList)