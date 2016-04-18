from django.contrib import admin
from books.models import Book, Author, Publisher

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book
    extra = 3

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 3

class BookAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


a="""
class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

#    fieldsets = [
#        ('Question Statement', {'fields': ['question_text']}),
#        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
"""
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
