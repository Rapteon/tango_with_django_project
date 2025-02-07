from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # Defining prepopulated field for slug to expedite user's
    # job of defining slugs. We can't add a category without
    # a slug, so this is necessary.
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")


admin.site.register(Page, PageAdmin)
