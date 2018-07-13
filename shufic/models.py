from django.db import models


class Video(models.Model):
    class Meta():
        db_table = "Video"
    Video_url = models.URLField()
    Video_name = models.CharField(max_length=200)
    Video_o = models.TextField()
    Video_data = models.DateTimeField()
    Video_likes = models.IntegerField(default=0)

    def __str__(self):
        return  self.Video_name

class Comment(models.Model):
    class Meta():
        db_table = "Comment"
    Comment_text = models.TextField()
    Comment_Video = models.ForeignKey(Video, True)

    def __str__(self):
        return  self.Comment_text
# Create your models here.
