let storage = localStorage.getItem('store')? JSON.parse(localStorage.getItem('store')): [];

let productName = document.querySelector('#productName');
let productPrice = document.querySelector("#price");


let addOrEdit = 0;

let addProduct = () => {
    if (addOrEdit == 0) {
        document.querySelector("#addOrEditBtn").innerHTML = "Add product";
        // emptying the error containers
        document.querySelector('#nameError').textContent = '';
        document.querySelector('#priceError').textContent = '';
        document.querySelector('#imageError').textContent = '';
        let product = {
            name: productName.value,
            price: productPrice.value,
        }

        if (product.name == '' || sotrage.find(item => item.name ==product.name)){
            document.querySelector('#nameError').textContent = "A product with this name already exists or product name left empty.";
        }
        if (product.price== '' || product.price < 10 || product.price > 100) {
            document.querySelector('#priceError').textContent = "Product price should be between 10 and 100";
        }

        if (product.name != '' && product.price >= 10 && product.price <= 100) {
            sotrage.push(product);
            localStorage.setItem('store', JSON.stringify(sotrage));
        }
    
    } else if (addOrEdit == 1) {
        document.querySelector("#addOrEditBtn").innerHTML = "Save product";
        let product = sotrage.find(item => item.name == productName.value);
        productName.value = product.name;
        productPrice.value = product.price;
        addOrEdit = 0;

        document.querySelector('#productDisplay').innerHTML = storage.map((item, i) => 
            `<div class="card w-25">
                <div class="card-body">
                    <img src="${item.imgUrl}" alt="" class="card-img-top img-fluid">
                    <div class="">
                        <button class="btn-dark btn" id="edit">edit</button>
                        <button class="btn-danger btn" id="remove">Remove</button>
                    </div>
                </div>
            </div>`);



        alert('product Saved successfully');

    };

    
};


document.querySelector('#addBtn').addEventListener('click', () => {
    addOrEdit = 0;
    addProduct();
})

document.querySelector('#editBtn').addEventListener('click', () => {
    addOrEdit = 1;
    addProduct();
})


