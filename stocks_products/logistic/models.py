from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Stock(models.Model):
    address = models.CharField(
        max_length=200, unique=True, verbose_name="Адресс склада"
    )
    products = models.ManyToManyField(
        Product,
        through="StockProduct",
        related_name="stocks",
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="positions",
        verbose_name="Склад",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="positions",
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество",)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
    )

    def __str__(self):
        return self.product.title
