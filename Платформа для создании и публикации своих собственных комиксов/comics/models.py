from django.db import models
from django.urls import reverse


class ComicBook(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания комикса")
    publish = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<ComicBook(id={self.id}, title='{self.title}', author_id={self.author_id})>"

    def get_absolute_url(self):
        return reverse('comic_detail', args=[self.pk])

    class Meta:
        ordering = ['-date_of_creation']
        verbose_name = "Комикс"
        verbose_name_plural = "Комиксы"

        indexes = [
            models.Index(fields=['-date_of_creation']),
        ]


class ComicBookPage(models.Model):
    comic_book = models.ForeignKey(ComicBook, on_delete=models.CASCADE, verbose_name="Комикс")
    image = models.ImageField(upload_to='comicbook_pages/', verbose_name="Изображение")

    class Meta:
        ordering = ['-id']
        verbose_name = "Страница комикса"
        verbose_name_plural = "Страницы комиксов"

    def __str__(self):
        return f"{self.comic_book.title} - Page {self.id}"

    def __repr__(self):
        return f"<ComicBookPage(id={self.id}, comic_book_id={self.comic_book_id})>"
