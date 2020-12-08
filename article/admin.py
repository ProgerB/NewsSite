from django.contrib import admin
from article.models import Article, Category, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'create_at']
    list_filter = ['title']


class ArticleImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ArticleImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Images)

