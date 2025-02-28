const books = [
    {
        ISBN: "9780743273565",
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        rating: 4.5,
        image: "https://m.media-amazon.com/images/I/61dRoDRubtL._AC_UY218_.jpg",
        price: 15.99,
        comments: [
            "A timeless classic about the American Dream.",
            "The characters are so vividly written.",
            "The ending left me speechless."
        ]
    },
    {
        ISBN: "9780061120084",
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        rating: 4.8,
        image: "https://m.media-amazon.com/images/I/81aY1lxk+9L._AC_UY218_.jpg",
        price: 12.99,
        comments: [
            "A powerful story about justice and morality.",
            "Atticus Finch is one of the greatest literary heroes.",
            "This book changed my perspective on life."
        ]
    },
    {
        ISBN: "9780451524935",
        title: "1984",
        author: "George Orwell",
        rating: 4.7,
        image: "https://m.media-amazon.com/images/I/612ADI+BVlL._AC_UY218_.jpg",
        price: 10.99,
        comments: [
            "A chilling depiction of a dystopian future.",
            "Orwell's vision feels more relevant than ever.",
            "Big Brother is watching!"
        ]
    },
    {
        ISBN: "9781503290563",
        title: "Pride and Prejudice",
        author: "Jane Austen",
        rating: 4.6,
        image: "https://m.media-amazon.com/images/I/91AFXQGcPVL._AC_UY218_.jpg",
        price: 8.99,
        comments: [
            "A delightful romance with witty dialogue.",
            "Elizabeth Bennet is such a strong character.",
            "Mr. Darcy is the ultimate romantic hero."
        ]
    },
    {
        ISBN: "9780316769488",
        title: "The Catcher in the Rye",
        author: "J.D. Salinger",
        rating: 4.0,
        image: "https://m.media-amazon.com/images/I/71nXPGovoTL._AC_UY218_.jpg",
        price: 11.99,
        comments: [
            "Holden Caulfield is such a relatable character.",
            "A coming-of-age story that resonates with many.",
            "The writing style is unique and engaging."
        ]
    },
    {
        ISBN: "9780345391803",
        title: "The Hitchhiker's Guide to the Galaxy",
        author: "Douglas Adams",
        rating: 4.4,
        image: "https://m.media-amazon.com/images/I/A1fE+AMrKPL._AC_UY218_.jpg",
        price: 14.99,
        comments: [
            "Hilarious and thought-provoking.",
            "The humor is out of this world!",
            "A must-read for sci-fi fans."
        ]
    },
    {
        ISBN: "9780385490818",
        title: "The Handmaid's Tale",
        author: "Margaret Atwood",
        rating: 4.3,
        image: "https://m.media-amazon.com/images/I/61su39k8NUL._AC_UY218_.jpg",
        price: 13.99,
        comments: [
            "A haunting and powerful story.",
            "Atwood's writing is both beautiful and terrifying.",
            "This book is a wake-up call."
        ]
    },
    {
        ISBN: "9781250080400",
        title: "The Nightingale",
        author: "Kristin Hannah",
        rating: 4.8,
        image: "https://m.media-amazon.com/images/I/81OkWjcf4WL._AC_UY218_.jpg",
        price: 16.99,
        comments: [
            "A heart-wrenching story of love and sacrifice.",
            "The characters feel so real and relatable.",
            "I couldn't put this book down."
        ]
    },
    {
        ISBN: "9780062498533",
        title: "The Hate U Give",
        author: "Angie Thomas",
        rating: 4.7,
        image: "https://m.media-amazon.com/images/I/71ss1p8nk6L._AC_UY218_.jpg",
        price: 12.99,
        comments: [
            "An important and timely story.",
            "Starr's voice is so powerful and authentic.",
            "This book opened my eyes to so many issues."
        ]
    },
    {
        ISBN: "9780316547611",
        title: "The Power",
        author: "Naomi Alderman",
        rating: 4.1,
        image: "https://m.media-amazon.com/images/I/61wncgMzC5L._AC_UY218_.jpg",
        price: 15.99,
        comments: [
            "A fascinating exploration of power dynamics.",
            "The concept is so unique and thought-provoking.",
            "This book kept me hooked from start to finish."
        ]
    },
    {
        ISBN: "9780062060624",
        title: "The Song of Achilles",
        author: "Madeline Miller",
        rating: 4.6,
        image: "https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UY218_.jpg",
        price: 14.99,
        comments: [
            "A beautiful and tragic love story.",
            "Miller's writing is absolutely stunning.",
            "I cried so much while reading this."
        ]
    },
    {
        ISBN: "9781501161933",
        title: "The Seven Husbands of Evelyn Hugo",
        author: "Taylor Jenkins Reid",
        rating: 4.5,
        image: "https://m.media-amazon.com/images/I/71KcUgYanhL._AC_UY218_.jpg",
        price: 13.99,
        comments: [
            "Evelyn Hugo is such a complex and fascinating character.",
            "The storytelling is masterful.",
            "I couldn't stop thinking about this book."
        ]
    },
    {
        ISBN: "9780062662569",
        title: "The Poppy War",
        author: "R.F. Kuang",
        rating: 4.3,
        image: "https://m.media-amazon.com/images/I/71Hso6PrC9L._AC_UY218_.jpg",
        price: 16.99,
        comments: [
            "A dark and gripping fantasy novel.",
            "The world-building is incredible.",
            "Rin's journey is both inspiring and heartbreaking."
        ]
    },
    {
        ISBN: "9780316229296",
        title: "The Fifth Season",
        author: "N.K. Jemisin",
        rating: 4.4,
        image: "https://m.media-amazon.com/images/I/915orvpMXZL._AC_UY218_.jpg",
        price: 14.99,
        comments: [
            "A groundbreaking fantasy series.",
            "Jemisin's writing is so imaginative and powerful.",
            "The world feels so real and immersive."
        ]
    },
    {
        ISBN: "9780316229265",
        title: "The Obelisk Gate",
        author: "N.K. Jemisin",
        rating: 4.3,
        image: "https://m.media-amazon.com/images/I/A1Bzd6IOF+S._AC_UY218_.jpg",
        price: 15.99,
        comments: [
            "A brilliant continuation of the series.",
            "The characters are so well-developed.",
            "The stakes feel so high in this book."
        ]
    },
    {
        ISBN: "9780316229241",
        title: "The Stone Sky",
        author: "N.K. Jemisin",
        rating: 4.5,
        image: "https://m.media-amazon.com/images/I/916klATi9zL._AC_UY218_.jpg",
        price: 16.99,
        comments: [
            "A perfect conclusion to the trilogy.",
            "The emotional payoff is incredible.",
            "Jemisin is a master storyteller."
        ]
    },
    {
        ISBN: "9780765382030",
        title: "The Three-Body Problem",
        author: "Liu Cixin",
        rating: 4.2,
        image: "https://m.media-amazon.com/images/I/910ap6L7TXL._AC_UY218_.jpg",
        price: 14.99,
        comments: [
            "A mind-bending sci-fi masterpiece.",
            "The science is so well-researched and fascinating.",
            "This book made me think about the universe in a whole new way."
        ]
    },
    {
        ISBN: "9780316399623",
        title: "The First Fifteen Lives of Harry August",
        author: "Claire North",
        rating: 4.3,
        image: "https://m.media-amazon.com/images/I/917HFS7sUyL._AC_UY218_.jpg",
        price: 13.99,
        comments: [
            "A unique and gripping time-loop story.",
            "Harry's journey is so compelling.",
            "The concept is executed brilliantly."
        ]
    },
    {
        ISBN: "9780345497529",
        title: "The City & The City",
        author: "China Miéville",
        rating: 4.0,
        image: "https://m.media-amazon.com/images/I/81Z71JsAbEL._AC_UY218_.jpg",
        price: 12.99,
        comments: [
            "A fascinating blend of mystery and speculative fiction.",
            "The world-building is so unique and immersive.",
            "This book kept me guessing until the end."
        ]
    },
    {
        ISBN: "9780307389077",
        title: "The Gone-Away World",
        author: "Nick Harkaway",
        rating: 4.1,
        image: "https://m.media-amazon.com/images/I/91Ti19Ig+hL._AC_UY218_.jpg",
        price: 15.99,
        comments: [
            "A wild and imaginative ride.",
            "The humor and action are perfectly balanced.",
            "This book is unlike anything I've ever read."
        ]
    }
];




// list of selected books
let selection = localStorage.getItem('selection')? JSON.parse(localStorage.getItem('selection')) : [];

// displayBooks(): displays books in the #bookList section.
let displayAllBooks = () => {
    let bookList = document.querySelector('#bookList');

    let info = books.map((book)=> 
    `<div class="col-4 mb-4 ">
        <div class="card d-flex flex-column gap-3 justify-content-center p-3 h-100">
            <div class="card-img-top d-flex justify-content-center p-0">
                <img src="${book.image} " alt="Image unavailable" class="img-fluid">
            </div>
            <div class="card-body p-1 ">
                <div class="card-title fw-bold ">${book.title}</div>
                <div class="card-text">By ${book.author} </div>
                <div class="card-text fst-italic">${book.price} $ </div>
                <div class="card-text"> rating: ${book.rating} </div>
            </div>
    
            <button class="btn btn-navy text-left w-50" onclick="addToSelection(${book.ISBN})">Add</button>
        </div>
    </div>`).join('');

    bookList.innerHTML = info;
};


// displaySelection(): displays books in the #selection section
let displaySelection = () => {
    let selectionList = document.querySelector('#selection');
     
    let info = selection.map((book)=>
    `<div class="col mb-4">
        <div class="card d-flex flex-row  gap-3 justify-content-center px-0">
            <div class="d-flex align-items-center p-3">
                <img src="${book.image} " alt="Image unavailable" class="img-fluid">
            </div>
            <div class="card-body p-1 d-flex flex-column gap-2 justify-content-around">
            <div>
                <div class="card-title fw-bold ">${book.title}</div>
                <div class="card-text">By ${book.author} </div>
                <div class="card-text fst-italic">${book.price} $ </div>
                <div class="card-text"> rating: ${book.rating} </div>
            </div>
                <div class="d-flex gap-2 align-content-">
                <button class="btn btn-navy text-left" onclick="showDetails(${book.ISBN})"data-bs-toggle="modal" data-bs-target="#bookDetails">Details</button>
                <button class="btn btn-danger text-left" onclick="remove(${book.ISBN})">Remove</button>
            
            </div>
            </div>
            
        </div>
    </div>`).join('');

    selectionList.innerHTML = info;

}


// addToSelection(): adds a book to the selection
let addToSelection = (isbn) => {
    let book = books.find((book) => book.ISBN == isbn);

    if(selection.find((book) => book.ISBN == isbn)) {
        alert("You've already selected this book.");
        return;
    }
    selection.push(book);
    localStorage.setItem('selection', JSON.stringify(selection));

    // refreshing the selection section
    displaySelection();
}

// showDetails(): shows details of a book in #selection
let showDetails = (isbn) => {
    let book = books.find((book) => book.ISBN == isbn);
    let titleDiv = document.querySelector('#modalTitle');
    let authorDiv = document.querySelector('#author');
    let priceDive = document.querySelector('#price');
    let commentsDiv = document.querySelector('#comments');
    let imageDiv = document.querySelector('#image');
    
    imageDiv.innerHTML = `<img src="${book.image}" alt="Image unavailable" class="img-fluid">`;
    titleDiv.innerHTML = book.title;
    authorDiv.innerHTML = `By ${book.author}`;
    priceDive.innerHTML = `${book.price} $`;
    commentsDiv.innerHTML = book.comments.map((comment) =>`<div class="  border border-secondary rounded p-2 fst-italic">${comment}</div>
`).join('');
};


let remove = (isbn) => {
    let book = selection.find((book) => book.ISBN == isbn);
    if (confirm(`Are you sure you want to remove ${book.title} from you selection?`)){
        selection.pop(book);
        localStorage.setItem('selection', JSON.stringify(selection));
    };
    displaySelection();
}






// display the books

displayAllBooks();

displaySelection();
