let element = document.querySelector('.use')
console.log(element)

let element1 = document.getElementsByClassName('use')
console.log(element1)

let elemente = document.body.children[0]
console.log(elemente)


// ******************************

let element2 = document.body.children[1];
console.log(element2)

let elemente2 = document.firstElementChild
console.log(element2)

// ************************************

let element3 = document.body.children[1].children[1];
console.log(element3);

let elemente3 = document.getElementById('pete')
console.log(pete.lastElementChild);

let newDiv = document.createElement('div') 
console.log(newDiv)

let newTextNode = document.createTextNode('Here I am');
console.log(newTextNode)

newDiv.appendChild(newTextNode);
document.body.appendChild(newDiv);
console.log(document.body.appendChild(newDiv))