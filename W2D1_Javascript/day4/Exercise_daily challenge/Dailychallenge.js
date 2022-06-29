

let user = prompt('Do a sentece separated by commas', 'Hello, World, in, a, frame');
let arr = user.split(',');
console.log(arr);




let sentence = ()=>{
	
	arr.forEach()

}
console.log(arr)




function frame(str){
	let border = '*'.repeat(str.length + 25)
	return `${border}\n* ${str} *\n${border}`
}

console.log(frame(arr))

sentence()

// correction:

// let arr = ["Hello", "World", "in", "a", "frame"] ;

// const longestString = strings => {
// 	let longest = strings[0].length;
// 	strings.forEach(str => {
// 		str.length >=  longest ? longest = str.length : longest;
// 	});
// 	return longest;
// }

// const createSpacesNeeded = spacesNeeded => {
// 	let spaces = '';
// 	for(let i = 0; i < spacesNeeded; i++) {
// 		if(i < spacesNeeded) {
// 			spaces = spaces + ' ';
// 		}
// 	}
// 	return spaces;
// }

// const stringsRecFrame = strings => {
// 	const longestStr = longestString(strings);
//   //console.log(longestStr)

//   let newLine = '\n';
//   console.log('*********');
//   strings.forEach(str => {
//   	if(str.length === longestStr) {
//   		console.log(`*${str}* ${newLine}`);
//   	} else {
//   		let spacesNeeded = longestStr - str.length;
//       //console.log('spacesNeeded: ', spacesNeeded)
//       let spaces = createSpacesNeeded(spacesNeeded);
//       //console.log('spaces: ', spaces)
//       console.log(`*${str}${spaces}* ${newLine}`);
//   }
// });
//   console.log('*********');
// }

// console.log(stringsRecFrame(arr))
