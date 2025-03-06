document.addEventListener('DOMContentLoaded', async () => {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const products = await fetchProducts();
    
    // Initialize
    renderProducts(products);
    updateCartBadge();

    // Event Listeners
    document.querySelectorAll('[data-category]').forEach(btn => {
        btn.addEventListener('click', () => filterProducts(btn.dataset.category, products));
    });

    document.getElementById('searchInput').addEventListener('input', (e) => {
        searchProducts(e.target.value, products);
    });

    document.getElementById('cartButton').addEventListener('click', () => {
        window.location.href = 'cart.html';
    });
});

async function fetchProducts() {
    try {
        const response = await fetch('products.json');
        return await response.json();
    } catch (error) {
        console.error('Error fetching products:', error);
        return [];
    }
}

function renderProducts(products, filterCategory = 'all') {
    const container = document.getElementById('productsContainer');
    container.innerHTML = '';

    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'col-md-4 col-lg-3';
        card.innerHTML = `
            <div class="card product-card h-100">
                <img src="${product.image}" class="card-img-top" alt="${product.title}">
                <div class="card-body">
                    <h5 class="card-title">${product.title}</h5>
                    <p class="card-text">$${product.price}</p>
                    <button class="btn btn-primary add-to-cart" data-id="${product.id}">Add to Cart</button>
                </div>
            </div>
        `;
        
        card.querySelector('.add-to-cart').addEventListener('click', () => addToCart(product.id));
        container.appendChild(card);
    });
}

function filterProducts(category, products) {
    document.querySelectorAll('[data-category]').forEach(btn => 
        btn.classList.toggle('active', btn.dataset.category === category));
    
    const filtered = category === 'all' 
        ? products 
        : products.filter(p => p.category === category);
    
    renderProducts(filtered);
}

function searchProducts(query, products) {
    const filtered = products.filter(p => 
        p.title.toLowerCase().includes(query.toLowerCase())
    );
    renderProducts(filtered);
}

function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    if (!cart.includes(productId)) {
        cart.push(productId);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartBadge();
    }
}

function updateCartBadge() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    document.getElementById('cartBadge').textContent = cart.length;
}