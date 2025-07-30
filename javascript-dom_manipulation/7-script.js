const { useLayoutEffect } = require("react");

document.addEventListener("DOMContentLoaded", function () {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => response.json())
        .then(data => {
            const listMovies = document.querySelector("ul.list_movies");
            const films = data.results;

            films.foreach(film => )
})
    .catch(error => console.log(error));
});