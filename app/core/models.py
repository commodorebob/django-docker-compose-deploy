from django.db import models

class Sample(models.Model):
    attachment = models.FileField()

class Book(models.Model):
    Author = models.CharField(max_length=100)
    Title = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)
    ThumbnailUrl = models.URLField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Branch(models.Model):
    BranchName = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=2)
    Zip = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20, blank=True, null=True)

class Inventory(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('Book', 'Branch')
