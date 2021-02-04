function f(x,y,a,b) {
    return a*x+b*y;
}

var line1 = readline().split(" ");
var line2 = readline().split(" ");
var a = parseInt(line1[0]);
var b = parseInt(line1[1]);
var m = parseInt(line2[0]);
var s = parseInt(line2[1]);
var x = s-m;
var y = 2*m-s;

if (s <= m+1) {
    console.log(Math.max(f(m-1,1,a,b),f(1,m-1,a,b),f(1,Math.max(s-2,1),a,b)));
} else if (s <= 2*m-1) {
    console.log(Math.max(f(x,y,a,b),f(m-1,1,a,b)));
} else {
    console.log(0);
}