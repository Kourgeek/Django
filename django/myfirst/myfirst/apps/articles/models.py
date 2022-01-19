import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('Название статьи',max_length=200)
	article_text = models.TextField('Текст статьи')
	publication_date = models.DateTimeField('Дата публикации')
	#like = models.IntegerField('Количество лайков')

	def __str__(self):
		return self.article_title
	
	def was_published_recently(self):
		return self.publication_date >= (timezone.now()-datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Имя автора',max_length=50)
	comment_text = models.CharField('Текст комментария',max_length=200)
	
	def __str__(self):
		return self.comment_text

	class Meta:
		verbose_name = 'Комметарий'
		verbose_name_plural = 'Комментарии'