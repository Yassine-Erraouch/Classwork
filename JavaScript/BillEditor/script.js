// the inputs
let codeInput = document.querySelector('#itemCode');
let labelInput = document.querySelector('#itemLabel');
let qtyInput = document.querySelector('#qty');
let priceInput = document.querySelector('#price');
let taxInput = document.querySelector('#tax');






// the display section for the items
let display = document.querySelector('#display');

// items: array of added objects 
let items = localStorage.getItem('items')?JSON.parse(localStorage.getItem('items')):[];


codeInput.value = 1;

// verifier: fucntion to verify that all the inputs are filled and valid;

let verifier = () => {
    code = codeInput.value;
    label = labelInput.value;
    qty = parseInt(qtyInput.value);
    price = parseFloat(priceInput.value);
    tax = parseInt(taxInput.value);
    console.log(`label: ${price}, qty: ${qty}, price: ${tax}`);
    if(!code || !label || !qty || !price || !tax) {
        alert('Please fill all the fields');
        return;
    };
    return true;

};


// displayItems(): function to fill the items table;
let displayItems = () => {
    display.innerHTML= "";
    let itemsToDisplay = items.map((item)=> `<tr>
    <td>${item.code} </td>
    <td>${item.label} </td>
    <td>${item.quantity} </td>
    <td>${item.price} </td>
    <td>${item.tax} </td>
    <td>${item.price*item.quantity} </td>
    <td>
        <button class="btn btn-primary" id="edit" onclick="editItem(${item.code})">Edit</button>
        <button class="btn btn-danger" id="remove" onclick="removeItem(${item.code})">Remove</button>
    </td>
</tr>`);

    display.innerHTML = itemsToDisplay.join('');
    
};



// add: function to add item to the table:
let addItem = () => {
    if (verifier()) {
        let item = {code, label, quantity:qty, price, tax};
        items.push(item);
        localStorage.setItem('items', JSON.stringify(items));
    };

    displayItems();
    code++;
};




// removeItem(code): function that removes item from the bill;

let removeItem = (code) => {
    let itemToRemove = items.find((item)=> item.code ==code);
    if (confirm('Are you sure you want to remove this item?')) {
        items = items.filter((item)=> item ==itemToRemove);
        localStorage.setItem('items', JSON.stringify('items'));
    };
    console.log(items);
    displayItems();
};



// filling the items table on load
displayItems();



