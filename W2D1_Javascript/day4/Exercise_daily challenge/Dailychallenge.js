

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


// ________________________________________________________


// let words = ["Hello", "World", "in", "a", "frame"];

// function longestWordLength(arr) {
//   let len = arr[0].length;
//   for (let i = 1; i < words.length; i++) {
//       if(arr[i].length > len){
//         len = arr[i].length;
//       }
//   }
//   return len;
// }

// function addSpaces(word,len){
//   if(word.length == len){
//     return "";
//   }
//   return " ".repeat(len-word.length);
// }

// function stars () {
//   let len = longestWordLength(words);
//   console.log("*".repeat(len+4));
//   for(x in words){
//     console.log('* ' + words[x] + addSpaces(words[x],len) + ' *');
//   }
//   console.log("*".repeat(len+4));
// }
// stars();








