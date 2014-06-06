from django.contrib import admin
from blog.models import Category, Article, UserProfile

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'preview')
    list_filter = ('author', 'category')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('title', 'content')
    fields = ('title', 'slug', 'author', 'category', 'content')
    prepopulated_fields = {'slug': ('title', )}

    def preview(self, article):
        """ give the 40 first characters
        """
        text = article.content[0:40]
        if len(article.content) > 40:
            return '%s...' % text
        else:
            return text

    preview.short_description = u'Preview'

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
