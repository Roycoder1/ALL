function sendData(event){
	event.preventDefault();
	// let username = document.forms[0].elements.username.value;
	let username = document.getElementById('username').value;
	let password = document.forms.form1.elements.password.value
	console.log(username,password)
}
// .trim()= verifie si l input est vide