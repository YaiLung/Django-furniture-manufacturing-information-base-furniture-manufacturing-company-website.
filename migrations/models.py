from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    category = models.CharField(max_length=100, default="Продукты", verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-time_create', 'title']

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя клиента")
    email = models.EmailField(verbose_name="Email клиента")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    # Другие поля, которые могут быть необходимы для клиентов

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

from django.db import models

class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Order #{self.id}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование склада")
    location = models.CharField(max_length=255, verbose_name="Местоположение склада")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость (в единицах товара)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя сотрудника")
    position = models.CharField(max_length=255, verbose_name="Должность")
    department = models.CharField(max_length=255, verbose_name="Отдел")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")
    hire_date = models.DateField(verbose_name="Дата приема на работу")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'
