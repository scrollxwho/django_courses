from .views import profile, RegisterUser, UsersView, UsersLoginView, SendEmail
from django.urls import path


urlpatterns = [
    path('home', profile, name='profile' ),
    path('registration', RegisterUser.as_view(), name="registration"),
    path('users', UsersView.as_view(), name="users"),
    path('exit', exit, name="exit"),
    path('login', UsersLoginView.as_view(), name="login"),
    path('email', SendEmail.as_view(), name="send_emails"),

]

