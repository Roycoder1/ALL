// 1.Prompt the user for a number to begin counting down bottles.

// function user (){
// 	let user= prompt('Choose a number');
// 	let userNumber=Number(user)
// 	// let substraction = substraction();
// 	substraction(user,userNumber)
// 	// console.log(user)
// }
// user()


// function substraction (user,userNumber){

// 	let bottle =userNumber;
// 	let sum =0;
// 	let addition = sum+1;
// 	let down = bottle+sum-1;

// 	text(bottle,sum,addition,down)

// 	// console.log(bottle)
// 	// console.log(sum)
// 	// console.log(addition)
// 	// console.log(down)
// }
// substraction()
// // console.log(substraction)




// function text (bottle,sum,addition,down){


// 	let text= bottle + 'bottle of beer on the wall'+bottle +'bottles of beer'+'Take' +addition +'down, pass it around'+down + 'bottles of beer on the wall';



// 	// console.log(bottle + 'bottle of beer on the wall')
// 	// console.log(bottle +'bottles of beer');
// 	// console.log	('Take' +addition +'down, pass it around');
// 	// console.log(down + 'bottles of beer on the wall');
// 	// console.log(text)
// 	// console.log(bottle)
// 	// console.log(sum)
// 	// console.log(addition)
// 	// console.log(down)



// 	while(1==1 ){  if (bottle > 0  ) {

// 		console.log(bottle + 'bottle of beer on the wall')
// 		console.log(bottle +'bottles of beer');
// 		console.log	('Take' +addition +'down, pass it around');
// 		console.log(down + 'bottles of beer on the wall');

// 		bottle++
// 		break;
// 	}
// 	else if (bottle=0) {

// 		console.log('no bottle of beer on the wall');
// 		break
// 	}
// }
// }
// // console.log(text);
// text()

function bottles(){
	let count = prompt('Choose a number');
	let user = Number(count);
	let sum = 0;
	let add = 1;
	let mini = user-1;


	for (i = 99; i >= 1; i--) {

		if (count==99) {
			console.log(Number(count) + 'bottle of beer on the wall')
			console.log(Number(count) +'bottles of beer');
			console.log	('Take' +Number(add)+'down, pass it around');
			console.log(Number(count)- Number(add) + 'bottles of beer on the wall');
			count=count-1;
			add=add+1;

		}



		if (count<99 ) {

			console.log(Number(count)-Number(add) + 'bottle of beer on the wall')
			console.log(Number(count)- Number(add) +'bottles of beer');
			console.log	('Take' + Number(add) +'down, pass it around');
			console.log(Number(count)- Number(add) + 'bottles of beer on the wall');
			count=count-1;
			add=add+1;


			if (count==0) { 
				console.log('no bottle of beer on the wall');}


				else if (Number(count)- Number(add)<0) { 
					console.log('no bottle of beer on the wall')
					return

				}




			}	

			else {
				break;
			}
		}
	}


	bottles()









