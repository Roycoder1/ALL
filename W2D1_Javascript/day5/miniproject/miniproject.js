let yes = (user)=>{
    if (user) {
        let userNumber = prompt("Enter a number between 0 to 10",4)
        let numb = Number(userNumber);
        let computerNumber = Math.floor(Math.random() * 10)
        console.log(computerNumber);
        console.log(condition(numb));
        if (condition(numb)){
            let guesses=0
            while(compareNumbers(numb,computerNumber)){
                guesses++
                if (guesses>=3 ) {
                  alert('sorry, no more guesses')
                  return
              }
              userNumber = prompt("Enter a number between 0 to 10",4)
              numb = Number(userNumber);
          }
      }
  }
}
let condition= (userNumber)=>{
    // let numb = Number(game);
    if (isNaN(userNumber)){
        alert("Sorry Not a number, Goodbye");
        return false;
    }
    else if(userNumber>10){
        alert('Sorry it"s not a good number, Goodbye')
        return false;
    }
    return true
}
let playTheGame =()=>{
    let user = confirm("Would you like to play a game?")
    if (user) {
        yes(user)
    }
    else{
        alert("No problem, Goodbye")
    }
}
playTheGame()
// Second part:
function compareNumbers (userNumber,computerNumber)
{
   console.log(userNumber);
   console.log(computerNumber)
   if (userNumber==computerNumber){
    alert("Winner");
    return false;
}
else if (userNumber > computerNumber){
    alert('Your number is bigger then the computer"s, guess again');
    // userNumber=prompt("ask for a new number");
    return true
}
else if (userNumber< computerNumber){
 alert('Your number is smaller than the computer"s, guess again');
   // userNumber = prompt("ask for a new number");
   return true
}
}
// condition()












// function random(){
//     let computerNumber = Math.floor(Math.random() * 10)
//     return computerNumber
// }
// function loop(guesses){

//     while(compareNumbers(numb,computerNumber)){
//         guesses++
//         if (guesses>3 ) {
//             return 


//         }
//         loop(guesses)
//     }


//     let yes = ()=>{

//         let computerNumber=random()
//         let userNumber = prompt("Enter a number between 0 to 10",4)
//         let numb = Number(userNumber);



//         if (condition(numb)){
//             let guesses=0
//             loop(guesses)











//             let condition= (userNumber)=>{

//     // let numb = Number(game);


//     if (isNaN(userNumber)){
//         alert('Sorry Not a number, Goodbye');
//         return false;
//     }
//     else if (userNumber>10||userNumber<0){
//         alert('Sorry it’s not a good number, Goodbye')
//         return false;
//     }
//     return true;



// }



// let playTheGame =()=>{
//     let user = confirm('Would you like to play a game?');

//     if (user===true) {
//         yes();
//     }
//     else{
//         alert('No problem, Goodbye');
//     }

// }
// playTheGame()

// // Second part:

// function compareNumbers (userNumber,computerNumber)
// {



//  console.log(userNumber);
//  console.log(computerNumber);

//  if (userNumber==computerNumber){
//     alert('Winner');
//     return false;

// }
// else if (userNumber > computerNumber){
//     alert('Your number is bigger then the computer’s, guess again');
//     return true

// }
// else if (userNumber< computerNumber){
//    alert('Your number is smaller than the computer’s, guess again');
//    return true
// }

// }
// // condition()

