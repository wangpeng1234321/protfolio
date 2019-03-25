from django.contrib import admin
from . import models # 从本级导入model

# Register your models here.

admin.site.register(models.Blog) #或者括号中写Blog,注册model
