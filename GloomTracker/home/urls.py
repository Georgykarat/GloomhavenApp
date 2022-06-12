from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("createsquad/", views.create_squad, name="create_squad"),
    path("<squadid>/", views.open_menu, name='pathpage'),
    path("<squadid>/addrep/", views.add_rep, name='add_rep'),
    path("<squadid>/minrep/", views.min_rep, name='min_rep'),
    path("<squadid>/addpro/", views.add_pro, name='add_pro'),
    path("<squadid>/minpro/", views.min_pro, name='min_pro'),
    path("<squadid>/addch/", views.add_ch, name='add_ch'),
    path("<squadid>/minch/", views.min_ch, name='min_ch'),
    path("<squadid>/map/", views.gloom_map, name='map'),
]