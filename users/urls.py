from django.urls import include
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('account/', AccountUserView.as_view(), name='account'),
    path('account_data/', AccountDataUserView.as_view(), name='account_data'),
    path('logout/', logout_user_view, name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('', include('django.contrib.auth.urls')),
    path('subscriber_email', subscriber_email, name='subscriber_email'),
    path('my_product_review', MyProductReviewView.as_view(), name='my_product_review'),
    path('communication', CommunicationView.as_view(), name='communication'),
]
