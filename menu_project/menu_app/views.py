from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db import connection
from .models import Menu, Ingredient, MenuIngredient, CodeValue
from .forms import EditMenuForm
import random

# トップ画面表示
def index(request):
    return render(request, 'menu_app/index.html')

# ランダムメニュー画面表示
def random_menu(request):
    menu_main = Menu.objects.filter(menu_category_code = "mc001")
    menu_sub = Menu.objects.filter(menu_category_code = "mc002")
    if menu_main:
        menu_main = random.choice(menu_main)
    if menu_sub:
        menu_sub = random.choice(menu_sub)
    return render(request, 'menu_app/random_menu.html', {'main': menu_main, 'sub': menu_sub})

# メニュー管理画面表示
def manage_menus(request):
    query_result = Menu.objects.extra(
        select={'menu_category_code': 'code_value.name'},
        tables=['code_value'],
        where=['menu.menu_category_code = code_value.code']
    )
    return render(request, 'menu_app/manage_menus.html', {'menus': query_result})

# メニュー編集画面表示
def save_edit_menu(request, menu_id):
    # メニューカテゴリーのデータを取得
    menu_categories = CodeValue.objects.filter(code__startswith = "mc")
    query_result = Menu.objects.filter(menu_id=menu_id).extra(
        select={
            'ingredient_name': 'ingredient.ingredient_name',
            'allergen_level': 'ingredient.allergen_level',
            'menu_id': 'menu.menu_id',
            'code_value' : 'code_value.name'
            
            },
        tables=['code_value','ingredient','menu_ingredient'],
        where=[
            'menu.menu_id = menu_ingredient.menu_id',
            'menu.menu_id = ingredient.ingredient_id',
            'menu.menu_category_code = code_value.code',
        ]
    )
    
    for ingredient in query_result:
        ingredient.allergen_level = "あり" if ingredient.allergen_level == 1 else "なし"
    return render(request, 'menu_app/edit_menu.html', {'menu': query_result, 'menu_categories': menu_categories})

def edit_menu(request, menu_id):
    # メニューカテゴリーのデータを取得
    menu_categories = CodeValue.objects.all()

    # メニュー情報の取得
    menu = Menu.objects.get(menu_id=menu_id)

    if request.method == 'POST':
        # POST リクエストの場合、フォームを使ってデータを処理
        form = EditMenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            # 保存後のリダイレクト先などを指定
            return redirect('manage_menus')
    else:
        # GET リクエストの場合、フォームを初期化して表示
        form = EditMenuForm(instance=menu)

    return render(request, 'menu_app/edit_menu.html', {'form': form, 'menu': menu})


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