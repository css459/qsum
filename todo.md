# To Do List

[x] Implement and test sentence similarity scoring

[x] Implement and test sentence similarity scoring *with query term*

[] Create a graph based on similarity scoring

[] Modify the graph to include *query terms*

[] Create random walk strategy

[] Test random walk strategy

[] Procure articles from scholarly sources and run algorithm

[] Create test to give to humans

[] Create presentation

# Follow up tasks

[x] Allow support for detecting words in the query of similar root

* Ex: If the query contains the term `Economic` we should also be properly weighting
the word `Economics` and vice versa

* For this, we can use the `ntlk.snowball` stemmer
    

# Source File Layout

* `similarity.py`: Includes functions to generate similarity scores between
                   sentences

* `graph.py`: Graph data structure

* `preprocess.py`: Parses text files into memory and gathers stop words, frequencies.

* `summarize.py`: Takes an input string of an article, and returns a summary

* `main.py`: Implements a user interface for querying a list of files which
             contain articles, and prints the summaries to a file and to console.

# Presentation Slides

* Introduction

* Problem Statement

* Strategy

* Results
