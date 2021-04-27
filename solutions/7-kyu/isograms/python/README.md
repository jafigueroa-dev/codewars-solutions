[isograms](https://www.codewars.com/kata/54ba84be607a92aa900000f1)

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

```haskell
isIsogram "Dermatoglyphics" == true
isIsogram "aba" == false
isIsogram "moOse" == false -- ignore letter case
```
```javascript
isIsogram("Dermatoglyphics") == true
isIsogram("aba") == false
isIsogram("moOse") == false // -- ignore letter case
```
```python
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```
```ruby
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```
```C
is_isogram("Dermatoglyphics" ) == true;
is_isogram("aba" ) == false;
is_isogram("moOse" ) == false; // -- ignore letter case
```
```julia
isisogram("Dermatoglyphics" ) == true
isisogram("aba" ) == false
isisogram("moOse" ) == false # -- ignore letter case
```
```nasm
for the string "Dermatoglyphics" return 1 ; It's true
for the string "aba" return 0 ; It's false
for the string "moOse" return 0 ; It's false
```