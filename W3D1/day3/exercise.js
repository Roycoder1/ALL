
function start(){
	let box = document.getElementById('inner');
	let pos = 0;
	let id = setInterval(function(){
		if (pos ==350){
			clearInterval(id)
		}
		else {
			pos++
			box.style.left = pos+'px';

		}
	},5)
	
}
function x(){
	let box = document.getElementById('inner');
	let pos = 0;
	let move = start()
	let id = setInterval(function(){
		if (pos ==350){
			clearInterval(id)
		}
		else {
			pos++
			box.style.top = pos+'px';

		}
	},5)
}