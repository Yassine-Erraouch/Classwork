// products list
const products = [
    {
        id: 1,
        name: "MacBook Pro 16-inch",
        price: 2399,
        category: "Laptops",
        brand: "Apple",
        description: "16-inch MacBook Pro with M2 Pro chip, 16GB RAM, 1TB SSD",
        specs: ["M2 Pro Chip", "16GB Unified Memory", "1TB SSD Storage", "16-core GPU", "16.2-inch Liquid Retina XDR Display"],
        rating: 4.8,
        stock: 15,
        image: "https://example.com/images/macbook-pro-16.jpg"
    },
    {
        id: 2,
        name: "Sony WH-1000XM5",
        price: 349,
        category: "Headphones",
        brand: "Sony",
        description: "Industry-leading noise canceling with 30-hour battery life",
        specs: ["Active Noise Cancellation", "30-hour battery", "Touch controls", "Built-in Alexa", "Quick charging"],
        rating: 4.7,
        stock: 42,
        image: "https://example.com/images/sony-wh-1000xm5.jpg"
    },
    {
        id: 3,
        name: "iPhone 14 Pro",
        price: 999,
        category: "Phones",
        brand: "Apple",
        description: "iPhone 14 Pro with Dynamic Island, Always-On display, and Pro camera system",
        specs: ["A16 Bionic chip", "Pro camera system", "Dynamic Island", "Always-On display", "Emergency SOS via satellite"],
        rating: 4.6,
        stock: 28,
        image: "https://example.com/images/iphone-14-pro.jpg"
    },
    {
        id: 4,
        name: "Samsung Galaxy Watch 5",
        price: 279,
        category: "Watches",
        brand: "Samsung",
        description: "Advanced health monitoring with improved battery life",
        specs: ["BioActive Sensor", "Sleep coaching", "13% larger battery", "Sapphire crystal glass", "IP68 water resistance"],
        rating: 4.4,
        stock: 37,
        image: "https://example.com/images/galaxy-watch-5.jpg"
    },
    {
        id: 5,
        name: "iPad Air",
        price: 599,
        category: "Tablets",
        brand: "Apple",
        description: "Powerful. Colorful. Wonderful. With M1 chip and all-day battery life",
        specs: ["M1 chip", "10.9-inch Liquid Retina display", "5G capable", "12MP Ultra Wide front camera", "Touch ID"],
        rating: 4.5,
        stock: 19,
        image: "https://example.com/images/ipad-air.jpg"
    },
    {
        id: 6,
        name: "Canon EOS R6",
        price: 2499,
        category: "Cameras",
        brand: "Canon",
        description: "Full-frame mirrorless camera with advanced autofocus and image stabilization",
        specs: ["20.1MP Full-Frame CMOS Sensor", "DIGIC X Image Processor", "4K 60p Video Recording", "In-Body Image Stabilization", "12 fps Mechanical Shutter"],
        rating: 4.7,
        stock: 8,  
        image: "https://example.com/images/canon-eos-r6.jpg"
    },
    {
        id: 7,
        name: "PlayStation 5",
        price: 499,
        category: "Gaming",
        brand: "Sony",
        description: "Next-gen gaming console with ultra-high speed SSD and immersive gameplay",
        specs: ["Ultra-High Speed SSD", "Integrated I/O", "Ray Tracing", "4K 120fps support", "HDR technology"],
        rating: 4.8,
        stock: 12,
        image: "https://example.com/images/ps5.jpg"
    },
    {
        id: 8,
        name: "Dell XPS 13",
        price: 1299,
        category: "Laptops",
        brand: "Dell",
        description: "13.4-inch laptop with InfinityEdge display and 11th Gen Intel processors",
        specs: ["11th Gen Intel Core i7", "16GB RAM", "512GB SSD", "13.4-inch FHD+ Display", "Thunderbolt 4"],
        rating: 4.5,
        stock: 23,
        image: "https://example.com/images/dell-xps-13.jpg"
    },
    {
        id: 9,
        name: "Bose QuietComfort Earbuds",
        price: 279,
        category: "Headphones",
        brand: "Bose",
        description: "World-class noise canceling true wireless earbuds",
        specs: ["Noise Cancelling", "6 hours battery", "Wireless charging", "IPX4 rating", "Bluetooth 5.1"],
        rating: 4.4,
        stock: 31,
        image: "https://example.com/images/bose-qc-earbuds.jpg"
    },
    {
        id: 10,
        name: "Samsung Galaxy S23 Ultra",
        price: 1199,
        category: "Phones",
        brand: "Samsung",
        description: "Ultimate smartphone with 200MP camera and S Pen integration",
        specs: ["200MP camera", "S Pen included", "Snapdragon 8 Gen 2", "5000mAh battery", "120Hz Dynamic AMOLED 2X"],
        rating: 4.6,
        stock: 17,
        image: "https://example.com/images/galaxy-s23-ultra.jpg"
    }
];


// fucntion to display the products
function displayProducts(products) {
    let productsList = products.map(product => `
        <div class="col-md-6 col-lg-4">
                        <div class="card product-card h-100">
                            <div class="product-image">
                                <img src="${product.image}" class="card-img-top" alt="${product.name}">
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">${product.name}</h5>
                                <p class="card-text text-success fw-bold">$${product.price}</p>
                                <button class="btn btn-primary w-100 add-to-cart" data-id="2">
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>`)
}
