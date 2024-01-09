const h = parseInt(readline());
var lines = [];
var color_start = [];
for (let i = 0; i < h; i++) {
  const row = readline().split(" ");
  if (row[0] == "0") {
    lines.push(row.slice(1));
    color_start.push("black");
  }
  else {
    lines.push(row);
    color_start.push("white");
  }
}

function sum(l) {
  var s = 0;
  for (let j of l) {
    s += parseInt(j);
  }
  return s;
}
var width = sum(lines.at(0));
var valid = true;
for (let j of lines) {
  if (sum(j) != width) {
    valid = false;
    break;
  }
}

if (valid) {
  for (let i = 0; i < h; i++) {
    var cst = color_start.at(i);
    var colors = cst == "white" ? [".", "O"] : ["O", "."];
    var s = "";
    for (let j = 0; j < lines.at(i).length; j++) {
      s += colors[j % 2].repeat(parseInt(lines.at(i).at(j)));
    }
    console.log(s);
  }
}
else {
  console.log("INVALID");
}
