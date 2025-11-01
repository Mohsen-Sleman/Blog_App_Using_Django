from django.urls import  path
from django.views.generic.base import TemplateView
from .views import Regester,Profile,CoustomLoginView,CoustomLogoutView,ConfirmLogout
urlpatterns = [
    path('regester/',Regester.as_view(),name='regester'),
    path('profile/',Profile.as_view(),name='profile'),
    path('login/',CoustomLoginView.as_view(),name='login'),
    path('logout/',CoustomLogoutView.as_view(),name='logout'),
    path('logout/confirm',ConfirmLogout.as_view(),name='logout_confirm'),
]
