# imdb-movie
The project is a small implementation of imdb movie review like application. The project was created assuming that a movie is directed by a single director.

**Used Tech Stack:**

  1. Django
  2. MySQL
  3. Python
  4. HTML

**Current Features:**

  1. Login/Signup
  2. Create/update/delete director
  3. Add movies, imdb score
  4. Search movies and directors
  5. Filter movies by genre
  6. Admin can mnage users, can add movies, directors, genres.
 
 **For running the application locally:**
  1. Clone the git repo.
     git clone "https://github.com/ssakkshii/imdb-movie.git"
  2. Install requirements in requirements.py
     pip install -r requirements.py
  3. Update the database details in settings.py file.
  4. Run command: python manage.py makemigrations
                  python manage.py migrate
                  python manage.py runserver
  5. Create user.
     python manage.py createsuperuser
  6. And open 127.0.0.1:8000/login in your web browser.

Please find the deatils for usage of APIs, screenshots and detailed documentation in attached Document.doc file.
