from django.contrib import admin
from .models import Post, Category, Privacy
from django_summernote.admin import SummernoteModelAdmin

#summernote
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Privacy)

