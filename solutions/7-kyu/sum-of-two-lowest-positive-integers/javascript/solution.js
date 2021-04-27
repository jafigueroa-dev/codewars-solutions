function sumTwoSmallestNumbers(numbers) {  
  const list = numbers.sort((a, b) => a - b)
  return list[0] + list[1]
}