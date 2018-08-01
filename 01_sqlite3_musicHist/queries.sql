-- Question 1: Query all of the entries in the Genre table

SELECT genre.label
FROM Genre

-- Question 2: Using the INSERT statement, add one of your favorite artists to the Artist table.

INSERT into Artist (artistname, yearestablished)
values("John Mayer", 1998)

-- Question 3: Using the INSERT statement, add one, or more, albums by your artist to the Album table.

INSERT into Album
select null, "Continuum", 2005, 67387, "Columbia", artist.ArtistId,  genre.genreid
FROM Artist, Genre
WHERE Artist.artistname = "John Mayer"
AND Genre.Label = "Rock"

-- Question 4: Using the INSERT statement, add some songs that are on that album to the Song table.

INSERT into Song
select null, "Gravity", 405, 2006, genre.genreid, artist.artistid, album.AlbumId
FROM Genre, Artist, Album
WHERE Genre.Label = "Rock"
AND Artist.artistname = "John Mayer"
AND Album.Title = "Continuum"

-- Question 5: Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.

SELECT art.ArtistName, s.title, al.title
FROM Song s
LEFT JOIN album al ON s.albumid = al.albumid
LEFT JOIN Artist art ON art.artistid = al.artistid
WHERE art.Artistname = "John Mayer"

-- Question 6: Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as "Song Count", al.title
FROM Album al
JOIN Song ON song.AlbumId = al.albumid
group by al.AlbumId

-- Question 7: Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as "Artist Songs", Artist.ArtistName
FROM Artist
JOIN Song
ON Artist.ArtistId = song.artistId
group by song.artistId

-- Question 8: Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as "Songs by Genre", genre.label
FROM Genre
JOIN Song
ON song.GenreId = Genre.GenreId
group by genre.Label

-- Question 9: Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.

SELECT max(Album.AlbumLength) as "Longest Album", Album.Title
FROM Album

-- Question 10: Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.

SELECT max(Song.SongLength) AS "Longest Song", Song.Title AS "Song Name"
FROM Song


-- Question 11: Modify the previous query to also display the title of the album.

SELECT max(Song.SongLength) AS "Longest Song", Song.Title AS "Song Name", Album.Title
FROM Song, Album