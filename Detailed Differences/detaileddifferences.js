var q = parseInt(readline());
for (let i = 0; i < q; i++) {
    let a = readline();
    let b = readline();
    let result = "";
    for (let j = 0; j < a.length; j++) {
        if (a[j]===b[j]) {
            result += ".";
        } else {
            result += "*";
        }
    }
    console.log(a);
    console.log(b);
    console.log(result);
}