#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importing my other classes and functions
# fresh_tomatoes.py is used for creating the fresh_tomatoes.html
import fresh_tomatoes
import media

# Create list of my six favorite movies by instantiating 6 movie classes
man_on_fire = media.Movie("Man on Fire", "Denzel on vendetta as a bodyguard","http://www.imdb.com/title/tt0328107/","https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg","https://www.youtube.com/watch?v=g4kLizDXLY0")

inside_out = media.Movie("Inside Out", "Riley moves to San Francisco","http://www.imdb.com/title/tt2096673/","https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg","https://www.youtube.com/watch?v=_MC3XuMvsDI")

jurassic_world = media.Movie("Jurassic World", "Dinosaurs are back","http://www.imdb.com/title/tt0369610/","https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg","https://www.youtube.com/watch?v=RFinNxS5KN4")

star_wars = media.Movie("Star Wars", "May the force be with you","http://www.imdb.com/title/tt2488496/","https://upload.wikimedia.org/wikipedia/en/e/e6/Star_Wars_The_Force_Awakens_Teaser_Poster.jpg","https://www.youtube.com/watch?v=wCc2v7izk8w")

mission_impossible_five = media.Movie("Mission Impossible 5", "May the force be with you","http://www.imdb.com/title/tt2381249/","https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg","https://www.youtube.com/watch?v=gOW_azQbOjw")

spectre = media.Movie("Spectre", "British Secret service...","http://www.imdb.com/title/tt2379713/","http://ia.media-imdb.com/images/M/MV5BMjIwNTA1MDA2Ml5BMl5BanBnXkFtZTgwNzIzMTA5NDE@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=LTDaET-JweU")

# Creating the list
movies = [man_on_fire, inside_out, jurassic_world, star_wars, mission_impossible_five, spectre]

# Passing the list to the open_movies_page function with parameter 'movies'
# Generate HTML for static web page and launch
fresh_tomatoes.open_movies_page(movies)