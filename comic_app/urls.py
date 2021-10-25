from django.urls import path
from . import views

app_name = "comic_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name ="index"),
    path("/title/<int:pk>/", views.TitleDetailView.as_view(), name="title_detail" ),
    path("/register/author/", views.RegisterAuthorView.as_view(), name="registerauthor"),
    path("/register/category/", views.RegisterCategoryView.as_view(), name="registercategory"),
    path("/register/title/", views.RegisterTitleView.as_view(), name="registertitle"),
    path("/register/evaluation/", views.RegisterEvaluationView.as_view(), name="registerevaluation"),
    path("/update/evaluation/<int:pk>/", views.UpdateEvaluationView.as_view(), name='update/evaluation'),
    
]