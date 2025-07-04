---
tags: [note/python]
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, September 6th 2024, 11:53:26 pm
---

## Importing Data
| Function                               | Description                                            | Notes |
| -------------------------------------- | ------------------------------------------------------ | ----- |
| `df.read_dsv('filename')`              | Reads in a csv and converts it to a dataframe          |       |
| `df.to_excel('filename', 'sheetName')` | Outputs a dataframe to excel                           |       |
| `data = pd.read_html(url)`             | Reads an HTML (website) and converts it to a dataframe |       |

You'll need to use dependent libraries to import stuff

### sqlalchemy

``` python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
sqldf = pd.read_squl('mytable_', con=engine)

```


## Writing Data

Finally, there are numerous methods you can transfer your data once your analysis has provided results:

| Writing Data Functions                   | Description                     |
| ---------------------------------------- | ------------------------------- |
| df.to_csv(filename)                      | Writes to a CSV file            |
| df.to_excel(filename)                    | Writes to an Excel file         |
| df.to_sql(table_name, connection_object) | Writes to a SQL table           |
| df.to_json(filename)                     | Writes to a file in JSON format |
| df.to_html(filename)                     | Saves as an HTML table          |
| df.to_clipboard()                        | Writes to the clipboard         |