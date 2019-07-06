from django.urls import path
from . import views
from .views import KevtestView, AboutView


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('kevtest', views.kevtest, name='kevtest'),
    path('kevtest', KevtestView.as_view(), name='kevtest'),
    path('about', AboutView.as_view(), name='about')
]


