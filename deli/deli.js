
function takeANumber(line, name) {
    line.push(name);
    console.log("You are number " + line.length)
    return line.length;
}

function nowServing(line) {
  var name = line[0];
  console.log("now serving " + line.splice(0,1));


}

function spot(line, name) {
  for (var i = 0; i <= line.length; i++) {
    if(line[i] == name) {
      return i;
    }
  }
  console.log("You're not in the line");
}
