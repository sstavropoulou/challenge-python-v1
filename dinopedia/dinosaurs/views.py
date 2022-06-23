# from unicodedata import name
# from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework import generics, status, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from .models import Dinosaur, DinosaurLike
from .serializers import (
    DinosaurSerializer,
    DinosaurPictureSerializer,
    DinosaurLikeSerializer,
)


class DinosaurListAPIView(generics.ListAPIView):
    """
    Get: a collection of dinosaurs
    """

    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ("name", "colour")
    search_fields = ["name"]


class DinosaurAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Update, Delete a dinosaur
    """

    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
    permission_classes = (IsAuthenticated,)


class DinosaurCreateAPIView(generics.CreateAPIView):
    """
    Create: a dinosaur
    """

    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class SearchDinosaurAPIView(generics.ListAPIView):
    queryset = Dinosaur.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DinosaurPictureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class DinosaurLikeAPIView(generics.CreateAPIView):
    """
    Like a Dinosaur
    """

    serializer_class = DinosaurLikeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        dinosaur = get_object_or_404(Dinosaur, id=self.kwargs["pk"])
        new_like, created = DinosaurLike.objects.get_or_create(
            user=request.user, dinosaur=dinosaur
        )
        if created:
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dinosaur = get_object_or_404(Dinosaur, id=self.kwargs["pk"])
        like = DinosaurLike.objects.filter(user=request.user, dinosaur=dinosaur)
        if like.exists():
            like.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
