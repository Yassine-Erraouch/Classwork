// the fields
let codeInput = document.querySelector('#itemCode');
let labelInput = document.querySelector('#itemLabel');
let qtyInput = document.querySelector('#qty');
let priceInput = document.querySelector('#price');
let taxInput = document.querySelector('#tax');

// items: array of added objects 
let items = localStorage.getItem('items')?JSON.parse(localStorage.getItem('items')): [];



// verifier: fucntion to verify that all the inputs are filled and valid;

let verifier = () => {
    let code = parseInt(codeInput.value);
    let label = labelInput.value;
    let qty = parseInt(qtyInput.value);
    let price = parseInt(price.value);
    let tax = parseInt(taxInput.value);

    if(!code || !label || !qty || !price || !tax) {
        alert('Please fill all the fields');
        return;
    };

    let item = {code, label, quantity: qty, price, tax};
    items.push(item);
    localStorage.setItem('items', JSON.stringify('items'));

}



