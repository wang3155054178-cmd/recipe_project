from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Recipe


# ---------------------- Главная страница 首页 ----------------------
def home(request):
    """
    Прототип представления: главная страница со списком всех рецептов
    """
    recipes = Recipe.objects.all()
    return render(request, "recipe/home.html", {"recipes": recipes})


# ---------------------- Детальная страница рецепта 菜谱详情 ----------------------
def recipe_detail(request, recipe_id):
    """
    Прототип представления: просмотр детальной информации рецепта
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe})


# ---------------------- Добавить рецепт 添加菜谱 ----------------------
@login_required
def recipe_add(request):
    """
    Прототип представления: создание нового рецепта (только для авторизованных)
    """
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        if title and category:
            Recipe.objects.create(
                title=title,
                category=category,
                ingredients=ingredients,
                steps=steps,
                author=request.user
            )
            return redirect("home")
    return render(request, "recipe/recipe_add.html")


# ---------------------- Редактировать рецепт 编辑菜谱 ----------------------
@login_required
def recipe_edit(request, recipe_id):
    """
    Прототип представления: редактирование существующего рецепта (только автор)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == "POST":
        recipe.title = request.POST.get("title")
        recipe.category = request.POST.get("category")
        recipe.ingredients = request.POST.get("ingredients")
        recipe.steps = request.POST.get("steps")
        recipe.save()
        return redirect("recipe_detail", recipe_id=recipe.id)
    return render(request, "recipe/recipe_edit.html", {"recipe": recipe})


# ---------------------- Удалить рецепт 删除菜谱 ----------------------
@login_required
def recipe_delete(request, recipe_id):
    """
    Прототип представления: подтверждение и удаление рецепта (только автор)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == "POST":
        recipe.delete()
        return redirect("home")
    return render(request, "recipe/recipe_delete.html", {"recipe": recipe})


# ---------------------- Рецепты по категории 按分类查看菜谱 ----------------------
def recipe_category(request, cat_name):
    """
    Прототип представления: фильтрация рецептов по категории
    """
    recipes = Recipe.objects.filter(category=cat_name)
    return render(request, "recipe/recipe_category.html", {"recipes": recipes})


# ---------------------- Регистрация пользователя 用户注册 ----------------------
def register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        if uname and pwd:
            # 判断用户名是否已经存在
            if User.objects.filter(username=uname).exists():
                # 用户名已存在，返回注册页面，不创建用户
                return render(request, "recipe/register.html")
            user = User.objects.create_user(username=uname, password=pwd)
            login(request, user)
            return redirect("home")
    return render(request, "recipe/register.html")



# ---------------------- Авторизация пользователя 用户登录 ----------------------
def user_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            next_page = request.POST.get("next")
            # 如果next为空或者没有，跳转到home
            if next_page:
                return redirect(next_page)
            else:
                return redirect("home")
    return render(request, "recipe/login.html")




# ---------------------- Личный кабинет 个人中心 ----------------------
@login_required
def profile(request):
    """
    Прототип представления: личный кабинет пользователя, список его рецептов
    """
    my_recipes = Recipe.objects.filter(author=request.user)
    return render(request, "recipe/profile.html", {"my_recipes": my_recipes})
