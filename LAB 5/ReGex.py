#1
import re

def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ['a', 'ab', 'abb', 'abbb', 'ac', 'abc']
for test_string in test_strings:
    if match_pattern(test_string):
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")

    
#2
import re

def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ['ab', 'abb', 'abbb', 'a', 'abc', 'abbbb']
for test_string in test_strings:
    if match_pattern(test_string):
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")


#3
import re

def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, string)
    return sequences

test_string = "This_is_a_test_string_with_some_sequences_like_this_one_and_this_too"
result = find_sequences(test_string)
print("Sequences found:", result)


#4
import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequences

test_string = "This Is a Test String With Some Sequences Like This One And This Too"
result = find_sequences(test_string)
print("Sequences found:", result)


#5
import re

def match_pattern(string):
    pattern = r'^a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False

test_strings = ['a', 'ab', 'acb', 'a123b', 'axbyzb', 'abbbb']
for test_string in test_strings:
    if match_pattern(test_string):
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")


#6
import re

def replace_with_colon(string):
    pattern = r'[ ,.]'
    replaced_string = re.sub(pattern, ':', string)
    return replaced_string

test_string = "This is a test, with some spaces and dots. It will be replaced."
result = replace_with_colon(test_string)
print("Original string:", test_string)
print("After replacement:", result)


#7
def snake_to_camel(snake_case):
    words = snake_case.split('_')

    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case

snake_case_string = "this_is_snake_case"
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case:", camel_case_string)


#8
import re

def split_at_uppercase(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

test_string = "SplitThisStringAtUpperCaseLetters"
result = split_at_uppercase(test_string)
print("Parts after splitting:", result)


#9
import re

def insert_spaces(string):

    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return result

test_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = insert_spaces(test_string)
print("Modified string:", result)


#10
def camel_to_snake(camel_case):
    snake_case = ''
    for i, char in enumerate(camel_case):
        if char.isupper() and i != 0:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case:", snake_case_string)
