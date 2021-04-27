function squareDigits(num){
  return parseInt(Array.from(String(num), Number).map(a => a**2).join(""));
}