from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import argparse
import pandas as pd
import os
from io import StringIO
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

def convert_table(source_csv, template_csv, target_csv):

    df1=pd.read_csv(source_csv).to_string()
    df2=pd.read_csv(template_csv).head().to_string()
    print(type(df1),type(df2))
    print(df1)
    print(df2)
    template='''Your task is to take this Dataframe2 as a template dataframe and transform dataframe1 values in dataframe2 template, Do it in this manner that it cover every row of dataframe1. 

                     Output Instructions: 
                     1. output Should be the csv data. 
                     2. output should not contain text data.
                     3. output should not contain code.


                     Dataframe1: {dataframe1}
                     Dataframe2: {dataframe2}
                     '''
    print(df2)
    prompt_template=PromptTemplate(input_variables=["dataframe1","dataframe2"],template=template)
    chain = LLMChain(llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY,model='gpt-3.5-turbo'), prompt=prompt_template,verbose=True)
    output=chain.run(dataframe1=df1,dataframe2=df2)
    print(output)    


    df = pd.read_csv(StringIO(output))

    df.to_csv(target_csv,index=False)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a source CSV using a template CSV")
    parser.add_argument("--source", required=True, help="Path to the source CSV file")
    parser.add_argument("--template", required=True, help="Path to the template CSV file")
    parser.add_argument("--target", required=True, help="Path to the target CSV file")

    args = parser.parse_args()

    convert_table(args.source, args.template, args.target)    


# python3 convert_table.py --source ./DATA/table_A.csv --template ./DATA/template.csv --target target.csv    