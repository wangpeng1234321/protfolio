from django.contrib import admin
from .models import Gallery # 从当前文件路径中的models中导入app
#（不要忘记迁移命令，访问需创建超级管理员权限）

# Register your models here.

admin.site.register(Gallery) # 注册app
