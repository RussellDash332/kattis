var q = parseInt(readline());
for (let i = 0; i < q; i++) {
    let n = parseInt(readline());
    let fact = 1;
    for (let j = 1; j <= n; j++) {
        fact *= j;
    }
    console.log(fact%10);
}