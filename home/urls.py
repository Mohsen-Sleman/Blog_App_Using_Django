
from django.urls import include, path
from .views import Home,Details_Post,PostCreate,PostUpdate,PostDelete


urlpatterns = [
    path('',Home.as_view(),name ='home'),
    path('details/<int:pk>' ,Details_Post.as_view(),name='details'),
    path('create/',PostCreate.as_view(),name='create'),
    path('update/<int:pk>' ,PostUpdate.as_view(),name='update'),
    path('delete/<int:pk>' ,PostDelete.as_view(),name='delete')
]
