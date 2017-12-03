from preprocess import *
from similarity import *


# Preprocess
def preprocess_from_file(file_name):
    art = ""
    with open(file_name, 'r') as a:
        for line in a:
            art += remove_non_ascii(line) + " "
            art.strip()

    return auto_preprocess(art)


# Get similarity

# Graph building

# Graph traversal

# Print summary


# Main function trigger
if __name__ == "__main__":
    query = "Mr. Trump's thoughts on the tax cut"
    sentences = preprocess_from_file("text/nytimes.txt")

    processed_query = auto_preprocess_single(query)
    get_similar_scores_to_query(processed_query, sentences)
