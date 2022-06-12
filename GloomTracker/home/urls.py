from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("createsquad/", views.create_squad, name="create_squad"),
    path("<squadid>/", views.open_menu, name='pathpage'),
    path("<squadid>/addrep/", views.add_rep, name='add_rep'),
    path("<squadid>/minrep/", views.min_rep, name='min_rep'),
]