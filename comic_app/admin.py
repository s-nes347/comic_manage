from django.contrib import admin

from comic_app.models import Author, Category, Evaluation, Title

admin.site.register(Author)   
admin.site.register(Category)
admin.site.register(Title)
admin.site.register(Evaluation)
