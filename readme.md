# Instructions

### Create python environment and activate it
```
python3.9 -m venv venv
source venv\bin\activate
```
### Install dependencies

```
pip install -r requirements.txt
```

### Add your openai api key in .env.EXAMPLE file and Rename it .env file
```
OPENAI_API_KEY= <ADD YOUR OPENAI_API_KEY>
```


### Then run the below command

``` 
python3 convert_table.py --source ./DATA/table_A.csv --template ./DATA/template.csv --target target.csv    
```



### This is the output return by the openai model
```
```python
df3 = pd.DataFrame()
df3['Date'] = pd.to_datetime(df1['Date_of_Policy']).dt.strftime('%d-%m-%Y')
df3['EmployeeName'] = df1['FullName']
df3['Plan'] = df1['Insurance_Plan'].str.replace(' Plan', '')
df3['PolicyNumber'] = df1['Policy_No'].str.replace('-', '')
df3['Premium'] = df1['Monthly_Premium'].astype(float)
df3

```