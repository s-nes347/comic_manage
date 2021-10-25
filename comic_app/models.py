from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="作者")
    
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="カテゴリー")
    
    def __str__(self):
        return self.category

class Title(models.Model):
    book_title = models.CharField(max_length=100, verbose_name="タイトル")
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="作者", related_name='author_name')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="カテゴリー", related_name="category_name")
    watch_number = models.PositiveSmallIntegerField(verbose_name="最終巻数", null=True, blank=True)
    watch_date = models.DateField(verbose_name="読んだ日")
    state_choice = ((1, "未完"), (2,"完結"))
    state = models.IntegerField(verbose_name="状態", null=False, blank=False, choices=state_choice)

    def __str__(self):
        return self.book_title

class Evaluation(models.Model):
    book_title = models.OneToOneField(Title, on_delete=models.CASCADE, verbose_name="タイトル", related_name='evaluation')
    story = models.PositiveSmallIntegerField(verbose_name="内容", validators=[MinValueValidator(1), MaxValueValidator(10)])
    draw = models.PositiveSmallIntegerField(verbose_name="画力", validators=[MinValueValidator(1), MaxValueValidator(10)])
    fit = models.PositiveSmallIntegerField(verbose_name="面白さ", validators=[MinValueValidator(1), MaxValueValidator(10)])
    character = models.PositiveSmallIntegerField(verbose_name="キャラクター", validators=[MinValueValidator(1), MaxValueValidator(10)])
    total_score = models.IntegerField(verbose_name="合計", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_score = self.story + self.draw + self.fit + self.character
        super().save(*args, **kwargs)
