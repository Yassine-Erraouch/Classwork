// fucntion for displaying the info


// defining products outside the fetch function so i can use it outside the function
let products;

// function to fetch data from json file
const getData = async() => {
    let response = await fetch('products.json');
    products = await response.json();
    displayInfo(products);
}