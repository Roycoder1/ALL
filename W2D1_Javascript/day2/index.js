// let user = prompt('How old are you?',20)

// if (user < 18)
// {
// 	console.log(alert('Sorry, you are too young to drive this car. Powering off'));
// }
// else if (user == 18)
// {
// 	console.log(alert("Congratulations on your first year of driving. Enjoy the ride!"));
// }
// else 
// {
// 	console.log(alert("Powering On. Enjoy the ride!"));
// }


// let fruit = 'Papayas';

// switch (fruit) {
// 	case 'Oranges':
// 	console.log('Oranges are $0.59 a pound.');
// 	break;
// 	default:
// 	console.log('Sorry, we are out of ' + fruit + '.');
// 	break;
// 	case 'Mangoes':
// 	case 'Papayas':
// 	console.log('Mangoes and papayas are $2.79 a pound.');
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
// }

// (a===b) ? console.log('yes'):console.log('no');


// write a function with switch
// let page = 'Home'
// switch(page){
// case 'Home'
// console.log('Home')
// break;
// case 'About'
// console.log('about')
// break;
// default:
// console.log('404 page')
// }



// let a = 2 + 2;

// switch (a) {
// 	case 3:
// 	alert( 'Too small' );
// 	break;
// 	case 4:
// 	alert( 'Exactly!' );
// 	break;
// 	case 5:
// 	alert( 'Too large' );
// 	break;
// 	default:
// 	alert( "I don't know such values" );
// }
// prediction: Exactly
// results:

// let a = 2 + 2;

// switch (a) {
// 	case 4:
// 	alert('Right!');
// 	break;

//   case 3: // (*) grouped two cases
//   case 5:
//   alert('Wrong!');
//   alert("Why don't you take a math class?");
//   break;

//   default:
//   alert('The result is strange. Really.');
//     // prediction : Right;
//     // results: Right;
// }

// let arr = [2,4,5,6]
// let obj = {
// 	name: 'John',
// 	lastname: 'Miller',
// 	age: 24,
// 	single: true,
// 	address: {
// 		street: 'Bezalel',
// 		num: 4,
// 		city: 'Ramat Gan',
// 		zipcode: {
// 			num: 879865
// 		}
// 	},
// 	fav: ['banana','kiwi','orange'],
// 	tv:[
// 	{name:'friend'},
// 	{name:'breaking bad'},
// 	{name:'starnger things'}
// 	]
// }
// console.log(obj.tv[1].name);
// // console.log(obj.fav[1]);
// // console.log(obj.address.zipcode.num);
// // console.log(obj.lastname);
// // console.log(obj[“lastname”]);
// // console.log(obj.single);

// Exercise 1: object
// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".



// 1.
let obj = {
	username: 'asdf',
	password: 'qwerty1',
}
let database = [obj];
let newsfeed = [
{username:'one', timeline:'t1'},
{username:'two', timeline:'t2'},
{username:'three', timeline:'t3'}
]
console.log(database[0].password);
console.log(newsfeed[2].timeline);







