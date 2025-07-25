-- List all genres of the show Dexter using the hbtn_0d_tvshows database
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_shows.title = 'DEXTER'
ORDER BY tv_genres.name ASC;