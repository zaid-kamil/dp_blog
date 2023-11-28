from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField("Article title", max_length=100)
    image = models.ImageField("Article image", upload_to="articles/images")
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    likes = models.PositiveIntegerField("Total likes",default=0)
    def __str__(self):
        return self.title
    
