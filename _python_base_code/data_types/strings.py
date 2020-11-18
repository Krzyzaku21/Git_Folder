# %% indeksowanie string
word = "Hello World"
print(word[0]) #H
print(word[1]) #e
print(word[2]) #l
print(word[3]) #l
print(word[4]) #o
print(word[0:5]) #Hello
# %% wstawianie różnych znaków
word = "He\'s"
word2 = r"He's"
print(word)
print(word2)
# %% ozielanie tekstu
#\n - linia pod
word = "Hello\nWorld"
print(word)
#\t - tabulacja
word1 = "Hello\tTab"
print(word1)
#\r - enter
word2 = "Hello\rEnter"
print(word2)
#\r\n - lini przerwy
word3 = "Hello\r\nLine"
print(word3)
# %% multilinia
word ="""
text1
text2
"""
print(word)
# %% booleans
word = "spam" == "Spam" #False
print(word)
word2 = "too" > "to" #True bo większa ilośc znaków
print(word2)
word3 = "abc" < "bbc" #True bo "b" wyższe od "a"
print(word3)
# %% operacje print stringu
one_line_string = "Hello World"
print("%s" % one_line_string) #Hello World
print(f"abc {one_line_string} def") #Hello World
print("abc {} def".format(one_line_string)) #Hello World
# %% operacje string
dodawanie = "text" + "text2" #texttext2
print(dodawanie)
mnozenie = "text" *2  #texttext
print(mnozenie)
# %% Reverse a string
my_str = "Hello"
reverse_str = my_str[::-1]
print(reverse_str) #olleH
# %% merge values
a = ("1", "2")
b, c = a
print(b,c) #1 2
# %% String Functions
print(", ".join(["spam", "eggs", "ham"]))# "spam, eggs, ham"
print("Hello ME".replace("ME", "world"))# "Hello world"
print("This is a sentence.".startswith("This")) # prints "True"
print("This is a sentence.".endswith("sentence.")) # prints "True"
print("This is a sentence.".upper() )# "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower())# "an all caps sentence"
print("spam, eggs, ham".split(", "))# "['spam', 'eggs', 'ham']"
# %%
