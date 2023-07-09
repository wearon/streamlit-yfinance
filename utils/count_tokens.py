from textblob import TextBlob

def count_tokens(vCountTokenStr):
    # Tokenize the input string
    blob = TextBlob(vCountTokenStr)
    tokens = blob.words

    # Count the number of tokens
    num_tokens = len(tokens)
    return num_tokens

def fit_within_token_limit(text, token_limit):
    remaining_tokens = token_limit
    shortened_text = text

    while count_tokens(shortened_text) >token_limit:
        # Reduce the length of the text by 10% and try again
        shortened_length = int(len(shortened_text) * 0.9)
        shortened_text = shortened_text[:shortened_length]

    return shortened_text