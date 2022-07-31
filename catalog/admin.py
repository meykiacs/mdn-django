from django.contrib import admin

from . import models

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 0

class BooksInline(admin.TabularInline):
    model = models.Book
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

    def display_genre(self, book):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ", ".join(genre.name for genre in book.genre.all()[:3])

    display_genre.short_description = "Genre"
    
    inlines = [BooksInstanceInline]

admin.site.register(models.Book, BookAdmin)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

    inlines = [BooksInline]

admin.site.register(models.Language)
admin.site.register(models.Genre)


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )
