from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    named_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="Named URL")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse('menu:dynamic_page', kwargs={'named_url': self.named_url})
            except NoReverseMatch:
                return "#"
        return self.url or "#"
