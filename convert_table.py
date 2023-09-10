from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
import argparse
import pandas as pd
import os
from io import StringIO
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

def convert_table(source_csv, template_csv, target_csv):
    





    agent = create_csv_agent(
        ChatOpenAI(openai_api_key=OPENAI_API_KEY,temperature=0, model="gpt-4"),
        [source_csv,template_csv],
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION

    )
    print(agent)
    output=agent.run('''Your task is to mapping the df1 to the df2  by transferring values and transforming values into the format of the df2, do this on all rows of df1. 
Output example:           
    Date    EmployeeName         Plan PolicyNumber  Premium
0  01-05-2023        John Doe    Gold Plan      AB12345    150.0
1  02-05-2023      Jane Smith  Silver Plan      CD67890    100.0
2  03-05-2023   Michael Brown  Bronze Plan      EF10111     50.0
3  04-05-2023   Alice Johnson    Gold Plan      GH12121    150.0
4  05-05-2023      Bob Wilson  Silver Plan      IJ13131    100.0
5  06-05-2023  Carol Martinez  Bronze Plan      KL14141     50.0
6  07-05-2023  David Anderson    Gold Plan      MN15151    150.0
7  08-05-2023      Eva Thomas  Silver Plan      OP16161    100.0
8  09-05-2023   Frank Jackson  Bronze Plan      QR17171     50.0
9  10-05-2023     Grace White    Gold Plan      ST18181    150.0

Instruction for output:
                     1. it only contain the transformed dataframe of df1.
                     2. it doen't anything than the transformed dataframe of df1.
                     3. the output structure should match the example.
                     4. don't return the code


''')
    print(output)
    df = pd.read_csv(StringIO(output), delim_whitespace=True, skipinitialspace=True)
    df.to_csv(target_csv)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a source CSV using a template CSV")
    parser.add_argument("--source", required=True, help="Path to the source CSV file")
    parser.add_argument("--template", required=True, help="Path to the template CSV file")
    parser.add_argument("--target", required=True, help="Path to the target CSV file")

    args = parser.parse_args()

    convert_table(args.source, args.template, args.target)    


# python3 convert_table.py --source ./DATA/table_A.csv --template ./DATA/template.csv --target target.csv    