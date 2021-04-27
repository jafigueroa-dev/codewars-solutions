[exclamation-marks-series-17-put-the-exclamation-marks-and-question-marks-to-the-balance-are-they-balanced](https://www.codewars.com/kata/57fb44a12b53146fe1000136)

# Description:

 Each exclamation mark weight is 2; Each question mark weight is 3. Put two string `left` and `right` to the balance, Are they balanced?
 
 If the left side is more heavy, return `"Left"`; If the right side is more heavy, return `"Right"`; If they are balanced, return `"Balance"`.

# Examples

```javascript
balance("!!","??") === "Right"
balance("!??","?!!") === "Left"
balance("!?!!","?!?") === "Left"
balance("!!???!????","??!!?!!!!!!!") === "Balance"
```
```python
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
```

```php
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
```

```haskell
-- For Haskell use the Comparison type defined in Preloaded code
-- data Comparison = Left | Right | Balance deriving (Show, Eq, Enum, Bounded)

balance :: String -> String -> Comparison

balance "!!" "??" == Right
balance "!??" "?!!" == Left
balance "!?!!" "?!?" == Left
balance "!!???!????" "??!!?!!!!!!!" == Balance
```