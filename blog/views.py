from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_page(request):
    blogs = Blog.objects # 将model.py文件中的所有对象赋予变量blogs
    return render(request, 'blog.html', {'blogs':blogs}) # 变量blogs传递到字典blogs中，
                                                         # 通过字典blogs传递到blogs.html，在通过html 文件进行使用
