from . import views
from django.urls import path
urlpatterns = [
    path('home/',views.home,name='home'),
    path('update/<int:pk>',views.update_task_view,name='update'),
    path('delete/<int:pk>',views.delete_task_view,name='delete'),
]