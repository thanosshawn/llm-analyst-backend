from langchain_core.runnables import RunnableLambda
def analyze(df):
    return df.describe().to_dict()



analyzer_agent=RunnableLambda(analyze)
