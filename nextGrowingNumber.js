const n = readline();

var growing = true;
for (var i = 1; i < n.length; i++) {
  if (n.at(i) < n.at(i - 1)) {
    console.log(n.substring(0, i) + n.at(i - 1).repeat(n.length - i));
    growing = false;
    break;
  }
}

if (growing) {
  if (n.at(-1) != '9') {
    console.log(parseInt(n) + 1);
  }
  else if (n == "9".repeat(n.length)) {
    console.log("1".repeat(n.length + 1));
  }
  else {
    var nine = n.indexOf('9');
    var next = "" + (parseInt(n.at(nine - 1)) + 1);
    console.log(n.substring(0, nine - 1) + next.repeat(n.length - nine + 1));
  }
}
