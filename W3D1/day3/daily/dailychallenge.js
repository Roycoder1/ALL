
function getValue(){


	let text = document.querySelector('input').value;
	console.log(text);
	

	let regex = '/^[A-Za-z0-9 ]+$/';

	if (text.test(regex)== regex) {

		return true;
	}
	else{
		return false ; 
	}



}


// var name = name.replace(/[^a-zA-Z0-9 ]/g, "");




