from django.contrib import admin

from comics.models import ComicBookPage, ComicBook


class ComicBookPageInline(admin.TabularInline):
    model = ComicBookPage
    extra = 1


@admin.register(ComicBook)
class ComicBookAdmin(admin.ModelAdmin):
    list_display = ('get_author_full_name', 'title', 'date_of_creation', 'publish')
    search_fields = ('title', 'description')
    list_filter = ('publish',)
    inlines = [ComicBookPageInline]

    fields = ('title', 'description', 'publish')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set author during the first save.
            obj.author = request.user
        super().save_model(request, obj, form, change)

    @admin.display(description='Автор комикса')
    def get_author_full_name(self, obj):
        return obj.author.username

    def get_queryset(self, request):
        return super().get_queryset(request).filter(author=request.user)
