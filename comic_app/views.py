from django.views import generic
from django.urls import reverse

from comic_app.form import AuthorForm, CategoryForm, TitleForm, EvaluationForm
from comic_app.models import Author, Title, Category , Evaluation

class IndexView(generic.ListView):
    template_name = "comic_app/index.html"
    context_objects_name = "title_list"
    queryset = Title.objects.all()

"""
Function-viewの場合

def index(request):
    title_list = Title.objects.all()
    return render(request, "comic_app/index.html", {"title_list": title_list})

"""

class TitleDetailView(generic.DetailView):
    model = Title
    templatename = "comic_app/detail.html"

"""
Function-viewの場合

def titledetail(request, pk):
    title = Title.objects.get(pk=pk)
    return render(request, "comic_app/detail.html", {"title": title})
    
"""
    
class RegisterAuthorView(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "comic_app/register.html"
    def get_success_url(self):
        return reverse("comic_app:index")

"""
Function-viewの場合
def registerauthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            retunr redirect("comic_app:index")
    else:
        form = AuthorForm()
        retunr render(request, "comic_app/register.html", {"form":form})

"""


class RegisterCategoryView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "comic_app/register.html"
    def get_success_url(self):
        return reverse("comic_app:index")

class RegisterTitleView(generic.CreateView):
    model = Title
    form_class = TitleForm
    template_name = "comic_app/register.html"
    def get_success_url(self):
        return reverse("comic_app:index") 

class RegisterEvaluationView(generic.CreateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = "comic_app/register.html"
    def get_success_url(self):
        return reverse("comic_app:index") 

class UpdateEvaluationView(generic.UpdateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = "comic_app/register.html"
    def get_success_url(self):
        return reverse("comic_app:index")
