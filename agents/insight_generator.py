from langchain_core.runnables import RunnableLambda

# Install the langchain_openai package using pip:
# pip install -U langchain-openai

from langchain_openai import ChatOpenAI



from dotenv import load_dotenv
import  os
load_dotenv()


from pydantic import SecretStr

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr('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'),
    model="mistralai/mistral-7b-instruct:free"  # You can use other supported models too
)

print(llm.invoke("What is the capital of France?").content)
def generate_insights(df):
    """
    Generate insights from the DataFrame using a language model.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        str: Generated insights as a string.
    """
    prompt = f"Generate human readable insights from the following data:\n{df}"
    response = llm.invoke(prompt)
    return response.content

insight_agent= RunnableLambda(generate_insights)
# This code defines an insight generation agent that uses a language model to generate human-readable insights from a DataFrame.        
# The `generate_insights` function takes a DataFrame as input, constructs a prompt with the first few rows of the DataFrame,
# and invokes the language model to generate insights. The result is returned as a string.
# The agent is created using `RunnableLambda`, allowing it to be used in a data processing pipeline.
# This agent can be used to provide insights into the data, which can be useful for reporting or further analysis.