from base64 import encode
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from os import listdir
import sys, os
from datetime import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv

# env
project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(project_folder, ".env"))

# from env
cnnhost = os.getenv("SQL_HOST")
cnnport = os.getenv("SQL_PORT")
cnndb = os.getenv("SQL_DBSTAGE")
cnnuser = os.getenv("SQL_USER")
cnnpwd = os.getenv("SQL_PWD")

# html pandas profiling output folder
dataprofiles = "data-profiles/"

# title prefix
dataprofiles_prefix = "pais"

engine = create_engine(
    "mssql+pyodbc://"
    f"{cnnuser}:{cnnpwd}@{cnnhost}:{cnnport}/{cnndb}?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)

conn = engine.connect()

sql_tables = "SELECT t.name AS name FROM sys.schemas AS s JOIN sys.tables AS t ON t.schema_id = s.schema_id ORDER BY 1"

sql_views = "SELECT v.name as name FROM sys.views as v ORDER BY 1;"

# get list for tables or views
rows = conn.execute(sql_views)

# per row
for row in rows:
    name = row["name"]
    print(name)
    df = pd.read_sql("SELECT * from " + name, engine)
    print(df)
    profile = ProfileReport(df, title=f"{name} Profiling Report", minimal=True)
    profile.to_file(f"{dataprofiles}{dataprofiles_prefix}_{name}.html")
