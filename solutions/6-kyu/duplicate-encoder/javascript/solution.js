function duplicateEncode(word){
    let stringCount = new Map();
    let newWord = ''
    
    for(i = 0;i < word.length; i++) {
      stringCount[word.charAt(i).toLowerCase()] = (stringCount[word.charAt(i).toLowerCase()]+1) || 1 ;
    }
    for(i = 0;i < word.length; i++) {
      if (stringCount[word.charAt(i).toLowerCase()] > 1) { 
        newWord += ')'
      } else {
        newWord += '('
      }
    }
    return newWord
}
