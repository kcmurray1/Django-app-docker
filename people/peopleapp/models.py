from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(null=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.CASCADE,
        related_name="children"
    )

    def __str__(self):
        if self.parent:
            return f"{self.id} {self.name} with parent {self.parent}"
        return f"{self.id} {self.name}"