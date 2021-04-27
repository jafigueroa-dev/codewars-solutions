function persistence(num) {
  x = num;
  count = 0;
  while (x.toString().length != 1) {
    x = eval(Array.from(String(x), Number).join("*"));
    count++;
  }
  return count;
}