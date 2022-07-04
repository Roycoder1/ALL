DOM
What is DOM (Document Object Model)

JavaScript can change all the HTML elements in the page
JavaScript can change all the HTML attributes in the page
JavaScript can change all the CSS styles in the page
JavaScript can remove existing HTML elements and attributes
JavaScript can add new HTML elements and attributes
JavaScript can react to all existing HTML events in the page
JavaScript can create new HTML events in the page

Finding HTML elements by id
Finding HTML elements by tag name
Finding HTML elements by class name
Finding HTML elements by selectors


Finding HTML Elements
Method	                                Description
document.getElementById('root')	        Find an element by element id
document.getElementsByTagName('div')	  Find elements by tag name
document.getElementsByClassName('a')	  Find elements by class name
document.querySelector('#root .a')
document.querySelectorAll('#root .a')


Changing HTML Elements
Property	Description
element.innerHTML/innerText =  new html content	Change the inner HTML of an element
element.attribute = new value	Change the attribute value of an HTML element
element.style.property = new style	Change the style of an HTML element
element.setAttribute(attribute, value)	Change the attribute value of an HTML element


Adding and Deleting Elements
Method	Description
document.createElement(element)	Create an HTML element
document.removeChild(element)	Remove an HTML element
document.appendChild(element)	Add an HTML element
document.replaceChild(new, old)	Replace an HTML element




DOM Selectors
--------------
getElementById
getElementsByTagName
getElementsByClassName

querySelector
querySelectorAll

getAttribute
setAttribute

##Changing Styles
style.{property} //ok

className //best
classList //best

classList.add
classList.remove
classList.toggle

##Bonus
innerHTML //DANGEROUS

parentElement
children
childNodes

document.createElement;
appendChild;
removeChild;
replaceChild;

##It is important to CACHE selectors in variables












let uls = document.getElementsByTagName('ul');
// <li> 7 </li>

let li = document.createElement('li');
li.textContent = '7'; //innerText innerHTML
// li.className.add('my_class_name');
li.setAttribute('id','myli');
li.style.color = 'red';

uls[0].appendChild(li);

let _old = uls[0].children[4];

let _new = uls[0].children[uls[0].children.length-1];


uls[0].replaceChild(_new,uls[0].children[4]);
uls[0].appendChild(_old)






