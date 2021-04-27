function order(words){
  let splitWords = words.split(' ');
  let result = new Array(splitWords.length).fill("");
  for (i = 0; i < splitWords.length; i++) {
    let num = splitWords[i].match(/\d+/);
    result[num - 1] = splitWords[i];
  }
  return result.join(" ");
}