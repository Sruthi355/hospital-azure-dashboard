import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import urllib

# === Step 1: Connect to local SQL Server ===
local_conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=RealTimePatientDB;"
    "Trusted_Connection=yes;"
)

try:
    local_conn = pyodbc.connect(local_conn_str)
    print("✅ Connected to Local SQL Server.")
except Exception as e:
    print("❌ Failed to connect to local SQL Server:", e)
    exit()

# === Step 2: Fetch patient records ===
try:
    query = "SELECT * FROM patients"
    df_patients = pd.read_sql(query, local_conn)
    print(f"✅ Fetched {len(df_patients)} records from local Patients table.")
except Exception as e:
    print("❌ Failed to fetch data from local SQL Server:", e)
    exit()

# === Step 3: Connect to Azure SQL Database using SQLAlchemy ===

# Replace with your actual Azure SQL credentials
username = "Sruthi"
password = "Harry@1910"
server = "hospitaldev.database.windows.net"
database = "RealTimePatientDB"

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

azure_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# === Step 4: Upload to Azure SQL ===
try:
    df_patients.to_sql("Patients", con=azure_engine, if_exists="append", index=False)
    print("✅ Data successfully uploaded to Azure SQL Database.")
except Exception as e:
    print("❌ Failed to upload data to Azure SQL:", e)