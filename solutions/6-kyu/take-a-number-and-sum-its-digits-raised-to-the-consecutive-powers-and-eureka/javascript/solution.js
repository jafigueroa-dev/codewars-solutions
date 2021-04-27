function sumDigPow(a, b) {
  const range = (start, end) => Array.from({length: (end - start)}, (v, k) => k + start);
  const n = range(a, b);
  let o = [];
  for (i = 0; i < n.length; i++) {
    let a = String(n[i]).split('').map((v, j) => Math.pow(v, j + 1)).reduce((a, b) => a + b, 0);
    if (a == n[i]) {
      o.push(n[i]);
    }
  }
  return o;
}
