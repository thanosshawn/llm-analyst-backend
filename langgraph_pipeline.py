import pandas as pd
from agents.cleaner import cleaner_agent
from agents.analyzer import analyzer_agent
from agents.insight_generator import insight_agent
from agents.report_generator import report_agent



def run_pipeline(df):
    cleaned_data = cleaner_agent.invoke(df)
    analysis_results = analyzer_agent.invoke(cleaned_data)
    insights = insight_agent.invoke(analysis_results)
    report = report_agent.invoke(insights)
    print("Pipeline completed successfully.")
    print("Generated Report:", report)  
    return report

pd.read_csv('mock.csv').pipe(run_pipeline)
