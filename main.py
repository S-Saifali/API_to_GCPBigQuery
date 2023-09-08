import requests
import io
from google.cloud import bigquery

csv_url = 'https://data.sfgov.org/api/views/rkru-6vcg/rows.csv?accessType=DOWNLOAD'

# Initialize a BigQuery client
client = bigquery.Client()

# Define the table ID (replace with your actual project, dataset, and table names)
table_id = 'banded-nimbus-398410.airport_dataset.Airport_table'

# Fetch the CSV data
response = requests.get(csv_url)
data = response.text

# Load data into BigQuery
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,  # Skip the header row
    autodetect=True,  # Automatically detect schema
)

job = client.load_table_from_file(io.StringIO(data), table_id, job_config=job_config)
job.result()  # Waits for the job to complete

print(f'Data loaded into {table_id}')

