function to_nato(words) {
  const key = {"a":"Alfa", "b":"Bravo", "c":"Charlie", "d":"Delta", "e":"Echo", "f":"Foxtrot", "g":"Golf", "h":"Hotel", "i":"India", "j":"Juliett", "k":"Kilo", "l":"Lima", "m":"Mike", "n":"November", "o":"Oscar", "p":"Papa", "q":"Quebec", "r":"Romeo", "s":"Sierra", "t":"Tango", "u":"Uniform", "v":"Victor", "w":"Whiskey", "x":"Xray", "y":"Yankee", "z":"Zulu"};
  const translation = [];
  for (i = 0; i < words.length; i++) {
    if (words.charAt(i).toLowerCase() in key) {
      translation.push(key[words.charAt(i).toLowerCase()]);
    } else if (words.charAt(i) != " ") {
      translation.push(words.charAt(i));
    }
  }
  return translation.join(" ");
}