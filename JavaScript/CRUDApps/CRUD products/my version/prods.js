// my elements
const form = document.getElementById("prodForm");
const productName = document.getElementById("prodName");
const productPrice = document.getElementById("prodPrice");
const productList = document.getElementById("ProductList");
const productIdField = document.getElementById("prodId");


// initializing the products array
let products = localStorage.getItem('products')?JSON.parse(localStorage.getItem('products')):[];



// display function
function displayProducts() {
    productList.innerHTML = "";  

    products.forEach((product, index) => {
        productList.innerHTML += `
        <tr>
            <td><input type="checkbox" class="ck" value="${index}"/></td>
            <td>${element.code}</td>
            <td>${element.name}</td>
            <td>${element.price}</td>
        </tr>`});
    
};




form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    const id = productIdField.value;
    const name = productName.value;
    const price = productPrice.value;
    const image = previewImage.src;


    if (!name || !price) {
        alert("Veuillez remplir tous les champs !");
        return;
    }

    const newProduct = { name, price}; 

    /*The id comes from the productIdField element,
    which is a hidden field in the form. The value of this field is set when the user clicks 
    the "Modifier" (Edit) button next to a product in the product list.
    */

    if (id) {
        products[id] = newProduct; 
    } else {
        products.push(newProduct); 
    }

    localStorage.setItem("products", JSON.stringify(products));
    form.reset();
    productIdField.value = "";
    displayProducts();
});


function deleteProduct(index) {
    products.splice(index, 1);
    localStorage.setItem("products", JSON.stringify(products));
    displayProducts();
}

// editin product
function editProduct(index) {
    const product = products[index];
    productName.value = product.name;
    productPrice.value = product.price;
    previewImage.src = product.image;
    previewImage.style.display = "block";
    productIdField.value = index;
};

document.getElementById('mainCheck').onclick = function (e) {
    let allCk = document.querySelectorAll('.ck');
    [...allCk].forEach((elt, pos) => {
        elt.checked = e.target.checked;
    });
}


document.querySelector('#deleteMany').addEventListener('click', function (e) {
    let allIds = [...document.querySelectorAll('.ck:checked')].map((c, i) => parseInt(c.value));
    for (let v in allIds) {
        students.splice(v, 1);
    }


    displayData();

});


// displaying products on load
displayProducts();