# ---------------------------------------import---------------------------------------------------
import Trie as tr
import keyboard

# ---------------------------------------input---------------------------------------------------
file_input = open("wordss.txt")
print("Please Enter Your Key:")
key = input()

myTrie = tr.Trie()
myTrie.formTrie2(file_input)
comp = myTrie.printAutoSuggestions(key)

if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")