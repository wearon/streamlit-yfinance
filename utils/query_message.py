from utils.num_tokens import num_tokens
from utils.strings_ranked_by_relatedness import strings_ranked_by_relatedness


import pandas as pd


def query_message(query: str, df: pd.DataFrame, model: str, token_budget: int) -> str:
    """Return a message for GPT, with relevant source texts pulled from a dataframe."""
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = 'Use the below text to answer the subsequent question. If the answer cannot be found in the text, write "I could not find an answer."'
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        next_article = f'\n\nNext section:\n"""\n{string}\n"""'
        print(next_article)
        if num_tokens(message + next_article + question, model=model) > token_budget:
            break
        else:
            message += next_article

    return message + question