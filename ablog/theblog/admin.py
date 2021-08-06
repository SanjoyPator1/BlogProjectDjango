from django.contrib import admin
from .models import Post, Category, Privacy

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Privacy)