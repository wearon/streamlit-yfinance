from utils.query_message import query_message


import openai
import pandas as pd


def ask( query: str, df: pd.DataFrame, model: str = "gpt-4", token_budget: int = 4096 - 500, print_message: bool = False, ) -> str:
    """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {"role": "system", "content": "You answer questions about text or doc that I provided."},
        {"role": "user", "content": message},
    ]
    response = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=0
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message