



// for (let i = 0;i < 5,i++)
// {
// 	console.log(i)
// }

// Exercise 1:



// for(let i=0;i<16 ;i++){


// 	if (i %2==0 )

// 		console.log(i + " is even")
// 	else if (i%2!==0) 

// 		console.log( i + " is odd")
// }

let names= ["john", "sarah", 23, "Rudolf",34]

for( let i =0; i < names.length; i++){
	
	if (typeof names[i] !=="string") {
		continue;
	}

	else if (names[i].charAt(0) == names[i].charAt(0).toUpperCase()){
		console.log(names[i]);

	}
	else {

		names[i]= names[i].charAt(0).toUpperCase() + names[i].slice(1);
		console.log(names[i]);
	}

}

// 2.
for( let i =0; i < names.length; i++){
	if (typeof names[i] !=="string") {
		break;
	}
	else{
		console.log(names[i]);
	}
}


