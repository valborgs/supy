from django.contrib import admin

# Register your models here.
from firstapp.models import Post, FileUpload

admin.site.register(Post)
admin.site.register(FileUpload)