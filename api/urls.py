from django.urls import path, include
from . import views

#Using Viewset
from rest_framework.routers import DefaultRouter

#Using Viewset
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailView),

    #Use Normal Views
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    #Using Viewset
    path('', include(router.urls)),

    #Nest Serializers
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]
