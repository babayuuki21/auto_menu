from django.contrib import admin
from django.urls import path
from menu_app.views import delete_menu
from menu_app.views import random_menu, manage_menus, manage_ingredients

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random_menu/', random_menu, name='random_menu'),
    path('manage_menus/', manage_menus, name='manage_menus'),
    path('manage_ingredients/', manage_ingredients, name='manage_ingredients'),
    path('delete_menu/<int:menu_id>/', delete_menu, name='delete_menu'),
]
