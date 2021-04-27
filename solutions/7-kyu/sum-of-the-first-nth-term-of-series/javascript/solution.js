function SeriesSum(n) {
  let finalNum = 1.25;
  let threeCount = 7;
  
  switch (n) {
    case 0:
      return "0.00"
    case 1:
      return "1.00"
    case 2:
      return "1.25"
  }
  
  for(i = 0; i < n - 2; i++) {
    finalNum += (1 / threeCount)
    threeCount += 3
  }
  return finalNum.toFixed(2).toString()
}