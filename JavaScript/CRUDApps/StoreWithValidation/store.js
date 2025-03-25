let sotrage = localStorage.getItem('store')? JSON.parse(localStorage.getItem('store')): [];

let productName = document.querySelector('#productName');
let productPrice = document.querySelector("#price");

let addProduct = () => {
    product = {
        name: productName.value,
        price: productPrice.value,
    }
    if (!product.name == '') {
        if (sotrage.find(item => item.name ==product.name)) {
            document.querySelector('#nameError').textContent = "A product with this name already exists."
        };
        
        
    }
    if ((product.price >=10 && product.price <= 100)) {
        document.querySelector('#nameError')
    }
}