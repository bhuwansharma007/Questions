from enum import unique
from django.db import models

# Create your models here.
# able name - bookshelf
# 1 - name
# 2 - author
# 3 - ISBN number
# 4 - publication
# 5 - genre

class Bookshlf(models.Model):
  name = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  ISBN_number = models.IntegerField()
  publication = models.CharField(max_length=255)
  genre = models.CharField(max_length=255)