let color_col = 3;
let color_row = 8;
let color_count = color_col * color_row;

let main_col = 60;
let main_row = 50;
let main_count = main_col * main_row;
let color;
let row;
let clear_ = document.getElementById('clear_')
let mouseDown ;
document.body.addEventListener('mousedown', function(){
	mouseDown= true
})
document.body.addEventListener('mouseup', function(){
	mouseDown= false
})


let sidebar = document.getElementById('sidebar');
let main = document.querySelector('#main');

for (let i = 0; i < color_count; i++) {
	let div = document.createElement('div');
	div.style.backgroundColor = generateRandomColor();
	sidebar.appendChild(div);
	div.addEventListener('click',function() {
		color= div.style.backgroundColor;
		console.log(color)

	})
	
	
}

for (var i = 0; i < main_count; i++) {
	let div = document.createElement('div');
	main.appendChild(div);

	div.addEventListener('mouseover', function(){
		

		if (mouseDown) {
			div.style.backgroundColor = color;
		}


		clear_.addEventListener('click', function(){
			div.style.backgroundColor = 'darkgrey';
		})
	})

	// if(color !== div){
	// 	div.addEventListener('change', function(){
	// 		let colors = color
}




function generateRandomColor(){
	let letters = '0123456789ABCDEF'
	let color = '#';
	for (let i = 0; i < 6; i++) {
		color += letters[Math.floor(Math.random()*16)]
	}
	return color;
}

// function clear(){

// 	console.log(clear_)
// 	let main = document.getElementById("main")
// 	clear_.addEventListener('click', function(){


// 		main.style.backgroundColor = 'darkgrey'
// 	})


// }
// clear()






