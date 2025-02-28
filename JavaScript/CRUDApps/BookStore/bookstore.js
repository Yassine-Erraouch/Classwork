
// the books list
// let books = [
//     { ISBN: "123456", title: "The Great Gatsby", image: "", price: 15.99 },
//     { ISBN: "654321", title: "To Kill a Mockingbird", image: "", price: 12.99 },
//     { ISBN: "789012", title: "1984", image: "", price: 10.99 },
//     { ISBN: "345678", title: "Pride and Prejudice", image: "", price: 8.99 },
//     { ISBN: "901234", title: "The Catcher in the Rye", image: "", price: 11.99 },
//     { ISBN: "567890", title: "The Hitchhiker's Guide to the Galaxy", image: "", price: 14.99 },
//     { ISBN: "123095", title: "The Handmaid's Tale", image: "", price: 13.99 },
//     { ISBN: "456782", title: "The Nightingale", image: "", price: 16.99 },
//     { ISBN: "789654", title: "The Hate U Give", image: "", price: 12.99 },
//     { ISBN: "234567", title: "The Power", image: "", price: 15.99 },
//     { ISBN: "890123", title: "The Song of Achilles", image: "", price: 14.99 },
//     { ISBN: "456789", title: "The Seven Husbands of Evelyn Hugo", image: "", price: 13.99 },
//     { ISBN: "123490", title: "The Poppy War", image: "", price: 16.99 },
//     { ISBN: "678901", title: "The Fifth Season", image: "", price: 14.99 },
//     { ISBN: "234901", title: "The Obelisk Gate", image: "", price: 15.99 },
//     { ISBN: "456109", title: "The Stone Sky", image: "", price: 16.99 },
//     { ISBN: "789012", title: "The Three-Body Problem", image: "", price: 14.99 },
//     { ISBN: "345678", title: "The First Fifteen Lives of Harry August", image: "", price: 13.99 },
//     { ISBN: "901234", title: "The City & The City", image: "", price: 12.99 },
//     { ISBN: "567890", title: "The Gone-Away World", image: "", price: 15.99 }
//   ];

let books = [
    { ISBN: "9780743273565", title: "The Great Gatsby", image: "https://m.media-amazon.com/images/I/61dRoDRubtL._AC_UY218_.jpg", price: 15.99 },
    { ISBN: "9780061120084", title: "To Kill a Mockingbird", image: "https://m.media-amazon.com/images/I/81aY1lxk+9L._AC_UY218_.jpg", price: 12.99 },
    { ISBN: "9780451524935", title: "1984", image: "https://m.media-amazon.com/images/I/71rpa1-kyvL._AC_UL320_.jpg", price: 10.99 },
    { ISBN: "9781503290563", title: "Pride and Prejudice", image: "https://m.media-amazon.com/images/I/91AFXQGcPVL._AC_UY218_.jpg", price: 8.99 },
    { ISBN: "9780316769488", title: "The Catcher in the Rye", image: "https://m.media-amazon.com/images/I/71nXPGovoTL._AC_UY218_.jpg", price: 11.99 },
    { ISBN: "9780345391803", title: "The Hitchhiker's Guide to the Galaxy", image: "https://m.media-amazon.com/images/I/A1fE+AMrKPL._AC_UY218_.jpg", price: 14.99 },
    { ISBN: "9780385490818", title: "The Handmaid's Tale", image: "https://m.media-amazon.com/images/I/61su39k8NUL._AC_UY218_.jpg", price: 13.99 },
    { ISBN: "9781250080400", title: "The Nightingale", image: "https://m.media-amazon.com/images/I/81OkWjcf4WL._AC_UY218_.jpg", price: 16.99 },
    { ISBN: "9780062498533", title: "The Hate U Give", image: "https://m.media-amazon.com/images/I/71ss1p8nk6L._AC_UY218_.jpg", price: 12.99 },
    { ISBN: "9780316547611", title: "The Power", image: "https://m.media-amazon.com/images/I/61wncgMzC5L._AC_UY218_.jpg", price: 15.99 },
    { ISBN: "9780062060624", title: "The Song of Achilles", image: "https://m.media-amazon.com/images/I/81msb6gUBTL._AC_UY218_.jpg", price: 14.99 },
    { ISBN: "9781501161933", title: "The Seven Husbands of Evelyn Hugo", image: "https://m.media-amazon.com/images/I/71KcUgYanhL._AC_UY218_.jpg", price: 13.99 },
    { ISBN: "9780062662569", title: "The Poppy War", image: "https://m.media-amazon.com/images/I/71Hso6PrC9L._AC_UY218_.jpg", price: 16.99 },
    { ISBN: "9780316229296", title: "The Fifth Season", image: "https://m.media-amazon.com/images/I/915orvpMXZL._AC_UY218_.jpg", price: 14.99 },
    { ISBN: "9780316229265", title: "The Obelisk Gate", image: "https://m.media-amazon.com/images/I/A1Bzd6IOF+S._AC_UY218_.jpg", price: 15.99 },
    { ISBN: "9780316229241", title: "The Stone Sky", image: "https://m.media-amazon.com/images/I/916klATi9zL._AC_UY218_.jpg", price: 16.99 },
    { ISBN: "9780765382030", title: "The Three-Body Problem", image: "https://m.media-amazon.com/images/I/910ap6L7TXL._AC_UY218_.jpg", price: 14.99 },
    { ISBN: "9780316399623", title: "The First Fifteen Lives of Harry August", image: "https://m.media-amazon.com/images/I/917HFS7sUyL._AC_UY218_.jpg", price: 13.99 },
    { ISBN: "9780345497529", title: "The City & The City", image: "https://m.media-amazon.com/images/I/81Z71JsAbEL._AC_UY218_.jpg", price: 12.99 },
    { ISBN: "9780307389077", title: "The Gone-Away World", image: "https://m.media-amazon.com/images/I/91Ti19Ig+hL._AC_UY218_.jpg", price: 15.99 }
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
                    <td class="fs-4 fw-bold" colspan='2'>Book${book.ISBN}</td>
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
                    <td><img src="${book.image} " alt="Image unavailable" class="img-fluid w-25 h-25"></td>
                </tr>`;
    infoTable.innerHTML = info;
}


let loadCart = () => {
    let booksInCart = cart.map((book)=> `<tr    >
                                            <td>${book.title} </td>
                                            <td>${book.price} </td>
                                            <td>${book.quantity} </td>
                                        </tr>`).join('');
    cartTable.innerHTML = booksInCart;
    let total = cart.reduce((acc, cur) => { return acc + cur.price*cur.quantity}, 0);
    cartTotal.textContent = total.toFixed(2);
}
// ajouter: fucntion to add a book to cart;
let ajouter = () => {

    if(bookList.value == "") {
        alert('Please select a book first');
        return;
    }
    let book = books.find((book)=> book.ISBN === bookList.value);
    if (cart.find((item) => item.ISBN === book.ISBN)) {
        let book2 = {...book, quantity: cart.find((item) => item.ISBN === book.ISBN).quantity + 1};
        cart[cart.findIndex(item => item.ISBN === book.ISBN)] = book2;
        loadCart();
    } else{
        book = {...book, quantity: 1};
        cart.push(book);
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));

    let booksInCart = cart.map((book)=> `<tr>
                                            <td>${book.title} </td>
                                            <td>${book.price} </td>
                                            <td>${book.quantity} </td>
                                        </tr>`).join('');
    
    
    loadCart();
};

// retirer: function to remove item from cart
let retirer = () => {
    if(bookList.value == "") {
        alert('Please select a book first');
        return;
    }
    if (confirm('Are you sure you want to remove this item from your cart?')) {
        let book = books.find((book)=> book.ISBN === bookList.value);
        if(!cart.find((item) => item.ISBN === book.ISBN)) {
            alert('This book is not in your cart');
            return;
        }
        cart = cart.filter((item) => item.ISBN !== book.ISBN);
        localStorage.setItem('cart', JSON.stringify(cart));
        
        loadCart();
    }
    
}

// laoding books to the book select on load
charger();

// loading the cart from local storage on load
loadCart();

// binding afficher() to the select
bookList.addEventListener('change', afficher);