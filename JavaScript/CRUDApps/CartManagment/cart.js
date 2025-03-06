document.addEventListener('DOMContentLoaded', async () => {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const products = await fetchProducts();
    const cartItems = products.filter(p => cart.includes(p.id));
    
    renderCartItems(cartItems);
    calculateTotal(cartItems);
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

function renderCartItems(items) {
    const container = document.getElementById('cartItems');
    container.innerHTML = '';

    items.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <img src="${item.image}" alt="${item.title}">
                ${item.title}
            </td>
            <td>$${item.price}</td>
            <td>1</td>
            <td>$${item.price}</td>
            <td>
                <button class="btn btn-danger btn-sm" onclick="remove()">Remove</button>
            </td>
        `;
        container.appendChild(row);
    });
}

function calculateTotal(items) {
    const total = items.reduce((sum, item) => sum + item.price, 0);
    document.getElementById('cartTotal').textContent = `$${total}`;
}