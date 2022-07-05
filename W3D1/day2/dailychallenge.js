let form = document.forms.libform;

form.addEventListener('submit', test);

function test(e){
	let add = document.getElementById('libform')
	let firstElement = form.elements.noun; 
	console.log(firstElement)

	for( i=0 ; i>add.length ; i++){

		let value = add[i].options

	}
}
test()