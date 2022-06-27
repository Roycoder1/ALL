// Exercise1:

let x = 5;
let y = 2;

if (x>y) {
	console.log('X is the biggest number');
}
else if (x<y)
{
	console.log('Error');
}

// Exercise 2:

// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’



let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())

if (newDog==='Chihuahua')
{
	console.log("I love Chihuahuas, it’s my favorite dog breed’")
}
else
{
	console.log("I dont care, I prefer cats")
}

// Exercise3:

let number = prompt("Give me a number",12);

if (number % 2 == 0) {
	console.log("x is an even number")}

	else if (number%2!==0)
	{
		console.log("x is an odd number")
	}

// Exercise 4 : Group chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let name_user1= "Lea123";
let name_user2 = "Princess45";
let user=prompt("How much users?")

if (user ==0) {
	console.log("no one is online");
}
else if (user == 1) 
{
	console.log( name_user1 + "is online")
}
else if (user==2)
{
	console.log(`${name_user1}, ${name_user2} "are online"`)
}
else if (user>2)
{
	console.log(`${name_user1} ${name_user2} "and 3 more are online"`)
}
