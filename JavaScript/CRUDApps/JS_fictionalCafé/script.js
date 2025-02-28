// 1. id="drinks" - <div> (Drinks section container)
// 2. id="drink1" - <select> (Dropdown for selecting Drink 1)
// 3. id="dPrice1" - <input> (Price input for Drink 1)
// 4. id="dQuantity1" - <input> (Quantity input for Drink 1)
// 5. id="drink2" - <select> (Dropdown for selecting Drink 2)
// 6. id="dPrice2" - <input> (Price input for Drink 2)
// 7. id="dQuantity2" - <input> (Quantity input for Drink 2)
// 8. id="drink3" - <select> (Dropdown for selecting Drink 3)
// 9. id="dPrice3" - <input> (Price input for Drink 3)
// 10. id="dQuantity3" - <input> (Quantity input for Drink 3)
// 11. id="pastries" - <div> (Pastries section container)
// 12. id="pastry1" - <select> (Dropdown for selecting Pastry 1)
// 13. id="pPrice1" - <input> (Price input for Pastry 1)
// 14. id="pQuantity1" - <input> (Quantity input for Pastry 1)
// 15. id="pastry2" - <select> (Dropdown for selecting Pastry 2)
// 16. id="pPrice2" - <input> (Price input for Pastry 2)
// 17. id="pQuantity2" - <input> (Quantity input for Pastry 2)
// 18. id="pastry3" - <select> (Dropdown for selecting Pastry 3)
// 19. id="pPrice3" - <input> (Price input for Pastry 3)
// 20. id="pQuantity3" - <input> (Quantity input for Pastry 3)
// 21. id="dTotal" - <input> (Total price input for Drinks)
// 22. id="pTotal" - <input> (Total price input for Pastries)


let drinksMenu = [
    { name: "Mana Latte", price: 5.50 },
    { name: "Shadow Mocha", price: 6.00 },
    { name: "Dungeon Brew", price: 4.00 },
    { name: 4.50 },
    { name: "Gatekeeper's Cold Brew", price: 5.00 },
    { name: "Phoenix Revival Tea", price: 4.50 },
    { name: "Ice Elf Iced Tea", price: 4.50 },
    { name: "Archmage's Chamomile", price: 4.00 },
];

let pastriesMenu = [
    { name: "Hunter's Doughnut", price: 3.50 },
    { name: "Gatekeeper's Cheesecake", price: 5.00 },
    { name: "Mana Crystal Cookies", price: 2.50 },
    { name: "Shadow Swirl Brownie", price: 4.50 },
    { name: "Beast Core Macarons", price: 3.00 },
];

//  selects for drinks
let drink1 = document.querySelector("#drink1");
let drink2 = document.querySelector("#drink2");
let drink3 = document.querySelector("#drink3");

//  selects for pastries
let pastry1 = document.querySelector("#pastry1");
let pastry2 = document.querySelector("#pastry2");
let pastry3 = document.querySelector("#pastry3");

// prices for drinks
let dPrice1 = document.querySelector("#dPrice1");
let dPrice2 = document.querySelector("#dPrice2");
let dPrice3 = document.querySelector("#dPrice3");

// prices for pastries
let pPrice1 = document.querySelector("#pPrice1");   
let pPrice2 = document.querySelector("#pPrice2");
let pPrice3 = document.querySelector("#pPrice3");

