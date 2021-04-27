function autocomplete(input, dictionary){
  let result = [];
  for (i = 0, j = 0; i < dictionary.length && j < 5; i++) {
    if (dictionary[i].toLowerCase().startsWith(input.replace(/[^a-zA-Z ]/g, "").toLowerCase())) {
      result.push(dictionary[i]);
      j++
    }
  }
  return result;
}