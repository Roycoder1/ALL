
// Exercise 1:

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
let b = fruits.sort();
console.log(b);
fruits.push("kiwi");
console.log(fruits);
fruits.splice(0,1);
console.log(fruits)
fruits.reverse()
console.log(fruits)

// Exercise 2: 

let moreFruits = ["Banana", 
[
"Apples", 
["Oranges"],
"Blueberries"
]
];
let oranges = moreFruits[1][1][0];
console.log(oranges);