from django.db import models

class Blog(models.Model):

    class Meta:
        db_table = 'blog'
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ['-id']

    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание',)
    date = models.DateField('Дата',)
    image = models.ImageField('Фото', upload_to='blog/images/', blank=True)
    url = models.URLField('Ссылка на пост', blank=True)

    def __str__(self):
        return self.title