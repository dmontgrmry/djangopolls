from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently') # table header on listing questions view
    list_filter = ['pub_date'] # filter on listing qestions view
    search_fields = ['question_text'] # search bar on listing questions view

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date published', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
