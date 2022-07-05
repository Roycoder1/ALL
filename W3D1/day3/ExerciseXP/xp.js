// function call (){


// 	let id = setTimeout(function (){
// 		alert('Hello World')
// 		let p = document.createElement('p');
// 		p.innerText = 'Hello WORLD'
// 		let container = document.getElementById('container');
// 		container.appendChild(p)
// 	},2000)

// }
// call()


// let id ;

// function repetition (){
// 	let count = 0
// 	id = setInterval(function(){
// 		let p = document.createElement('p');
// 		p.innerText = 'Hello WORLD'
// 		let container = document.getElementById('container');
// 		container.appendChild(p)
// 		count++
// 		if (count>3) {
// 			_clear();

// 		}

// 	},2000)

// }


// repetition()



// function _clear (){


// 	clearInterval(id)
// }
// Exercise 2 :

// function s (data){
// 	console.log(data)
// }

// function myMove(){
// 	let box = document.getElementById('animate');
// 	let container = document.getElementById('container')
// 	let pos = 0;
// 	let id = setInterval(function(){
// 		if (pos ==350){
// 			clearInterval(id)
// 		}
// 		else {
// 			pos++
// 			box.style.left = pos+'px';

// 		}
// 	},5)

// }

// Exercise 3 :


let elem =document.getElementById('box')
elem.addEventListener('dragend', function(event){

	let x = event.clientX
	let y = event.clientY;
	elem.style.left = x+'px';
	elem.style.top = y+'px';
	console.log(x,y)

})





