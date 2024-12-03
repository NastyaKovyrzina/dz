#zad 1
def group_words_by_first_letter(words):
    grouped = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)
    return grouped

words = ["apple", "banana", "avocado", "blueberry", "cherry"]
result = group_words_by_first_letter(words)
print(result)

#zad2
def find_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = find_anagrams(words)
print(result)

#zad3
def group_words_by_length(text):
    words = text.split()
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(word.lower())
    return grouped

text = "This is a simple test"
result = group_words_by_length(text)
print(result)

#zad4
def cartesian_product(list1, list2):
    return [(a, b) for a in list1 for b in list2]

list1 = [1, 2]
list2 = ['a', 'b']
result = cartesian_product(list1, list2)
print(result)

#zad5
def convert_to_palindromes(words):
    palindromes = []
    for word in words:
        palindromes.append(word + word[::-1])
    return palindromes

words = ["word", "rev"]
result = convert_to_palindromes(words)
print(result)

#zad6
def create_unique_id(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    unique_id = ''
    for char in s:
        if count[char] % 2 == 1:
            unique_id += char.upper()
        else:
            unique_id += char.lower()
        count[char] = 0  # Убираем чтобы избежать повторного учета

    return unique_id

input_str = "success"
result = create_unique_id(input_str)
print(result)

#zad7
def replace_with_synonyms(text, synonyms):
    words = text.split()
    new_text = []
    for word in words:
        new_text.append(synonyms.get(word, word))
    return ' '.join(new_text)

text = "quick brown fox"
synonyms = {'quick': 'fast', 'brown': 'dark'}
result = replace_with_synonyms(text, synonyms)
print(result)
