from django.urls import path

from core.views import (
    signup, index, update_profile, dashboard
)

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user_profile/', update_profile, name='update_profile'),
]
