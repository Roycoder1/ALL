let listTasks = []

function getValue(event){
	event.preventDefault()
	console.log('jjjjj')
	let input = document.querySelector('input');
	console.log(input.value)



	if (input.value=='') {
		console.log(input.value)
		alert('this value is empty')


	}
	else{
		input = input.value;
		
		listTasks.push(input)
		
		let lists = document.querySelector('.listTasks')
		
		// let text = listTasks.toString()
		




		let createDiv = document.createElement('div')
		let create = document.createElement('input');
		create.setAttribute('type', 'checkbox')
		// create.classList ='fa-solid fa-x';
		createDiv.innerText = ' X  '+ input
		console.log(createDiv)
		lists.appendChild(createDiv)
		lists.appendChild(create)
		console.log(lists)

	}
}




