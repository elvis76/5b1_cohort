# from .models import Student
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'author', 'publish', 'status')
 list_filter = ('status', 'created', 'publish', 'author')
 search_fields = ('title', 'body')
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('author',)
 date_hierarchy = 'publish'
 ordering = ('status', 'publish')
 

admin.site.register(Comment)

admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display = ('name', 'email', 'post', 'created', 'active')
 list_filter = ('active', 'created', 'updated')
 search_fields = ('name', 'email', 'body') 
 


# admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["name", "email", "is_active", "date_joined"]
#     list_editable = ["is_active"]
#     list_filter = ["is_active", "date_joined"]
