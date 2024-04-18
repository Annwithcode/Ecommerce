from django.urls import path

from userauths import views

urlpatterns = [
 
    path('sign-up',views.register_view,name='sign-up'),
    path('login',views.login_view,name='login'),
    path('sign-out',views.logout_view,name='logout')


]
