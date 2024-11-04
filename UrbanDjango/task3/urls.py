from django.urls import path
from .views import platform, games, cart

urlpatterns = [
    path('platform/', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]

# urlpatterns = [
#     path('platform_view/', platform, name='platform_view'),
#     path('games_view/', games, name='games_view'),
#     path('cart_view/', cart, name='cart_view'),
# ]
