[check-by-queen](https://www.codewars.com/kata/5a1cae0832b8b99e2900000c)

In a game of chess, a queen is the most powerful piece on the board. She can move an unlimited number of squares in a straight line in any of 8 directions (forwards, backwards, left, right, and each of the four diagonals in between).

The diagram below shows the queen's influence from her current position - she would be able to take any piece on a square marked with an 'X'.

<br>
<figure>
<img style="display:block; margin:auto;" src="https://s-media-cache-ak0.pinimg.com/originals/57/7f/04/577f04f3bd21238fd74626155968aeca.jpg">
</figure>

<figcaption style="text-align:center; font-size:12px;">
  Image from: https://www.pinterest.com/pin/567453621770398092/
</figcaption>
<br>

An opponent's king who can be taken by the queen is said to be in 'check', and would then need to find some way to escape this situation.

In any normal game of chess, the queen would work with her army on an 8x8 board to threaten the king in this way, and ultimately try to win the game. However, for this kata, the queen will work by herself on a 5x5 board.

The 5x5 chessboard will be represented as a 2 dimensional array, (ie: an array containing 5 other arrays, each containing 5 single character elements). Empty spaces within each sub-array will be represented by an asterix: ```"*"```, while one of these 25 elements will be represented by a ```"q"``` (queen) and a ```"k"``` (king). Both will be represented in lower case.

The 2 dimensional chessboard array would look something like this:
```javascript
var board = [ [ '*', '*', '*', '*', '*' ],
              [ '*', '*', '*', '*', 'k' ],
              [ '*', '*', '*', '*', '*' ],
              [ '*', 'q', '*', '*', '*' ],
              [ '*', '*', '*', '*', '*' ] ];
```
Your task is to write a function which will return ```true``` if the king is in check, and ```false``` if he isn't.

Click <a href="https://en.wikipedia.org/wiki/Chess">here</a> for a more in-depth instruction on chess.





