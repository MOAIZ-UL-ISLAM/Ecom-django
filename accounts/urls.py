
from django.urls import path
from accounts.views import RegistrationView,ActivateView

urlpatterns = [
    
    path("register/",RegistrationView.as_view(), name="register"),
    path('account/activate/<str:uid>/<str:token>/', ActivateView.as_view(), name='activate'),
]
