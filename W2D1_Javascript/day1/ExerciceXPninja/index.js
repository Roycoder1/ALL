 5 >= 1
 // prediction:true
 // results:true
 console.log(5 >= 1)


 0 === 1

 // prediction:false
 // results:false
 console.log( 0 === 1)


 4 <= 1

 // prediction:false
 // results:false
 console.log(4 <= 1)

 1 != 1

 // prediction:false
 // results:false
 console.log(1 != 1)

 "A" > "B"

 // prediction:undefined
 // results:false
 console.log("A" > "B")

 "B" < "C"

 // prediction:undefined
 // results:true
 console.log("B" < "C")

 "a" > "A"

 // prediction:Nan
 // results:true
 console.log("a" > "A")

 "b" < "A"

 // prediction:undefined
 // results:false
 console.log("b" < "A")

 true === 
 false
 // prediction:false
 // results:false
 console.log(true === 
    false)

 true != true
 // prediction:false
 // results:false
 console.log(true != true)

 // exercice2:(finir demain)

 // let num1 =prompt('enter a string of number separated by commas,please');
 
 // let tab=num1.toLocaleString();
 // console.log(tab)

// exercice3:

// let nemo=prompt("Veuillez saisir une phrase avec Nemo", "J'aime le monde de Nemo");
// let nemo1=nemo.search("Nemo");
// let positionNemo= 7;

// if  (nemo=nemo1){
//    console.log(`I found Nemo at ${positionNemo}`)
// }
// else {
//    console.log(`There is no Nemo`)
// }
// correction:

let str = prompt('Please find my Nemo ?');

let arr = str.split(' ');
console.log(arr.indexOf('Nemo'));
// let start = str.indexOf('Nemo');

// console.log(str);
// console.log(start);
// console.log(start+4);
// console.log(str.substring(start,start+4));
//
// str = str.substring(start+5,str.length);
// console.log(str);
// start = str.indexOf('Nemo');
// console.log(str.substring(start,start+4));
//
// str = str.substring(start+5,str.length);
// console.log(str);
// start = str.indexOf('Nemo');
// console.log(str.substring(start,start+4));

//My Nemo is sleeping













