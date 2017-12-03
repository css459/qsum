from preprocess import *


# Preprocess
def preprocess_from_file(file_name):
    art = ""
    with open(file_name, 'r') as a:
        for line in a:
            art += remove_non_ascii(line) + " "
            art.strip()

    s = auto_preprocess(art)

    return art


# Get similarity

# Graph building

# Graph traversal

# Print summary


# Main function trigger
if __name__ == "__main__":
    article = preprocess_from_file("text/nytimes.txt")
