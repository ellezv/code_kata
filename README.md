# Code Kata
This repo contains my solutions to various katas from codewars.com

##Sum of Positive - 8kyu  

- Module: *sum_positives.py*    
- Tests: *test_sum_positives.py*  
- Link: [Code Wars: Sum of Positive](https://www.codewars.com/kata/sum-of-positive/)

Interesting solution:
```python
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

##Add Length - 8kyu

- Module: *add_length.py*
- Tests: *test_add_length.py*
- Link: [Code Wars: Add Length](https://www.codewars.com/kata/add-length)

Interesting solution:
```python
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
```

##Name on Billboard 8kyu

- Module: *billboard.py*
- Tests: *test_billboard.py*
- Link:  [Code Wars: Name on Billboard](https://www.codewars.com/kata/name-on-billboard)

Interesting solution:
```python
def billboard(name, price=30):
    return sum(price for letter in name)
```

##Opposites Attract - 8kyu

- Module: *opposites.py*
- Tests: *test_opposites.py*
- Link: [Code Wars: Opposites Attract](https://www.codewars.com/kata/opposites-attract/)

```python
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
```

##Is There a Vowel in There? - 8kyu
- Module: *is_vowel.py*
- Tests: *test_is_vowel.py*
- Link:[Code Wars: Is There a Vowel in There?](https://www.codewars.com/kata/is-there-a-vowel-in-there)

Interesting solution:
```python
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]
```

##Get Average - 8kyu
- Module: *get_average.py*
- Tests: *test_is_average.py*
- Link: [Code Wars: Get Mean of an Array](https://www.codewars.com/kata/get-the-mean-of-an-array/)

Interesting solution:
```python
def get_average(marks):
    return sum(marks) / len(marks)

```

###Title Case - 6kyu
- Module : *title_case.py*
- Tests: *test_title_case.py*
- Link: [Code Wars: Title Case](https://www.codewars.com/kata/title-case/)

Interesting solution:
```python
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
```

##Jaden Casing Strings - 7kyu
- Module: *jaden_case.py*
- Tests: *test_jaden_case.py*
- Link: [Code Wars: Jaden Casing Strings](https://www.codewars.com/kata/jaden-casing-strings/)

Interesting solution:
```python
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
```

##Simple Pig Latin - 5kyu
- Module: *simple_pig_latin.py*
- Tests: *test_simple_pig_latin.py*
- Link: [Code Wars: Simple Pig Latin](https://www.codewars.com/kata/simple-pig-latin/)

Interesting solution:
```python
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
```

##How Many Lightsabers Do You Own - 8kyu
- Module: *lightsaber.py*
- Tests: *test_lightsaber.py*
- Link: [Code Wars: How Many Lightsabers do you own](https://www.codewars.com/kata/how-many-lightsabers-do-you-own/)

Interesting solution:
```python
def howManyLightsabersDoYouOwn(name=""):
    return (18 if name=="Zach" else 0)
```

## Sum of nth Term of Series - 7kyu
- Module : *sum_terms.py*
- Tests: *test_sum_terms.py*
- Link: [Code Wars: Sum of nth Term of Series](http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/)

Interesting solution:
```python
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```

## Proper Parenthetics
- Module: *proper_parenthetics.py*
- Tests: *test_parenthetics.py*


##Sort a Deck of Cards - 7kyu
- Module : *sort_cards.py*
- Tests: *test_sort_cards.py*
- Link : [Code Wars: Sort a deck of Cards](https://www.codewars.com/kata/sort-deck-of-cards/)

Interesting solution:
```python
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
```

## Forbes Top 40
- Module: *forbes.py*
- Tests : *test_forbes.py*

