#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creating the Movie Class and initiate with 5 attributes:
# Movie Title, Storyline, More, Poster Image, Youtube Tailer
class Movie():
    """ ... this is the class documentation docstring ...
    this class creates a template for a movie webpage
    """
    def __init__(self, movie_title, movie_storyline, movie_more, poster_image, trailer_youtube):
        """ ... this is the constructor method docstring ...
        I added self.more and modified it in the fresh_tomatoes.py
        to have a better description of the movies playing
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.more = movie_more
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Create function to launch youtube trailer. Launched on click from static website.
    def show_trailer(self):
        """ show_trailer() docstring...
        lets the magic happen and open this embedded youtube trailer for the selected movie
        """
        webbrowser.open(self.trailer_youtube_url)
