## query
create a function the input is as integer between 1 and 6 and the output tuple with random values and the length of tuple must match the argument givin to the function
## answer
```
 def roll_dice(num_dice):
    return tuple(random.randint(1, 6) for _ in range(num_dice))
```       