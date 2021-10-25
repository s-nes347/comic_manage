from django.forms import ModelForm
from comic_app.models import Author, Category, Title, Evaluation
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ("name",)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("category",)

class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields =("book_title", 
                 "author_name", 
                 "category_name", 
                 "watch_number", 
                 "watch_date",
                 "state"
                                  
        )

class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields =("book_title",
                "story", 
                 "draw", 
                 "fit", 
                 "character", 
                                                   
        )



