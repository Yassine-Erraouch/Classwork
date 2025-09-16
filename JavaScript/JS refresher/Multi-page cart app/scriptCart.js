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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmckups.com%2Fwp-content%2Fuploads%2F2023%2F04%2Fimage-21.png&f=1&nofb=1&ipt=0463f68da651166c8ccfcdf1c57c3abc6899d2d0ee95d2835a71595a81b876cf"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpng.pngtree.com%2Fpng-vector%2F20240315%2Fourmid%2Fpngtree-isolated-of-sony-wh-1000xm5-wireless-headphones-front-view-featuring-a-png-image_11941302.png&f=1&nofb=1&ipt=2744ad76bd958011e5656fa7e04cb0b3129cdbf9878884e63fe2ca5a35270791"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F55%2F65%2Fde%2F5565def9af4efaa522def9bd4898e145.jpg&f=1&nofb=1&ipt=2c2453fe17f0194721836f57e534a4975b45e3390d25562e9016f7c578ba0717"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71E8iEWXY9L.jpg&f=1&nofb=1&ipt=24dd39733908f2d2aa6176e0ba45dc27f54d9de3139f9aa3c655f2e340edf8d2"
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
        image: "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/ipad-air-select-wifi-blue-202203?wid=470&hei=556&fmt=png-alpha&.v=1645066726182"
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
        image: "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi1.adis.ws%2Fi%2Fcanon%2Feos-r6-mark-ii_frt_range-module_95730d11ef3948d5bfc4b6276520600c&f=1&nofb=1&ipt=6fdba8875ed1a81c2c9181dd07f30b2817b77bd2e3b6e01019ac7da44911644d"
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
        image: "https://m.media-amazon.com/images/I/619BkvKW35L._AC_SL1500_.jpg"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic1.xdaimages.com%2Fwordpress%2Fwp-content%2Fuploads%2F2024%2F01%2Fdell-xps-16-1.png&f=1&nofb=1&ipt=27b11e3351ce93e5914133fdcdadff296db4aae0438d7c6ff096b1686c6be683"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fassets.bose.com%2Fcontent%2Fdam%2FBose_DAM%2FWeb%2Fconsumer_electronics%2Fglobal%2Fproducts%2Fheadphones%2Fqc_earbuds%2Fsilo_images%2Fv2%2FQCEB_PDP_Ecom-Gallery-B04.jpg%2Fjcr%3Acontent%2Frenditions%2Fcq5dam.web.1920.1920.jpeg&f=1&nofb=1&ipt=49f42533369d5032f79eb6735208e3ae1678d49c452d58f1c3800f5837719842"
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
        image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F035%2F572%2F095%2Foriginal%2Fsamsung-galaxy-s23-ultra-black-transparent-image-free-png.png&f=1&nofb=1&ipt=881715c6fb38f38839e98aa27be04c6e07b1b93a736b77a5a6476182492572c1"
    }
];


let cartItems = localStorage.getItem('cartItems') ? JSON.parse(localStorage.getItem('cartItems')) : [];

// function to display products

function displayProducts(products) {
    let productsList = '';
    products.forEach(prod => {
        productsList += `
            <div class="col-md-6 col-lg-4">
                <div class="card product-card h-100">
                    <div class="product-image">
                        <img src="${prod.image}" class="card-img-top w-50 m-2 object-fit-contain " alt="${prod.name}">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">${prod.name}</h5>
                        <p class="card-text text-success fw-bold">$${prod.price}</p>
                        <button class="btn btn-primary w-100 add-to-cart" data-id="${prod.id}" onclick="addToCart(${prod.id})">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>
        `;
    });
    document.getElementById('products-list').innerHTML = productsList;
}
displayProducts(products);


// function to add product to cart
function addToCart(prodId) {
    const product = products.find(p => p.id === prodId);

    if (!cartItems.includes(product)) {
        cartItems.push(product);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        alert(`${product.name} has been added to your cart.`);
    } else {
        cartItems.product.quantity += 1;
    }
}



// function to display filter radio buttons for categories
function displayFilters() {
    const categories = [...new Set(products.map(prod => prod.category))];
    let filtersList = '<div class="form-check"><input class="form-check-input" type="radio" name="category" id="all" value="All" checked><label class="form-check-label" for="all">All</label></div>';
    document.querySelector('#categories').innerHTML = filtersList + categories.map(cat => `
        <div class="form-check">
            <input type="radio" class="form-check-input border-1 border-secondary" name="category" id=${cat} value="${cat}">
            <label class="form-check-label" for="${cat}">${cat}</label>
        </div>`).join('');
    
}

function filterProducts() {
    const selectedCategory = document.querySelector('input[name="category"]:checked').value;
    if (selectedCategory === 'All') {
        displayProducts(products);
    } else {
        const filteredProducts = products.filter(prod => prod.category === selectedCategory);
        displayProducts(filteredProducts);
    }
}


displayFilters();