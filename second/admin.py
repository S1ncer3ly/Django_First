from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Post, Comment, Contact

# Register your models here.

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


# for config of categories admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)
    list_filter = ('cat_id',)
    list_per_page = 5


# for config of Post admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('post_id',)
    list_per_page = 5

    class Media:
        js = ('https://cdn.tiny.cloud/1/hfarogfgmyudmiio0xqj6hkv348yp25tyoxv3p10xhm4i8x0/tinymce/6/tinymce.min.js',
              'js/script.js',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'date_added']
    actions = ['delete_selected_comments']

    def delete_selected_comments(self, request, queryset):
        # Perform the delete operation on selected comments
        queryset.delete()

    delete_selected_comments.short_description = 'Delete selected comments'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
    actions = ['delete_selected_Contacts']

    def delete_selected_Contact(self, request, queryset):
        # Perform the delete operation on selected Contacts
        queryset.delete()

    delete_selected_Contact.short_description = 'Delete selected Contacts'

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)