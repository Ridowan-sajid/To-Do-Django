from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.todo_create,name="todo-form"),
    path('',views.home,name="home"),
    path('update_form/<int:pk>/',views.update_todo,name="up_form"),
    path('detail_form/<int:pk>/',views.detail_todo,name="det_form"),
    path('delete_form/<int:pk>/',views.delete_todo,name="dele_form")
]
