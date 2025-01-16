class Produit:
    def __init__(self,code, name, price):
        self.product_code = code
        self.product_name = name
        self.price = price
    def __str__(self):
        return f'{self.product_code}-{self.product_name}-{self.price}'
    def __eq__(self,p):
        return p.product_code==self.product_code
    def afficher(self):
        print(f"{self.product_name}**{self.price}")



class Cart:
    def __init__(self):
        self.product_list = []
        
    
    # method to add product to cart
    def add_product(self, product):
        self.product_list.append(product)
        setattr(product, "quantity", 1)
    
    #method to remove product from cart
    def remove_product_from_cart(self, product):
        if product in self.product_list:
            index = self.product_list(product.product_code)
            self.product_list.remove(index)
        else:
            return f"the product is not in cart"
    
    # class to increment the quanitity of a product
    def increment_qte(self, product):
        if product in self.product_list:
            product.quantity += 1
        else:
            self.add_product(product)
    
    def decrement_qte(self, product):
        if product in self.product_list:
            if product.quantity > 0:
                product.quantity -= 1
            else:
                self.remove_product_from_cart(product)
        
    def total_amount(self):
        total = 0
        for product in self.product_list:
            total += product.price * product.quantity
        return total
    
    def __str__(self):
        cart_str = "Product Code | Product Name | Price | Quantity\n"
        for product in self.product_list:
            cart_str += f"{product.product_code}         | {product.product_name}| {product.price} | {product.quantity}\n"
        cart_str += f"Total: {self.total_amount()}"
        return cart_str
       
            
# creating some Product instances 
p1 = Produit("P001", "Apple iPhone", 999.99)
p2=  Produit("P002", "Samsung TV", 1299.99)
p3=  Produit("P003", "Nike Shoes", 79.99)
p4=  Produit("P004", "Sony Headphones", 149.99)
p5=  Produit("P005", "Canon Camera", 499.99)

print(p1)
print(p1 == p2)

# creating a Cart instance
cart = Cart()

# adding some items
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.add_product(p4)
cart.add_product(p5)

cart.increment_qte(p1)
cart.decrement_qte(p2)
cart.total_amount()
print(cart)