function multiplicationTable(row,col){
  let table = [];
  for(var i = 1; i < row + 1; i++) {
    table[i-1] = [...Array(col).keys()].map(x => i * (x + 1));
  }
  return table;
}