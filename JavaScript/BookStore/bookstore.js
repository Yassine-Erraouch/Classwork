
// the books list
let books = [
    { ISBN: "123456", title: "The Great Gatsby", image: "", price: 15.99 },
    { ISBN: "654321", title: "To Kill a Mockingbird", image: "", price: 12.99 },
    { ISBN: "789012", title: "1984", image: "", price: 10.99 },
    { ISBN: "345678", title: "Pride and Prejudice", image: "", price: 8.99 },
    { ISBN: "901234", title: "The Catcher in the Rye", image: "", price: 11.99 },
    { ISBN: "567890", title: "The Hitchhiker's Guide to the Galaxy", image: "", price: 14.99 },
    { ISBN: "123095", title: "The Handmaid's Tale", image: "", price: 13.99 },
    { ISBN: "456782", title: "The Nightingale", image: "", price: 16.99 },
    { ISBN: "789654", title: "The Hate U Give", image: "", price: 12.99 },
    { ISBN: "234567", title: "The Power", image: "", price: 15.99 },
    { ISBN: "890123", title: "The Song of Achilles", image: "", price: 14.99 },
    { ISBN: "456789", title: "The Seven Husbands of Evelyn Hugo", image: "", price: 13.99 },
    { ISBN: "123490", title: "The Poppy War", image: "", price: 16.99 },
    { ISBN: "678901", title: "The Fifth Season", image: "", price: 14.99 },
    { ISBN: "234901", title: "The Obelisk Gate", image: "", price: 15.99 },
    { ISBN: "456109", title: "The Stone Sky", image: "", price: 16.99 },
    { ISBN: "789012", title: "The Three-Body Problem", image: "", price: 14.99 },
    { ISBN: "345678", title: "The First Fifteen Lives of Harry August", image: "", price: 13.99 },
    { ISBN: "901234", title: "The City & The City", image: "", price: 12.99 },
    { ISBN: "567890", title: "The Gone-Away World", image: "", price: 15.99 }
  ];

// cart array
let cart = localStorage.getItem('cart')? JSON.parse(localStorage.getItem('cart')): [];










// the global variables

// the select
let bookList = document.querySelector('#books');   

// the display table
let infoTable = document.querySelector('#bookInfoTable');

// the cart table
let cartTable = document.querySelector('#cartTable')

// the cart total

let cartTotal = document.querySelector('#total')






// charger: function that fills the #books select with book titles as options
let charger = () => {
    

        // using a for loop 
    // for (let book of books){
    //     let title = book.title;
    //     let isbn = book.ISBN;
        
    //     bookList.innerHTML += `<option value="${isbn}">${title}</option>`;
    // }

    
        // using map
    const options = books.map((book) => `<option value="${book.ISBN}">${book.title}</option>`).join('');

    bookList.innerHTML += options;
}


// afficher: function that displays the information of the book slected in #books;
let afficher = () => {
    let book = books.find((book)=> book.ISBN === bookList.value);
    let info = `<tr>
                    <td class="fs-4 fw-bold" colspan='2'>Book ${book.ISBN}</td>
                </tr>
                <tr>
                    <td class="fw-bold">Title</td>
                    <td>${book.title} </td>
                </tr>

                <tr>
                <td class="fw-bold">Price</td> 
                <td>${book.price} </td>
                </tr>

                <tr>
                    <td class="fw-bold">Image</td> 
                    <td><img src="${book.image} " alt="Image unavailable"></td>
                </tr>`;
    infoTable.innerHTML = info;
}

// ajouter: fucntion to add a book to cart;
let ajouter = () => {

    if(bookList.value == "") {
        alert('Please select a book first');
        return;
    }
    let book = books.find((book)=> book.ISBN === bookList.value);
    cart.push(book);
    localStorage.setItem('cart', JSON.stringify(cart));

    let booksInCart = cart.map((book)=> `<tr>
                                            <td>${book.title} </td>
                                        </tr>
                                        <tr>
                                            <td>${book.price} </td>
                                        </tr>`).join('');
    let cartTable.innerHTML = booksInCart;
    let total = cart.reduce((acc, cur) => { return acc + cur.price}, 0);
    cartTotal.textContent = total.toFixed(2);
    console.log(total.toFixed(2), typeof(total))
    console.log('added');
}



// laoding books to the book select on load
charger();

// binding afficher() to the select
bookList.addEventListener('change', afficher);