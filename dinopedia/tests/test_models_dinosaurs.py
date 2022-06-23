from datetime import datetime, timedelta
from dinosaurs.models import Dinosaur
import pytest


@pytest.fixture
def dinosaur_one(db) -> Dinosaur:
    return Dinosaur.objects.create(
        name="Tyrannosaurus",
        picture1="http://0.0.0.0:8000/uploads/dino1.jpeg",
        picture2="http://0.0.0.0:8000/uploads/dino2.jpeg",
        eating_class="carnivore",
        colour="green",
        period="cretaceous",
        created_at=datetime.now() - timedelta(hours=2),
        updated_at=datetime.now(),
    )


@pytest.fixture
def dinosaur_two(db) -> Dinosaur:
    return Dinosaur.objects.create(
        name="Velociraptor",
        picture1="http://0.0.0.0:8000/uploads/dino3.jpeg",
        picture2="http://0.0.0.0:8000/uploads/dino4.jpeg",
        eating_class="carnivore",
        colour="brown",
        period="cretaceous",
        created_at=datetime.now() - timedelta(hours=2),
        updated_at=datetime.now(),
    )


def test_two_different_dinosaurs_create(dinosaur_one, dinosaur_two):
    assert dinosaur_one.pk != dinosaur_two.pk


def test_dinosaur_name(dinosaur_one):
    expected_string = dinosaur_one.name
    assert str(dinosaur_one) == expected_string


def test_get_total_number_of_likes(dinosaur_one):
    total_number_of_likes = dinosaur_one.dinosaurlike_set.count()
    assert dinosaur_one.get_total_number_of_likes() == total_number_of_likes
