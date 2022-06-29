// let infoAboutMe =()=>{

// 	let name = 'Roy';
// 	let familyName = 'Benisti';
// 	let age = 25;
// 	return name + familyName + age ;
// }
// console.log(infoAboutMe())

// // Part2:

// let infoAboutPerson =(personName, personAge, personFavoriteColor)=>{
// 	return 'Your name is '+ personName + 'you are ' + personAge + 'years old, your favorite color is'+ personFavoriteColor;
// }
// console.log(infoAboutPerson("David ", 45, " blue"));
// console.log(infoAboutPerson("Josh ", 12, " yellow"));

// // Exercise 2 :

// let calculateTip = ()=>{
// 	let john = prompt("enter the amount of the bill");
// 	let bill = Number(john)

// 	if (john<50) {
// 		return bill*1.2 ;
// 	}
// 	else if (john >50 && john<200){
// 		return bill*1.15;
// 	}
// 	else
// 	{
// 		return bill* 1.1;
// 	}

// }

// console.log(calculateTip())

// // Exercise 3 :

// let isDivisible = (x,y)=>{

// 	let sum =0;
// 	for(i = 0; i<=500; i++){
// 		if (i%23==0) {
// 			sum = sum + i;
// 			console.log(i)
// 		}
// 	}
// 	console.log("sum"+ sum)
// }

// isDivisible()

// let isDivisible1 = (x,y)=>{
// 	for(i = 0; i<=500; i++){
// 		if (i % x == 0 && i % y == 0) {
// 			console.log(i)
// 		}
// 	}
// }
// isDivisible1(3,45)



// Exercise4 :

// let stock = { 
// 	"banana": 6, 
// 	"apple": 0,
// 	"pear": 12,
// 	"orange": 32,
// 	"blueberry":1
// }  

// let prices = {    
// 	"banana": 4, 
// 	"apple": 2, 
// 	"pear": 1,
// 	"orange": 1.5,
// 	"blueberry":10
// } 

// let shoppingList= ['banana','orange','apple']


// let myBill= ()=>{
// 	let bill = 0;
// 	for(i of shoppingList){
// 		if (i in stock && stock[i]!==0){
// 			bill += prices[i];
// 			stock[-1];


// 		}
// 		else
// 			console.log('Sorry there is no stock')
// 	}

// 	return bill	
// }
// console.log(myBill())

// // Exercise 5 :

// let changeEnough=(itemPrice, amountOfChange)=>{
// 	let sum= 0;
// 	let change =[0.25,0.10,0.05,0.01];


// 	for(i = 0; i < 3 ; i++){
// 		let total=change[i]*amountOfChange[i];
// 		console.log(sum+=change[i]*amountOfChange[i]);

// 	}

// 	if(sum+=change[i]*amountOfChange[i]>=itemPrice){
// 		return true;
// 	}
// 	else{
// 		return false;
// 	}
// 	console.log(sum+=change[i]*amountOfChange[i]+sum);
// }

// console.log(changeEnough(4.25, [25, 20, 5, 0]));


// Exercise6 :

let hotelCost= (hotel)=>{
	let ask = prompt("How much night would you like to stay in the hotel?")
	let numb= Number(ask);
	let sum = 0
	console.log(typeof(ask));
	if (typeof(numb)=='number') {
		for(i=0; i<numb; i++)

			console.log(hotel);
		let total = sum+numb*hotel;
		console.log(total);

	}
	else{
		while(typeof(ask)!=='number');
		ask = prompt("How much night would you like to stay in the hotel?")
		return ask
	}
}
hotelCost(140)

// 2.

let planeRideCost = ()=>{
	let user = prompt('enter a destination','Dubai');
	let numb= Number(user);

	let destination = {
		London : 183+'$',
		Paris : 220+'$',
		All_other_destination: 300+'$',
	}
	let obj = Object.keys(destination);
	


	if (user ==obj[0]) {
		console.log(`London : ${destination.London}`)
	}

	else if (user==obj[1]) {
		console.log(`Paris : ${destination.Paris}`)
	}
	else
	{
		console.log(`Autre destination : ${destination.All_other_destination}`)
	}
}
planeRideCost()

// Exercise 3 :

let rentalCarCost = (rentCar)=>{
	let car = prompt('How much time would you like to rent the car?');
	let numb = Number(car);
	let sum1 = 0;
	let total = sum1+numb*rentCar;
	console.log(total);
	if (numb>10) {
		let discount = total * 0.95;
		console.log(discount);
	}


}



rentalCarCost(40);




let ask = prompt("How much night would you like to stay in the hotel?")
let numb= Number(ask);
let sum = 0
let total = sum+numb*140;
let user = prompt('enter a destination','Dubai');
let numb2= Number(user);
let car = prompt('How much time would you like to rent the car?');
let numb1 = Number(car);
let sum1 = 0;
let total1 = sum1+numb1*40;
let discount = total1 * 0.95;

let destination = {
	London : 183+'$',
	Paris : 220+'$',
	All_other_destination: 300+'$',
}


let totalVacationCost = (hotelCost,planeRideCost,rentalCarCost)=>{

	

	console.log(`The car cost ${hotelCost}the hotel cost${planeRideCost}the plane tickets cost ${rentalCarCost}`);
}
totalVacationCost(total1,total,destination.All_other_destination)


