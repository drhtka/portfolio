from django.db import models


class Project(models.Model):
    
    class Meta:
        db_table = 'project'
        verbose_name = 'портфолио'
        verbose_name_plural = 'портфолио'
    
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание', max_length=250)
    image = models.ImageField('Фото', upload_to='personal_portfolio/images/')
    url = models.URLField('Ссылка на сайт', blank=True)
    adaptiv = models.BooleanField('Адаптив', null=True)

    def __str__(self):
        return self.title

