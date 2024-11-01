from django.db import models


# Create your models here.
class CommonModel(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: True
