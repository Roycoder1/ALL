
function getValue(){


	let text = document.querySelector('input').value;
	console.log(text);
	let input= document.querySelector('input')
	

	let regex = /[^a-zA-Z0-9]/g
	let isValid =regex.test(text);


	if (!isValid) {

		return true;
	}
	else{
		text = text.replace(/[^a-zA-Z0-9]/g, '')
	}
	console.log('false')
}






// var name = name.replace(/[^a-zA-Z0-9 ]/g, "");




