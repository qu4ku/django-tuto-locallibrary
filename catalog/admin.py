from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
# First way of registering things
admin.site.register(Author, AuthorAdmin)

# We don't change that, standard way:
admin.site.register(Genre)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
            }),
        ('Availability', {
            'fields': ('status', 'due_back')
            }),
    )

