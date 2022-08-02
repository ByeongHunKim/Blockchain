secretVal = "";
for (var i = 0; i < 16; i++) {
  secretVal += ar.charAt(Math.floor(Math.random() * ar.length));
}

console.log("secretVal : ", secretVal);
