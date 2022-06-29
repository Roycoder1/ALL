const numbers = [5,0,9,1,7,4,2,6,3,8];

let number1 = numbers.join(" ");
let number2 = numbers.join("+");
let number3 = numbers.join("");
console.log(number1)
console.log(number2)
console.log(number3)
console.log(numbers.toString());

let numberAscending = numbers.sort();
let numberDescending = numberAscending.reverse()
console.log(numberDescending)

let red = [[5],[0],[9],[1],[7],[4],[2],[6],[3],[8]];

for ( let i= 0; i<1 ;i++)
	for( let j = 0; j<10;j++){
		console.log(red[i,j])
	}

// corretion bubble sort:

let arr = [[5],[0],[9],[1],[7],[4],[2],[6],[3],[8]];

let temp;

for (let i=0 ; i<arr.length;i++){
	for(let j =0 ; i<arr.length;i++){
		if (arr[i]>arr[j]){
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		}
	}
}
console.log(arr)
