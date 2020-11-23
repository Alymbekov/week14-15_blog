from django.urls import path

from .views import (
    PostListApiView, PostDetailApiView
)

urlpatterns =[
    path('<int:pk>/', PostDetailApiView.as_view()),
    path('', PostListApiView.as_view()),
]
