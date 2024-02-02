from django.shortcuts import render, redirect
from django.http import Http404
from django.db import connection
from .models import Menu, Ingredient, MenuIngredient, CodeValue
import random

# トップ画面表示
def index(request):
    return render(request, 'menu_app/index.html')

# ランダムメニュー画面表示
def random_menu(request):
    menus = Menu.objects.all()
    random_menu = random.choice(menus)
    ingredients = random_menu.ingredients.all()
    return render(request, 'menu_app/random_menu.html', {'menu': random_menu, 'ingredients': ingredients})

# メニュー管理画面表示
def manage_menus(request):
    query_result = Menu.objects.extra(
        select={'menu_category_code': 'code_value.name'},
        tables=['code_value'],
        where=['menu.menu_category_code = code_value.code']
    )
    return render(request, 'menu_app/manage_menus.html', {'menus': query_result})


# 食材管理画面表示
def manage_ingredients(request):
    ingredients = Ingredient.objects.all()  # 食材データを取得
    
    for ingredient in ingredients:
        ingredient.allergen_level = "あり" if ingredient.allergen_level == 1 else "なし"
    return render(request, 'menu_app/manage_ingredients.html', {'ingredients': ingredients})

def custom_query_sample():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table WHERE some_condition;")
        result = cursor.fetchall()
        return result
    


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