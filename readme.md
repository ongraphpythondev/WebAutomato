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
Date,EmployeeName,Plan,PolicyNumber,Premium
05/01/2023,John Doe,Gold,AB-12345,150.0
05/02/2023,Jane Smith,Silver,CD-67890,100.0
05/03/2023,Michael Brown,Bronze,EF-10111,50.0
05/04/2023,Alice Johnson,Gold,GH-12121,150.0
05/05/2023,Bob Wilson,Silver,IJ-13131,100.0
05/06/2023,Carol Martinez,Bronze,KL-14141,50.0
05/07/2023,David Anderson,Gold,MN-15151,150.0
05/08/2023,Eva Thomas,Silver,OP-16161,100.0
05/09/2023,Frank Jackson,Bronze,QR-17171,50.0
05/10/2023,Grace White,Gold,ST-18181,150.0

```
