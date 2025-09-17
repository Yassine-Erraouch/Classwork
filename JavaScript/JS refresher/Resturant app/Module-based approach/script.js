import {
    dishes,
    cart,
    categories,
    addToCart,
    saveCart,
    loadCart,
    removeDish,
    cartCount,
    updateTotal,
    increment,
    decrement,
    search
} from "./functions.js";

function loadDishes() {
    document.querySelector('#items-grid').innerHTML = dishes.map(dish => `
            <div class="col">
                <div class="card h-100">
                    <img src="${dish.image}" class="card-img-top" alt="${dish.name}" style="height: 200px; object-fit: cover;">
                    <div class="card-body">
                        <h5 class="card-title text-light">${dish.name}</h5>
                        <p class="card-text text-light">${dish.category}</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="text-light">$${dish.price.toFixed(2)}</span>
                        </div>
                        <button class="btn btn-gold w-100 mt-3" onclick="addToCart(${dish.id})">
                            <i class="fas fa-cart-plus me-1"></i> Add to Cart
                        </button>
                    </div>
                </div>
            </div>`).join('');

    cartCount();
    updateTotal();
}

loadDishes();