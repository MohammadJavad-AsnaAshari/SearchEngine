# ---------------------------------------import---------------------------------------------------
import keyboard


# ---------------------------------------trie node---------------------------------------------------
class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False

# ---------------------------------------trie class---------------------------------------------------
class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

# ---------------------------------------trie CLI---------------------------------------------------
    def formTrie2(self, fin):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for i, line in enumerate(fin):
            if i == 120000: break
            word = line.strip()
            self.insert(word)  # inserting one key to the trie.

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True


    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.

        if node.last and keyboard.read_hotkey() == "tab":
            print(word, end="\r")
                
        for a, n in node.children.items():
            # print(node.children.items())
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return -1

        self.suggestionsRec(node, key)
        return 1
    
    
 # ---------------------------------------trie GUI---------------------------------------------------
    global key_list
    key_list = []

    def suggestionsRecGUI(self, node, word, comboBox):

        # Method to recursively traverse the trie
        # and return a whole word.

        if node.last:
            key_list.append(word)
                
        comboBox["values"] = key_list
        for a, n in node.children.items():
            # print(node.children.items())
            self.suggestionsRecGUI(n, word + a, comboBox)

    def printAutoSuggestionsGUI(self, key, comboBox):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root

        global key_list

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                comboBox["values"] = []
                return 0
            node = node.children[a]
            comboBox["values"] = []

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            comboBox["values"] = []
            return -1

        self.suggestionsRecGUI(node, key, comboBox)
        key_list = []
        return 1