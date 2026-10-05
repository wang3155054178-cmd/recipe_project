from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe

# 首页
def home(request):
    recipes = Recipe.objects.all()
    return render(request, "home.html", {"recipes": recipes})

# 菜谱详情
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})

# 添加菜谱，需要登录
@login_required
def recipe_add(request):
    if request.method == "POST":
        # 接收表单数据，保存菜谱
        pass
    return render(request, "recipe_add.html")

# 编辑菜谱
@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        # 更新菜谱数据
        pass
    return render(request, "recipe_edit.html", {"recipe": recipe})

# 删除菜谱
@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect("home")
    return render(request, "recipe_delete.html", {"recipe": recipe})

# 分类页面
def recipe_category(request, cat_name):
    recipes = Recipe.objects.filter(category=cat_name)
    return render(request, "recipe_category.html", {"recipes": recipes})

# 用户注册
def register(request):
    if request.method == "POST":
        # 创建用户
        pass
    return render(request, "register.html")

# 用户登录
def user_login(request):
    if request.method == "POST":
        # 验证用户
        pass
    return render(request, "login.html")

# 个人中心
@login_required
def profile(request):
    my_recipes = Recipe.objects.filter(author=request.user)
    return render(request, "profile.html", {"my_recipes": my_recipes})
