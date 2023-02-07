
from django.urls import path

from users.views import *

urlpatterns = [
    path('users/login/', auth_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view),
]

