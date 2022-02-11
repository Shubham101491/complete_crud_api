from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='all'),
    path('students/<int:pk>/', views.students, name='specific_data'),
    path('post/',views.post,name='post_data'),
    path('put/<int:pk>/',views.update,name='update_data'),
    path('patch/<int:pk>/',views.patial_update,name='patch'),
    path('delete/<int:pk>/',views.delete,name='delete')
]
