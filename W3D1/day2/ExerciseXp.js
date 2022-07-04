// // let retrieve = document.querySelector('h1');
// // console.log(retrieve)

// // let retrieveP = document.querySelector('article')
// // console.log(retrieveP)
// // let retrieveDef=document.querySelectorAll('p')[3]
// // retrieveP.removeChild(retrieveDef)

// // let red = document.querySelector('h2');
// // red.addEventListener('click', function(){
// // 	red.style.backgroundColor= 'red'
// // })

// // let hide = document.querySelector('h3');
// // hide.addEventListener('click', function(){
// // 	hide.style.display= 'none'
// // })

// // let button = document.querySelector('button')
// // button.style.width= '59px';
// // button.style.height = '23px'

// // button.addEventListener('click', function(){

// // 	let all = document.querySelector('article')
// // 	console.log(all)
// // 	document.body.style.fontWeight = 'bold';

// // })

// // let bonus1 = document.querySelector('h1')
// // bonus1.addEventListener('mouseover', function(event){
// // 	event.target.style.fontSize = Math.random()*100+ 'px'

// // })

// // let bonus2= document.querySelectorAll('p')[1];
// // console.log(bonus2)
// // bonus2.addEventListener('mouseover', function(event){
// // 	event.target.style.opacity = 0.1
// // })

// // Exercise 2 :

// let allBoldItems=[]

// function getBold_items (){

// 	let bold = document.getElementsByTagName('strong')
// 	console.log(bold)
// 	for (i=0; i<bold.length; i++){

// 		allBoldItems.push(bold[i])
// 		console.log(allBoldItems)
// 	}
// }
// getBold_items()

// function highlight() {

// 	for(i=0; i<allBoldItems.length; i++){
// 		allBoldItems[i].style.color = 'blue'
// 	}
// 	// allBoldItems.style.color = 'blue'

// 	console.log(allBoldItems)
// }
// highlight()

// function return_normal (){

// 	for(i=0; i<allBoldItems.length; i++){
// 		allBoldItems[i].style.color = 'black'


// 	}
// }
// return_normal()



// let change = document.querySelector('p');
// console.log (change)



// change.addEventListener('mouseover', highlight)
// change.addEventListener('mouseout', return_normal)


// Exercise 5 :


let anim = document.querySelector('h1');
console.log(anim)
anim.addEventListener('click', function(event){
	anim.style.color='blue'
})
anim.addEventListener('mouseover', function(event){
	anim.style.textAlign='center'})
anim.addEventListener('mouseout', function(event){
	anim.style.fontSize ='43px'
})
anim.addEventListener('dblclick', function(event){
	document.body.style.backgroundColor ='darkviolet'
})

