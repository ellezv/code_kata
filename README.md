# Code Kata
This repo contains my solutions to various katas from codewars.com

##Sum of Positive - 8kyu  

- Module: *sum_positives.py*    
- Tests: *test_sum_positives.py*  
- Link: (https://www.codewars.com/kata/sum-of-positive/, Code Wars: Sum of Positive)

```python
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

###Add Length - 8kyu

- Module: *add_length.py*
- Tests: *test_add_length.py*
- Link: (https://www.codewars.com/kata/add-length, Code Wars: Add Length)

```python
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
```

###Name on Billboard 8kyu

- Module: *billboard.py*
- Tests: *test_billboard.py*
- Link: (https://www.codewars.com/kata/name-on-billboard, Code Wars: Name on Billboard)

```python
def billboard(name, price=30):
    return sum(price for letter in name)
```

###Opposites Attract - 8kyu

- Module: *opposites.py*
- Tests: *test_opposites.py*
- Link: (https://www.codewars.com/kata/opposites-attract/, Code Wars: Opposites Attract)

```python
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
```

###Is There a Vowel in There? - 8kyu
- Module: *is_vowel.py*
- Tests: *test_is_vowel.py*
- Link:(https://www.codewars.com/kata/is-there-a-vowel-in-there, Code Wars: Is There a Vowel in There?)

```python
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]
```

###Get Average - 8kyu
- Module: *get_average.py*
- Tests: *test_is_average.py*
- Link: (https://www.codewars.com/kata/get-the-mean-of-an-array/, Code Wars: Get Mean of an Array)

```python
def get_average(marks):
    return sum(marks) / len(marks)

```

###Title Case - 6kyu
- Module : *title_case.py*
- Tests: *test_title_case.py*
- Link: (https://www.codewars.com/kata/title-case/, Code Wars: Title Case)

```python
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
```

###Jaden Casing Strings - 7kyu
- Module: *jaden_case.py*
- Tests: *test_jaden_case.py*
- Link: (https://www.codewars.com/kata/jaden-casing-strings/, Code Wars: Jaden Casing Strings)

```python
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
```

###Simple Pig Latin - 5kyu
- Module: *simple_pig_latin.py*
- Tests: *test_simple_pig_latin.py*
- Link: (https://www.codewars.com/kata/simple-pig-latin/, Code Wars: Simple Pig Latin)

```python
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
```

###How Many Lightsabers Do You Own - 8kyu
- Module: *lightsaber.py*
- Tests: *test_lightsaber.py*
- Link: (https://www.codewars.com/kata/how-many-lightsabers-do-you-own/, Code Wars: How Many Lightsabers do you own)

```python
def howManyLightsabersDoYouOwn(name=""):
    return (18 if name=="Zach" else 0)
```