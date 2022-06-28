// Exercise1:

let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people);
let index= people.indexOf("James");
people[index]="Jason"
console.log(people);
people.push("Roy");
console.log(people);
console.log(people.indexOf("Mary"));

console.log(people.slice(1,3));
console.log(people.indexOf("Foo"))
// Outside of the array
let last=people.push('Adam');
console.log(people)

// Part II:
for(let i=0;i<4;i++)
	console.log(people[i]);

for(let i = 0;i<4;i++){


	if (people[i]=="Jason") {
		
		console.log(people[i]);
		break;
	}

	console.log(people[i]);}

	// Exercise 2:

	let colors = ['blue','orange','red','black','green'];
	

	for(let i=0;i<5;i++)
		console.log(`My #${i+1} choice is ${colors[i]}`)

	let suffix =['st','nd','rd','th','th']



	for(let i=0;i<5;i++)
		console.log(`My ${i+1}${suffix[i]} choice is ${colors[i]}`)

// Exercise 3:

let user= prompt("Choose a number please over 10");
let type = typeof(Number(user));
user = Number(user);

console.log((type));


while(user < 10){
	user = prompt('Type another number over 10');
	user= Number(user);
}


// Exercise 4:

let building = {
	numberOfFloors : 4,
	numberOfAptByFloor : {
		firstFloor : 3,
		secondFloor : 4,
		thirdFloor : 9,
		fourthFloor : 2,
	},
	nameOfTenants : ["Sarah", "Dan", "David"],
	numberOfRoomsAndRent:  {
		sarah: [3, 990],
		dan :  [4, 1000],
		david : [1, 500],
	},
}
console.log(building.numberOfFloors);

console.log(building.numberOfAptByFloor.firstFloor);

console.log(building.numberOfAptByFloor.thirdFloor);

console.log(building.nameOfTenants[1]);
console.log(building.numberOfRoomsAndRent.dan);

let sumSarah= building.numberOfRoomsAndRent.sarah[1];
let sumDavid =building.numberOfRoomsAndRent.david[1];
let sumDan = building.numberOfRoomsAndRent.dan[1];
console.log(sumSarah);
console.log(sumDavid);

if (sumSarah || sumDavid > sumDan ) {
	console.log(sumDan+200);
}

// Exercise 5:

let obj = {

	brother : 'Yaniv',
	key: 'yes',
	value1 : 1 ,

	mother : 'Carmel',
	key1 :'no',
	value2 : 2,

	father : 'Guernica',
	key2: 'maybe',
	value3 :3,
};

for (x in obj){
	console.log(x)
	console.log(obj[x]);
}

// Exercice 6 :

let details = {
	my: 'name',
	is: 'Rudolf',
	the: 'raindeer'
}
for(x in details){
	let details1 = details.toString
	console.log(x,details[x]);
}

// Exercise 7:

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let a = names.sort();
console.log(a);
let b = a.slice([0],[5]);


console.log(b)















