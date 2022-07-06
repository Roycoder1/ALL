
function getValue(event){


	let text = document.querySelector('input');
	console.log(text);
	
	

	let regex = /[^a-zA-Z]/g
	let isValid =regex.test(text.value);
	console.log(isValid)

	if (isValid) {

		// event.target.value = event.target.value.slice(0,-1)
		text.value = text.value.replace(regex,"")


	}
	// if (!isValid) {

	// 	console.log('true')
	// }
	// else{
	// 	text = text.replace(/[^a-zA-Z0-9]/g, '')
	// 	console.log('false')
	// }
	
}






// var name = name.replace(/[^a-zA-Z0-9 ]/g, "");




