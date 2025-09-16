// 1. Étant donné un tableau [1, 2, 3, 4], utilise map pour retourner [2, 4, 6, 8
let array1 = [1,2,3,4];
let mappedArray = array1.map(x=>x*2);
console.log(mappedArray)


// 2. À partir du tableau [1, 2, 3, 4, 5, 6], retourne uniquement les nombres pairs.

let numbers = [1,2,3,4,5,6];
let evenNumbers = numbers.filter(x=> x%2 === 0);
console.log(evenNumbers);

// 3. Calcule la somme des éléments du tableau [10, 20, 30, 40]
let numbers2 = [10,20,30,40];
let sum = numbers2.reduce((a,b)=> a+b,0);
console.log(sum);


// 4. Affiche chaque fruit du tableau ["pomme", "banane", "orange"].
let fruits = ["pomme", "banane", "orange"];
    // using the spread operator
console.log(...fruits);
    // using .join method
console.log(fruits.join(','))


// 5. Transforme chaque mot en majuscules dans le tableau ["react","javascript", "html"].
let words = ["react", "javascript", "html"];
let uppercaseWords = words.map(w=>w.toUpperCase());
console.log(uppercaseWords);


// // 6. À partir du tableau d’objets suivant : 
//         const users = [ 
            //              {name: "Alice", age: 25}, 
            //              {name: "Bob", age: 30}, 
            //             {name: "Charlie", age: 35} 
            //                                 ]; 
// Retourne seulement les prénoms : ["Alice", "Bob", "Charlie"]. 

const users = [ 
                {name: "Alice", age: 25}, 
                {name: "Bob", age: 30}, 
                {name: "Charlie", age: 35}
];

let names = users.map(u=>u.name);
console.log(names)

// 7. Trouve le premier nombre supérieur à 50 dans [10, 20, 60, 80].

let numbers3 = [10, 20, 60, 80];
console.log(numbers3.find(x=> x>50));

// 8. À partir du tableau [5, 12, 8, 130, 44], garde seulement les nombres > 10 et multiplie-les par 2.
let numbers4 = [5, 12, 8, 130, 44];
let finalNumbers= (numbers4.filter(x=> x>10)).map(x=>x*2);
console.log(finalNumbers);

// 9. Compte combien de fois chaque fruit apparaît dans le tableau : 
    //  const fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"];

const fruits2 = ["pomme", "banane", "pomme", "orange", "banane", "pomme"];

let counts = fruits2.reduce((acc,f)=> acc[f] = (acc[f] || 0) +1
                            return acc
                            , {});
console.log(counts);