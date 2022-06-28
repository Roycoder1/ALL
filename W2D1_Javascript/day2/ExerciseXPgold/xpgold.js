// Exercise 1 : The World Translator

let languages= prompt('Which languages do you speak?')

languages= languages.toLowerCase()
console.log(languages)

let french = "Bonjour";
let english = "Hello";
let Hebrew = "Shalom";

switch(languages)
{
	case 'french':
	alert('Bonjour');
	break;

	case "english":
	alert("Hello");
	break;

	case "hebrew":
	alert("Shalom")
	break;

	default:
	alert("01110011 01101111 01110010 01110010 01111001")
}

// Exercise 2:

let grade= prompt('Which is your grade?');

if (grade>90) {
	console.log("A")
}
else if (grade>80&&90) {
	console.log("B")
}
else if (grade>=70&&80) {
	console.log("C")
}
else if (grade<70)
{
	console.log("D")
}

// Exercise 3: Verbing

// Prompt the user for a string. It must be a verb.
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
// If the length of the string is less than 3, leave it unchanged.


let verb = prompt("enter a verb");
let verb1 = verb.indexOf('ing');
let var1= verb.substring(verb.length-3,verb.length)
console.log(verb.length)

if (verb.length>=3 && var1!=='ing') {
	console.log (verb+'ing');

}
else if (verb.length>3 && var1=='ing') {
	console.log(verb+'ly');
}
else if (verb.length<3) {


	console.log(verb)
}





