def main():
    with open("books/frankenstein.txt") as s:
        file_contents = s.read()
    lower_contents = file_contents.lower()
    appearances = {}
    file_length = len(file_contents.split())
    for char in lower_contents:
        if char not in appearances:
            if char in "abcdefghijklmnopqrstuvwxyz":
                appearances[char] = 1
        else:
            appearances[char] += 1
    word_list = [{'letter': char, 'count': appearances[char]} for char in appearances]
    def sort_on(dict):
        return dict["count"]
    word_list.sort(reverse=True, key=sort_on)
    return file_length, word_list

file_length, word_list = main()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{file_length} words found in the document")

for i in range(0, len(word_list)):
    print(f"The '{word_list[i]['letter']}' was found {word_list[i]['count']} times")

print("--- End report ---")