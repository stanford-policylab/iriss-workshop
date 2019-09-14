from sys import argv

def top_n(d, n = 5):
    """Prints the `n` words occurring most frequently.
    
    Args:
        d: A dictionary which contains `key:value` pairs of the following sort:
            `word:count`, where `word` is a word, and `count` is the number of
            occurrences.
        n: The number of words to print.
    Returns:
        None. (Prints the top `n` words as a side-effect.)
    """
    d = sorted(d, key = d.get, reverse = True)
    print(d[:n])

def make_dict(f)
    """Turns a file into a dictionary by tokenizing text using whitespace.
    
    Args:
        f: A file object.
    Returns:
        A dictionary of `key:value` pairs where `key` is a token (i.e., word)
        and `value` is the number of occurences in the file.
    """
    words = f.read().split(" \n\t")
    {word:words.count(word) for word in set(words)}

if __name__ == "__main__":
    with open(argv[1], "r") as f:
        d = make_dict(f)
        top_n(d, n = argv[2])