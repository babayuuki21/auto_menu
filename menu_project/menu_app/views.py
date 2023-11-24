from django.shortcuts import render, redirect
from django.http import Http404
from .models import Menu, FoodIngredient
import random

def random_menu(request):
    menus = Menu.objects.all()
    random_menu = random.choice(menus)
    ingredients = random_menu.ingredients.all()
    return render(request, 'menu_app/random_menu.html', {'menu': random_menu, 'ingredients': ingredients})

def manage_menus(request):
    menus = Menu.objects.all()
    return render(request, 'menu_app/manage_menus.html', {'menus': menus})

def manage_ingredients(request):
    ingredients = FoodIngredient.objects.all()
    return render(request, 'menu_app/manage_ingredients.html', {'ingredients': ingredients})

def add_menu(request):
    # 既存のメニューを取得
    menus = Menu.objects.all()

    # 新しいメニューを作成して保存
    new_menu = Menu(name='New Menu')
    new_menu.save()

    # 全メニューからランダムに一つを選択
    random_menu = random.choice(menus)
    ingredients = random_menu.ingredients.all()

    return render(request, 'menu_app/random_menu.html', {'menu': random_menu, 'ingredients': ingredients})

def delete_menu(request, menu_id):
    try:
        # 特定のIDのメニューを取得
        menu_to_delete = Menu.objects.get(pk=menu_id)
        
        # メニューを削除
        menu_to_delete.delete()
        
        # 成功メッセージなどを追加すると良い
        
        
    except Menu.DoesNotExist:
        # エラーメッセージなどを追加すると良い
        raise Http404("Menu does not exist")
    
    # 削除後にリダイレクトなどを行う
    return redirect('some_redirect_url')