let planets = ['Mercure', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']




const listPlanets1 = document.getElementsByClassName('listPlanets')[0];
console.log(listPlanets1)
let element1= document.createElement('div');
element1.classList.add('planet');
element1.innerHTML = planets[0]
listPlanets1.appendChild(element1);
let mercure = document.getElementsByClassName( 'planet')[0]
mercure.style.background = 'white'
console.log(mercure)



const listPlanets2 = document.getElementsByClassName('listPlanets')[0];
let element2= document.createElement('div');
element2.classList.add('planet')
element2.innerHTML = planets[1]
listPlanets2.appendChild(element2);
let venus = document.getElementsByClassName( 'planet')[1]
venus.style.background = 'pink'
console.log(venus)


const listPlanets3 = document.getElementsByClassName('listPlanets')[0];
let element3= document.createElement('div');
element3.classList.add('planet');
element3.innerHTML = planets[2]
listPlanets3.appendChild(element3);
let earth = document.getElementsByClassName( 'planet')[2]
earth.style.background = 'blue'
console.log(earth)



const listPlanets4 = document.getElementsByClassName('listPlanets')[0];
let element4= document.createElement('div');
element4.classList.add('planet')
element4.innerHTML = planets[3]
listPlanets4.appendChild(element4);
let mars = document.getElementsByClassName( 'planet')[3]
mars.style.background = 'red';
console.log(mars)


const listPlanets5 = document.getElementsByClassName('listPlanets')[0];
let element5= document.createElement('div');
element5.classList.add('planet')
element5.innerHTML = planets[4]
listPlanets5.appendChild(element5);
let jupiter = document.getElementsByClassName( 'planet')[4]
jupiter.style.background = 'orange'
console.log(jupiter)



const listPlanets6 = document.getElementsByClassName('listPlanets')[0];
let element6= document.createElement('div');
element6.classList.add('planet')
element6.innerHTML = planets[5]
listPlanets6.appendChild(element6);
let saturn = document.getElementsByClassName( 'planet')[5]
saturn.style.background = 'purple'


console.log(saturn)



const listPlanets7 = document.getElementsByClassName('listPlanets')[0];
let element7= document.createElement('div');
element7.classList.add('planet');
element7.innerHTML = planets[6]
listPlanets7.appendChild(element7);
let uranus = document.getElementsByClassName( 'planet')[6]
uranus.style.background = 'green'

console.log(uranus)



const listPlanets8 = document.getElementsByClassName('listPlanets')[0];
let element8= document.createElement('div');
element8.classList.add('planet');
element8.innerHTML = planets[7]
listPlanets8.appendChild(element8);
let neptune = document.getElementsByClassName( 'planet')[7]
neptune.style.background = 'yellow'

console.log(neptune)




