let person = ['john','marie','lise'];

for( let i = 0; i < person.length; i++ )
{
	person[i]=person[i].charAt(0).toUpperCase()+person[i].slice(1);
	
}
console.log(person)



for(let i of person){
	i=i.charAt(0).toUpperCase()+i.slice(1);
}
console.log(person)






for( let i = 0; i < person.length; i++){
	if (person[i]=="lise") {
		console.log("Bonjour Lise")
	}
	else if (person[i]=="John") {
		console.log("Bonjour John")
	}
	else{
		console.log("Bonjour Marie")
	}
}


