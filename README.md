# Dinosaur API 

The developed API allows you to find all the available kinds of dinosaurs, search for a particular kind, like yu favourite and see your favourites.

## Basic Features

* Custom User model and authentication using email and password.
* Register, Login, Logout, Update password funcionalities and JTW authenication
* CRUD endpoints for a dinosaur wiki page
* Search functionality for finding a dinosaur
* Like functionality
* Swagger documentation provided by drf_spectacular

## Quick start

1. Clone this repo.
2. Run docker-compose --build to build the images. Two containers will be created, the application and the db.
3. Run docker-compose -up -d to start the containers. 
4. Access the API from http://0.0.0.0:8000/api/

For local installation:
1. Use a virtual enviroment
2. install poetry
3. Run poetry update to install all dependencies.
4. docker-compose -up --build -d db
2. python dinopedia/manage.py makemigrations dinosaurs users
3. python dinopedia/manage.py migrate
4. python dinopedia/manage.py runserver 0.0.0.0:8000

## Developmet process

The developed Django project consists of two apps, the user app which is dedicated to the user management and authentication and the dinosaurs app which is dedicated to the dinosaurs wiki features.

### Dinosaurs

Two different data models was developep for the dinosaurs app, the Dinosaur model whinch represents a dinosaur object and the DinosaurLike model which represents a user like to a dinosaur.

Dinosaur Model: Includes the following fields
* name (text field)
* picture1 (django image field)
* picture2 (django image field)
* eating_class (django choices field)
* colour (text field)
* period (django choices field)
* av_size (django choices field)
* created_at (datetime field)
* updated_at (datetime field)

Dinosaur Like Model:
* user (user foreing key)
* dinosaur (dinosaur foreing key)
* created (datetime filed)

A list of endpoints was built on top of that models in order to support the feature mentioned above.

* `get` /api/dinosaurs/: The dinosaur list. Everyone has access to the list, the dinosaur list can be filtered by name.
* `get`, `put`, `path`, `delete` /api/dinosaur/{id}/: Only authenticated users can get, update or remove a particular dinosaur.
* `post` api/dinosaur/create/: Authenticated user can create a new dinosaur.
* `get` api/dinosaur/search/: Authenticated users can full text search a particular dinosaur name using the filter ?search="name", the respected api returns the dinosaur name and their iimages
* `post`, `delete` /api/dinosaurs/{id}/like/: An authenticated user can like a particular dinosaur, or delete their previous like.

### Users

Django Auth user was extend to CustomUser. Custom user can register/login by email address and password. The BaseUserManager class was extend also in order to support functions for creating app users (create_user) and administrator users (create super_user).

A list of endpoints was built on top of the CustomUser model in order to support the feature mentioned above.

* `post` /api/users/register/: The user can register in the system.
* `post` /api/user/login/: A registered user logs into the system.
* `post` /api/user/logout/: A loged in user logs out from the system.
* `get`, `put`, `patch` /api/users/{id}/: An authenicated user can view or update their account.
* `put`, `patch` /api/users/password/change/: An authenicated user can change their password.
* `post` /api/users/token/refresh/: The token of an authenticated user can be manually refreshed.

