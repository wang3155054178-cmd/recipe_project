from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="菜谱名称")
    category = models.CharField(max_length=100, verbose_name="分类")
    ingredients = models.TextField(verbose_name="食材")
    steps = models.TextField(verbose_name="制作步骤")
    image = models.ImageField(upload_to="recipe_img/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
