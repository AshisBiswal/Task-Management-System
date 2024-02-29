from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',views.user_login,name = 'login'),
    path('',views.home,name = 'home'),
    path('register/',views.register,name = 'register'),
    path('task/',views.task,name = 'task_page'),
    path('addtask/',views.addtask,name="addtask"),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('comment/<int:task_id>/', views.comments, name='comment'),
    path('delete_comment/<int:comment_id>/', views.deletecomment, name='delete_comment'),
    path('delete_task/<int:task_id>/', views.deletetask, name='delete_task')
]
