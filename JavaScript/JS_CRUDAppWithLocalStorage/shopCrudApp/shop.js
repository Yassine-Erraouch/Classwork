




// getting the products from the local storage if they exist otherwise an empty array
let products = localStorage.getItem('products') ? JSON.parse(localStorage.getItem('products')) : [];



// assigning each of the inputs and buttons to a variable
    // modal inputs
let productName = document.querySelector('#productName');
let productPrice = document.querySelector('#productPrice');
let productQty = document.querySelector('#productQty');
let productCat = document.querySelector('#productCategory');

    // filter select input
let catFilter = document.querySelector('#filterSelect');

    // create button
let createBtn = document.querySelector('#createBtn');
    // create modal
let filterBtn = document.querySelector('#filterBtn');
    // save Button
let saveBtn = document.querySelector('#saveBtn');

// function to add products
let addProduct = () => {
    if(productName.value == '' || productPrice.value == '' || productQty.value == '' || productCat.value == '') {   
        swal.fire({
            title: "Please fill all the fields",
            icon: "warning",
            button: "Ok"
        })
        return;
    }
    let newProduct = {id: uuidv4(), name:productName.value, price:productPrice.value, quantity:productQty.value, category:productCat.value};
    products.push(newProduct);
    localStorage.setItem('products', JSON.stringify(products));
    swal({
        title: "Product added successfully",
        icon: "success",
        button: "Ok"
    })
}

let fillTable = () => {
    let newP = products.map((p, i)=>(
        `<tr>
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${p.price}</td>  
            <td>${p.quantity}</td>
            <td>${p.category}</td>
            <td>
            <button class="btn btn-primary" onclick="editProduct(${p.id})"><i class="fa-solid fa-pen"></i></button>
            <button class="btn btn-danger" onclick="deleteProduct(${p.id})"><i class="fa-regular fa-trash-can"></i></button>
            </td>
            </tr>`
    )).join('');

    document.querySelector('#productTable tbody').innerHTML = newP;
}

let deleteProduct = (id) => {
   swal.fire({
       title: "Are you sure you want to delete this product?",
       icon: "warning",
       showCancelButton: true,
       confirmButtonColor: "#3085d6",
       cancelButtonColor: "#d33",
       confirmButtonText: "Yes, delete it!"
   }).then((result) => {
   if (result.isConfirmed) {
       products = products.filter(p => p.id != id);
       localStorage.setItem('products', JSON.stringify(products));
       fillTable();
       swal.fire({
           title: "Product deleted successfully",
           icon: "success",
           button: "Ok"
       })
   }
   })
}
    


// running filltable onload to fill the tables with data from local storage
fillTable();