import fresh_tomatoes
import media

man_on_fire = media.Movie("Man on Fire", "In a Mexico City wracked by a recent wave of kidnappings, ex-CIA operative John Creasy (Denzel Washington) reluctantly accepts a job as a bodyguard for 9-year-old Lupita (Dakota Fanning), the daughter of wealth…","http://www.imdb.com/title/tt0328107/","https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg","https://www.youtube.com/watch?v=g4kLizDXLY0")

inside_out = media.Movie("Inside Out", "Riley (Kaitlyn Dias) is a happy, hockey-loving 11-year-old Midwestern girl, but her world turns upside-down when she and her parents move to San Francisco. Riley's emotions -- led by Joy (Amy Poehler) -- try to guide her through this difficult, life-changing event. However, the stress of the move br…","http://www.imdb.com/title/tt2096673/","https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg","https://www.youtube.com/watch?v=_MC3XuMvsDI")

jurassic_world = media.Movie("Jurassic World", "Located off the coast of Costa Rica, the Jurassic World luxury resort provides a habitat for an array of genetically engineered dinosaurs, including the vicious and intelligent Indominus rex. When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok. Now…","http://www.imdb.com/title/tt0369610/","https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg","https://www.youtube.com/watch?v=RFinNxS5KN4")

star_wars = media.Movie("Star Wars", "The further adventures of Luke Skywalker (Mark Hamill), Han Solo (Harrison Ford) and Princess Leia (Carrie Fisher)...","http://www.imdb.com/title/tt2488496/","https://upload.wikimedia.org/wikipedia/en/e/e6/Star_Wars_The_Force_Awakens_Teaser_Poster.jpg","https://www.youtube.com/watch?v=wCc2v7izk8w")

mission_impossible_five = media.Movie("Mission Impossible 5", "With the IMF now disbanded and Ethan Hunt (Tom Cruise) out in the cold, a new threat -- called the Syndicate -- soon emerges. The Syndicate is a network of highly skilled operatives who are dedicated to establishing a new world order via an escalating series of terrorist attacks. Faced with what may…","http://www.imdb.com/title/tt2381249/","https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg","https://www.youtube.com/watch?v=gOW_azQbOjw")

spectre = media.Movie("Spectre", "A cryptic message from his past sends James Bond (Daniel Craig) on a quest to uncover a sinister organization while M (Ralph Fiennes) battles political forces that want to shut down the British secret service...","http://www.imdb.com/title/tt2379713/","http://ia.media-imdb.com/images/M/MV5BMjIwNTA1MDA2Ml5BMl5BanBnXkFtZTgwNzIzMTA5NDE@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=LTDaET-JweU")

movies = [man_on_fire, inside_out, jurassic_world, star_wars, mission_impossible_five, spectre]
fresh_tomatoes.open_movies_page(movies)
