from sentence import Sentence

# Get similarity

# Graph building

# Graph traversal

# Print summary


# Main function trigger
if __name__ == "__main__":
    query = "Mr. Trump's thoughts on the tax cut"

    q = Sentence(query)
    s = Sentence.sentences_from_article_file("text/nytimes.txt")

    similar = q.get_similar_scores_to_self(s)

    print query, "\n"
    for s in similar:
        print s[0], s[1].original
