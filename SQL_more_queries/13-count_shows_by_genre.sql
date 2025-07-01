-- Lists all genres from hbtn_0d_tvshows ad displays the number of shows linked to each
SELECT tv_genres.name, tv_show_genres.genre_id
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genre
ORDER BY tv_show_genres.genre_id ASC;