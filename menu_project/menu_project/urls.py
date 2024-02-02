from django.contrib import admin
from django.urls import path
from menu_app.views import index, random_menu, manage_menus, manage_ingredients, delete_menu, edit_menu, save_edit_menu
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random_menu/', random_menu, name='random_menu'),
    path('manage_menus/', manage_menus, name='manage_menus'),
    path('edit_menu/<int:menu_id>/', edit_menu, name='edit_menu'),
    path('save_edit_menu/<int:menu_id>/', save_edit_menu, name='save_edit_menu'),
    path('delete_menu/<int:menu_id>/', delete_menu, name='delete_menu'),
    path('manage_ingredients/', manage_ingredients, name='manage_ingredients'),
    path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
