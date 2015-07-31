var isRobAwesome = "yes";
var colorOfRobsShirt = "yellow";

console.log("Hello World");

console.log("And all our yesterdays are lighted fools");
console.log("The way to dusty death");
console.log("Out, out brief candle " + isRobAwesome);

function checkout(item1, item2, coupon) {
  var subtotal = item1 + item2;
  subtotal = subtotal * (1 - coupon);
  var total = subtotal * 1.06;
  total = total.toFixed(2);
  return total;
}


function goToLunch(name) {
  alert("Lunch time!");
  alert("Close your computer, " + name);
  console.log("Let's eat food");

}

function roll() {
  var dice1 = (Math.floor(Math.random() * 6 + 1));
  var dice2 = (Math.floor(Math.random() * 6 + 1));
  var total = (dice1 + dice2);
  return total;

}


function howAmIDoing(collegeGpa, isFootballPlayer, needToGetIntoGradSchool) {
if (collegeGpa >= 4.0) {
  alert("I am so awesome");
}
else if (collegeGpa >= 3.0 || !needToGetIntoGradSchool){
  console.log("better get a job");
}
else if (collegeGpa >= 3.0) {
    alert("Not too shabby");
}
  else if (isFootballPlayer == true) {
    alert("I'm happy either way");
}
    else {
      alert("Crap! Study hard");
}
}



var numbers = [2, 3, 5, 7, 11, 13, 17, 23 ];
/*var i = 0;
while (i < numbers.length) {
  numbers[i] = numbers[i] +1;
  i = i + 1;
}
*/

function multByTwo(arr) {


for(var i = 0; i < arr.length; i++) {
  arr[i] = arr[i] * 42;
  console.log(arr[i]);
}
return arr;
}
