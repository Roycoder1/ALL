let listTasks = []

function getValue(){


	let input = document.querySelector('input')
	input.value
	console.log(input.value)



	if (input.value=='') {
		console.log(input.value)
		alert('this value is empty')


	}
	else{
		input = input.value;
		
		listTasks.push(input)
		
		let lists = document.querySelector('.listTasks')
		
		let text = listTasks.toString()
		




		let createDiv = document.createElement('div')
		let create = document.createElement('input');
		create.setAttribute('type', 'checkbox')
		// create.classList ='fa-solid fa-x';
		createDiv.innerText = ' X  '+ text
		console.log(createDiv)
		lists.appendChild(createDiv)
		lists.appendChild(create)
		console.log(lists)

	}
}

getValue()




