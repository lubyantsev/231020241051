from django.contrib import admin
from .models import Buyer, Game  # Импортируйте вашу модель

admin.site.register(Buyer)  # Регистрация модели Buyer в админке
admin.site.register(Game)    # Регистрация модели Game в админке