from rest_framework import serializers

from .models import Dinosaur, DinosaurLike


class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = "__all__"


class DinosaurPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ("name", "picture1", "picture2")


class DinosaurLikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DinosaurLike
        fields = ("id", "user", "dinosaur")
