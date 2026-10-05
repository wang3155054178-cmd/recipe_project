from django.urls import path
from . import views

urlpatterns = [
    # 首页
    path('', views.home, name='home'),
    # 菜谱详情
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    # 添加菜谱
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    # 编辑菜谱
    path('recipe/edit/<int:recipe_id>/', views.recipe_edit, name='recipe_edit'),
    # 删除菜谱
    path('recipe/delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'),
    # 用户注册
    path('accounts/register/', views.register, name='register'),
    # 用户登录
    path('accounts/login/', views.user_login, name='user_login'),
    # 个人中心
    path('accounts/profile/', views.profile, name='profile'),
    # 分类筛选
    path('recipe/category/<str:cat_name>/', views.recipe_category, name='recipe_category'),
]
