from django.urls import path
from . import api_views
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('',views.signup,name='main_page'),
    path('task/list', views.list, name='list'),
    path('task/<str:pk>/', views.details, name='details'),
    path('task/', views.create, name='create'),
    path('task/<str:pk>/update/', views.update, name='update'),
    path('task/<str:pk>/delete/', views.delete, name='delete'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('tasks/', api_views.TaskList.as_view(),name='task-list'),
    path('tasks/<int:pk>/', api_views.TaskDetail.as_view(),name='task-detail'),
    path('users/', api_views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', api_views.UserDetail.as_view(),name='user-detail'),
    path('', api_views.api_root),
    path('tasks/<int:pk>/highlight/', api_views.TaskHighlight.as_view(),name='task-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)