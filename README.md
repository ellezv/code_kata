# Code Kata
This repo contains my solutions to various katas from codewars.com

##Sum of Positive:  

- Module: *sum_positives.py*    
- Tests: *test_sum_positives.py*  
- Link: (https://www.codewars.com/kata/sum-of-positive/, Code Wars: Sum of Positive)

```python
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

###Add Length:

- Module: *add_length.py*
- Tests: *test_add_length.py*
- Link: (https://www.codewars.com/kata/add-length, Code Wars: Add Length)

```python
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
```

###Name on Billboard

- Module: *billboard.py*
- Tests: *test_billboard.py*
- Link: (https://www.codewars.com/kata/name-on-billboard, Code Wars: Name on Billboard)

```python
def billboard(name, price=30):
    return sum(price for letter in name)
```

###Opposites Attract

- Module: *opposites.py*
- Tests: *test_opposites.py*
- Link (https://www.codewars.com/kata/opposites-attract/, Code Wars: Opposites Attract)

```python
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
```