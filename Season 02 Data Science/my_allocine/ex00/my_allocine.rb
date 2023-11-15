requests['Display all actors'] = "SELECT * FROM actors;"
requests['Display all genres'] = "SELECT * FROM genres"
requests['Display the name and year of the movies'] = "SELECT mov_title, mov_year FROM movies;"
requests['Display reviewer name from the reviews table'] = "SELECT rev_name FROM reviews;"

requests["Find the year when the movie American Beauty released"] = "SELECT mov_year FROM movies WHERE mov_title LIKE 'American Beauty';"
requests["Find the movie which was released in the year 1999"] = "SELECT mov_title FROM movies WHERE mov_year in (1999);"
requests["Find the movie which was released before 1998"] = "SELECT mov_title FROM movies WHERE mov_year < 1998;"
requests["Find the name of all reviewers who have rated 7 or more stars to their rating order by reviews rev_name (it might have duplicated names :-))"] = "SELECT reviews.rev_name FROM reviews, movies_ratings_reviews WHERE movies_ratings_reviews.rev_stars >= 7 AND reviews.id = movies_ratings_reviews.rev_id ORDER BY reviews.rev_name;"
requests["Find the titles of the movies with ID 905, 907, 917"] = "SELECT mov_title FROM movies WHERE id IN (905, 907, 917);"
requests["Find the list of those movies with year and ID which include the words Boogie Nights"] = "SELECT movies.id, mov_title, mov_year mov_year FROM movies WHERE mov_title LIKE 'Boogie Nights%';"
requests["Find the ID number for the actor whose first name is 'Woody' and the last name is 'Allen'"] = "SELECT id FROM actors WHERE act_fname LIKE 'Woody%' AND act_lname LIKE 'Allen%';"

requests["Find the actors with all information who played a role in the movies 'Annie Hall'"] = "SELECT DISTINCT actors.* FROM actors, movies_actors, movies WHERE movies.mov_title LIKE 'Annie Hall' AND movies.id = movies_actors.mov_id AND  actors.id =  movies_actors.act_id"
requests["Find the first and last names of all the actors who were cast in the movies 'Annie Hall', and the roles they played in that production"] = "SELECT actors.act_fname, actors.act_lname, movies_actors.role FROM actors, movies, movies_actors WHERE movies.mov_title = 'Annie Hall' AND movies.id = movies_actors.mov_id AND actors.id = movies_actors.act_id"

requests["Find the name of movie and director who directed a movies that casted a role as Sean Maguire"] = "SELECT DISTINCT directors.dir_fname , directors.dir_lname, movies.mov_title FROM movies, directors, movies_actors, directors_movies WHERE movies_actors.role LIKE 'Sean Maguire' AND  movies_actors.mov_id = movies.id AND  directors_movies.mov_id = movies.id AND directors.id = directors_movies.dir_id"
requests["Find all the actors who have not acted in any movie between 1990 and 2000 (select only actor first name, last name, movie title and release year)"] = "SELECT actors.act_fname, actors.act_lname, movies.mov_title, cast(substr(movies.mov_dt_rel, 1, 4) AS int)
FROM movies
JOIN movies_actors
	ON movies_actors.mov_id = movies.id
JOIN actors
	ON actors.id = movies_actors.act_id
	
WHERE actors.id NOT IN (
	SELECT actors.id
	FROM actors
	JOIN movies_actors
		ON actors.id = movies_actors.act_id
	JOIN movies
		ON movies.id = movies_actors.mov_id
	WHERE cast(substr(movies.mov_dt_rel, 1, 4) AS int) BETWEEN 1990 AND 2000
)"