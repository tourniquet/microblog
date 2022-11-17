from django.db import models

class Topic(models.Model):
  text = models.CharField(max_length=100)

  def __str__(self):
    return self.text


class Post(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
  text = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'posts'

  def __str__(self):
    return f'{self.text[:50]}...'
