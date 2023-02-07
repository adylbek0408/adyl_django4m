
from django.urls import path

from users.views import *

urlpatterns = [
    path('login/', auth_view),
    path('register/', register_view),
    path('logout/', logout_view),
]

