// Ajoutez le code ci-dessus à votre fichier HTML

// Utilisation de Javascript :
// Récupérez le divet console.log it
// Changez le nom "Pete" en "Richard".
// Remplacez chaque prénom des deux <ul>'spar votre nom.
// Supprimez le <li>qui contient le nœud de texte "Sarah".

// Bonus - Utilisation de Javascript :
// Ajoutez une classe appelée student_listaux deux <ul>'s.
// Ajoutez les classes universityet attendanceau premier <ul>.


// let div = document.querySelector('div')
// console.log(div);
// let pete = document.body.children[1].children[1];
// console.log(pete.textContent = 'Richard')

// let roy = document.body.children[1].children[1];

// console.log(roy.textContent = 'Roy',)
// let roy2 = document.body.children[1].children[0];
// console.log(roy2.textContent = 'Roy',)

// let parentElem =document.getElementsByClassName('list')[1];
// console.log(parentElem)
// let childElem = parentElem.children[1]
// console.log(childElem)
// console.log(parentElem.removeChild(childElem));


// Exercise 2 :
// Ajoutez une couleur d'arrière-plan "bleu clair" et un peu de rembourrage au fichier <div>.

// Ne pas afficher le <li>qui contient le nœud de texte "John".

// Ajoutez une bordure au <li>qui contient le nœud de texte "Pete".

// Modifiez la taille de la police de tout le corps.

// Bonus : Si la couleur de fond du div est "bleu clair", alertez "Bonjour x et y" (x et y sont les utilisateurs dans la div).

// let blue = document.querySelector('div')
// console.log(blue.style.background='lightblue')

// let john = document.querySelectorAll ('li')[0]
// console.log(john.style.display = 'none')

// let pete = document.querySelectorAll ('li')[1]
// console.log(pete.style.border= '2px solid yellow')
// let body = document.body
// console.log(body)
// console.log(body.style.fontSize = '50px')

// // Bonus :

// let div = document.querySelector('div')



// if (blue.style.background=='lightblue') {
// 	alert('Hello John and Pete')

// }

// Exercise 3:

// Ajoutez le code ci-dessus à votre fichier HTML

// Dans le <div>, modifiez la valeur de l'attribut id de navBar à socialNetworkNavigation , à l'aide de la setAttributeméthode .

// Nous allons ajouter un nouveau <li>au <ul>.
// Tout d'abord, créez une nouvelle <li>balise (utilisez la createElementméthode).
// Créez un nouveau nœud de texte avec "Déconnexion" comme texte spécifié.
// Ajoutez le nœud de texte au nœud de liste nouvellement créé ( <li>).
// Enfin, ajoutez ce nœud de liste mis à jour à la liste non ordonnée ( <ul>), en utilisant la appendChildméthode.

// let navbar = document.getElementById('navBar')
// navbar.setAttribute('id','socialNetworkNavigation')

// const nav = document.getElementsByClassName('socialNetworkNavigation')[0];
// let litag = document.createElement('li')
// litag.innerText = 'Logout';
// document.body.appendChild(litag)
// let node = document.getElementsByTagName("a")[0];
// node.appendChild(litag)


// Exercise 4 :

// Jetez un œil à ce lien pour obtenir de l'aide.

// Le but de ce défi est d'afficher une liste de deux livres sur votre navigateur.

// Dans le corps de la page HTML, créez un div vide :
// <div class="listBooks"></div>
// Dans le fichier js, créez un tableau appelé allBooks. Il s'agit d'un tableau d'objets. Chaque objet est un livre qui possède 4 clés (soit 4 propriétés) :
// Titre,
// auteur,
// image : une url,
// déjàRead : qui est un booléen (vrai ou faux).

// Initiez le tableau avec 2 livres de votre choix (c'est-à-dire ajoutez manuellement 2 objets livres dans le tableau)
// Exigences : Toutes les instructions ci-dessous doivent être codées dans le fichier js :
// À l'aide du DOM, rendez les livres dans un tableau HTML (le tableau HTML doit être ajouté au <div>créé dans la partie 1).
// Pour chaque livre :
// Vous devez afficher le titre du livre et l'auteur du livre.
// Exemple : HarryPotter écrit par JKRolling.
// La largeur de l'image doit être définie sur 100px.
// Si le livre est déjà lu. Définissez la couleur des détails du livre sur rouge.
let img = document.createElement("img");
img.src = "https://www.babelio.com/couv/bm_CVT_Bel-Ami_5950.jpg" ;
let src = document.getElementsByClassName("listBooks")[0];
src.appendChild(img);

let element2= document.createElement('div');
let img2 = document.createElement("img");
element2.classList.add('img2');
img.src = "https://d1w7fb2mkkr3kw.cloudfront.net/assets/images/book/lrg/9781/4549/9781454911869.jpg";
let src2 = document.getElementsByClassName("listBooks")[0];
src2.appendChild(img);


let allBooks

allBooks = {
	
	Title : 'Bel-ami',
	Author : 'Guy de Maupassant',
	// img.src = 'belami.jpg',
	alreadyRead: true,


	Title : 'art of war',
	Author : 'Sun Tzu',
	// img.src = 'art.JPG',
	alreadyRead: true,	
}

let book = document.getElementsByClassName("listBooks")[0];
let element1= document.createElement('p');
element1.innerText = 'Title : Bel-ami\nAuthor: Guy de Maupassant\nalreadyRead: true'
element1.style.marginLeft= '60px'
book.appendChild(element1);














