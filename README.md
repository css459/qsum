# Qsum
#### Summarization platform curated towards search queries
#### By Eric Lin, Cole Smith

## Requirements
* `nltk` - `pip install nltk`

# System Design Pipeline

## Preprocessing

The pipeline begins with preprocessing the article files in to Python objects.
Articles are stored in files, and preprocessing begins by tokenizing every sentence
in the article, and building `Sentence` objects from them.

When a `Sentence` is initialized, it stores the original sentence string, and a
processed string. The processed string undergoes the following pipeline:

* Non-ascii character removal
* Stop word removal
* Stemming (Snowball)

At the end of a preprocessing operation a `Sentence` might look like this:

* Original: 
    
    `I had to fire General Flynn because he lied to the Vice President and the FBI,  Mr. Trump wrote.`
  
* Preprocessed:

    `[u'fire', u'general', u'flynn', u'lie', u'vice', u'presid', u'fbi', 'mr', u'trump', u'wrote']`


## Similarity Scoring

Similarity scoring uses the count of similar stems from two preprocessed 
lists (Sentences) A and B. The more similar stems list A and B.