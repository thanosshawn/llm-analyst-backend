from langchain_core.runnables import RunnableLambda

import pandas as pd

def clean(df):
    return df.dropna()

cleaner_agent=RunnableLambda(clean)
# This code defines a simple data cleaning agent that removes rows with missing values from a DataFrame.
# It uses the `Runnable` class from `langchain_core` to create a reusable cleaning function.    
# The `clean` function takes a DataFrame as input and returns a cleaned DataFrame with no missing values.
# This agent can be used in a data processing pipeline to ensure that the data is clean before further analysis.