
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/<int:pk>/', views.student_detail, name="stuent-detail"),
    path('info/', views.students_detail, name="stuents-detail"),
    
]
