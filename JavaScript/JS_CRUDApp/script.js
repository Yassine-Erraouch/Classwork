



let movies = [];
let genres = ['action', 'adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'science-fiction', 'thriller', 'war', 'western'];

let select = document.querySelector('#movieGenre');
genres.forEach((genre) => {
    select.insertAdjacentHTML('beforeend', `<option value="${genre}">${genre}</option>`)
})

let editSelect = document.querySelector('#editMovieGenre');
genres.forEach((genre) => {
    editSelect.insertAdjacentHTML('beforeend', `<option value="${genre}">${genre}</option>`)
})


let fillTable = () => {
    let movieList = document.querySelector('#movieList');
    movieList.innerHTML = '';
    for (let movie of movies) {
        let tr = document.createElement('tr');
        tr.innerHTML = `<td>${movie.id}</td>
                        <td>${movie.title}</td>
                        <td>${movie.genre}</td>
                        <td>${movie.rating}</td>
                        <td>${movie.year}</td>
                        <td>
                            <button class="btn btn-primary" id="modifyBtn" onclick="modifyMovie(${movie.id})" data-bs-toggle="modal" data-bs-target="#editMovieForm">Modify info</button>
                            <button class="btn btn-danger" id="deleteBtn" onclick="deleteMovie(${movie.id})">Delete info</button>
                        </td>
`;
        movieList.appendChild(tr);
    }
}


let addMovie = () => {
    let movieTitle = document.querySelector('#movieTitle').value;
    let movieRating = document.querySelector('#movieRating').value;
    let movieYear = document.querySelector('#movieYear').value;
    let movieGenre = document.querySelector('#movieGenre').value;

    if (!movieTitle || !movieRating || !movieYear || !movieGenre){
        Swal.fire({
            title: '',
            text: 'Please fill all the fields',
            icon: 'warning',
            confirmButtonText: 'ok'
          })
        return;
    }

    if (movies.find(movie => movie.title == movieTitle) && movies.find(movie => movie.year == movieYear)) {
        Swal.fire({
            title: 'Error!',
            text: 'Movie already exists',
            icon: 'error',
            confirmButtonText: 'ok'
          })
        return;
    }


    let movie = {
        id: movies.length > 0?movies[movies.length - 1].id + 1: 1,
        title: movieTitle,
        rating: movieRating,
        year: movieYear,
        genre: movieGenre,
    };
    movies.push(movie);

    // clear the form
    document.querySelector('#movieTitle').value = '';
    document.querySelector('#movieRating').value = '';
    document.querySelector('#movieYear').value = '';
    document.querySelector('#movieGenre').value = '0';

    console.log(movies); //test
    // updating the table
    fillTable();
};
let updateMovie  = () => {}

let modifyMovie = (id) => {
    let movie = movies.find(m => m.id === id)

    document.querySelector('#editMovieTitle').value = movie.title;
    document.querySelector('#editMovieRating').value = movie.rating;
    document.querySelector('#editMovieYear').value = movie.year;
    document.querySelector('#editMovieGenre').value = movie.genre;

    // updating the table
    
    movie.title = document.querySelector('#editMovieTitle').value;
    movie.rating = document.querySelector('#editMovieRating').value;
    movie.year = document.querySelector('#editMovieYear').value;
    movie.genre = document.querySelector('#editMovieGenre').value;

    fillTable();

};


let deleteMovie = (id) => {
    movies = movies.filter(m => m.id !== id);
    fillTable();
};





