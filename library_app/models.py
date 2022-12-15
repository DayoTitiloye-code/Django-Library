from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=(100))

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=(100))
    name = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} - {self.name}'


