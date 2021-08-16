from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.log_in, name="login"),
    path('post/', views.post, name="post"),
    path('logout/', views.user_logout, name="logout"),
]
