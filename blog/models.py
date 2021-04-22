from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Content")
    like = models.IntegerField(verbose_name="Like")
    views = models.IntegerField(verbose_name="Views")

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        # ordering = ['views']


class CommentModel(models.Model):
    com_cont = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blog

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

# Create your models here.
