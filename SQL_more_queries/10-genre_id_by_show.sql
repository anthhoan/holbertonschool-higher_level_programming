--  Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_shows.title ON genre_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id