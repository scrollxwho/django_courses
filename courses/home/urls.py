from .views import index, pricing, RegisterUser, UsersView, exit, UsersLoginView, SendEmail
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('prices', pricing, name="pricing"),
    path('registration', RegisterUser.as_view(), name="registration"),
    path('users', UsersView.as_view(), name="users"),
    path('exit', exit, name="exit"),
    path('login', UsersLoginView.as_view(), name="login"),
    path('email', SendEmail.as_view(), name="send_emails"),

]