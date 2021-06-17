# • A string literal is enclosed in either single quotes, double quotes, or either quotation mark
# repeated three times. When the quotation mark is repeated three times, the string may span
# multiple lines.
# • Strings are immutable.
# • Strings can be concatenated using the plus operator.
# • A string can be repeated by multiplying it by an integer.
# • The str() function converts its argument to a string.
# • A string is a sequence. Thus:
# – A string can be used as the iterable in the header of a for-loop (in which case the loop
# variable takes on the values of the individual characters of the string).
# – The len() function returns the length of a string, i.e., the number of characters.
# – An individual character in a string can be accessed by specifying the character’s index
# within brackets.
# – Slicing can be used to obtain a portion (or all) of a string.


s="hi itsm me trying "
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())

ss= "rngv jlsnefdka;vja k er;mgvklre2 45dwsv ncjwLDSNVF CM.A/W DV JWNDV,CNW WOEFNKLWEJOWOEF OWJEFKL"
print(ss.count("n"))
print(ss.find("2"))
print (ss.find("cm".upper()))

s2="the best and more accurate results begins with the ok ,,the incredibles "

look_for = "th"
start_index = -1
for i in range(s.count(look_for)):
        start_index = s2.index(look_for, start_index + 1)
        print(s2[start_index : start_index + len(look_for) + 5])

w=s2.replace("the","TThEE")
print(w)


print(s2.split())
for words in s2.split():
    print(words )
