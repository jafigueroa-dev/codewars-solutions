[last-digit-of-a-huge-number](https://www.codewars.com/kata/5518a860a73e708c0a000027)

For a given list `[x1, x2, x3, ..., xn]` compute the last (decimal) digit of 
`x1 ^ (x2 ^ (x3 ^ (... ^ xn)))`. 

E. g.,
```c
last_digit({3, 4, 2}, 3) == 1
```
```java
int[] array = new int[] {3,4,2};
lastDigit(array) == 1
```
```cpp
last_digit({3, 4, 2}) == 1
```
```csharp
int[] array = new int[] {3,4,2};
LastDigit(array) == 1
```
```golang
LastDigit([]int{3, 4, 2}) == 1
```
```haskell
lastDigit [3, 4, 2] == 1
```
```javascript
lastDigit([3, 4, 2]) === 1
```
```python
last_digit([3, 4, 2]) == 1
```
```prolog
last_digit([3, 4, 2], 1).
```
because `3 ^ (4 ^ 2) = 3 ^ 16 = 43046721`.

_Beware:_ powers grow incredibly fast. For example, `9 ^ (9 ^ 9)` has more than 369 millions of digits. `lastDigit` has to deal with such numbers efficiently.

_Corner cases:_ we assume that `0 ^ 0 = 1` and that `lastDigit` of an empty list equals to 1.

This kata generalizes [Last digit of a large number](http://www.codewars.com/kata/last-digit-of-a-large-number/haskell); you may find useful to solve it beforehand.