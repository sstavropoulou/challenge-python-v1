from pickle import TRUE
from django.db import models
from django.conf import settings

# Create your models here.


class Dinosaur(models.Model):
    class EatingClassType(models.TextChoices):
        HERBIVORE = "herbivore"
        OMNIVORE = "omnivore"
        CARNIVORE = "carnivore"

    class PeriodType(models.TextChoices):
        TRIASSIC = "triassic"
        JURASSIC = "jurassic"
        CRETACEOUS = "cretaceous"
        PALEOGENE = "paleogene"
        NEOGENE = "neogene"

    class AverageSizeType(models.TextChoices):
        TINY = "tiny"
        VERY_SMALL = "very_small"
        SMALL = "small"
        MEDIUM = "medium"
        LARGE = "large"
        VERY_LARGE = "very_large"

    name = models.CharField(max_length=200)
    picture1 = models.ImageField(upload_to="uploads", null=True)
    picture2 = models.ImageField(upload_to="uploads", null=True)
    eating_class = models.TextField(choices=EatingClassType.choices)
    colour = models.TextField()
    period = models.TextField(choices=PeriodType.choices)
    av_size = models.TextField(choices=AverageSizeType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_total_number_of_likes(self):
        return self.dinosaurlike_set.count()


class DinosaurLike(models.Model):
    """
    Model to like Dinosaurs
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dinosaur = models.ForeignKey(Dinosaur, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
