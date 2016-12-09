# code_kata
This repo contains my solutions to various katas from codewars.com

##Sum of Positive:  

-Module: *sum_positives.py*    
-Tests: *test_sum_positives.py*  
-Link: (https://www.codewars.com/kata/sum-of-positive/, Code Wars: Sum of Positive)

```python
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

###Add Length:

-Module: *add_length.py*
-Tests: *test_add_length.py*
-Link: (https://www.codewars.com/kata/add-length, Code Wars: Add Length)

```python
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
```
