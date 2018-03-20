from django.db import models
from django_api.users import models as user_models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140, null=True)
    caption = models.TextField(null=True)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField(null=True)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message

class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'user:{} - caption:{}'.format(self.creator.username, self.image.caption)