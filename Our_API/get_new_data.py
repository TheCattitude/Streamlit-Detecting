# Standard library
import argparse
import os
import sys

# External libraries
import requests
from google.cloud import bigquery
from taxifare.ml_logic.params import LOCAL_DATA_PATH


def get_new_data(month):
    """
    Source local CSVs train_new.csv and val_new.csv alongside with BigQuery tables train_new and val_new for a given month.
    parameter:
    - month: `str` with values in ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
    returns None
    """
    available_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
    if month not in available_months:
        raise ValueError(f'{month} is not a valid month, run `python get_new_data.py -h` for help')

    base_source_url = 'https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/'
    base_source_uri = "gs://datascience-mlops/taxi-fare-ny"

    client = bigquery.Client()
    project = os.environ.get('PROJECT')
    dataset = os.environ.get('DATASET')

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        skip_leading_rows=1
    )

    for split in ['train', 'val']:
        source_url = f'{base_source_url}{split}_{month}.csv'

        # Local
        print(f"⬇️ Fetching new {split} data for {month} ...")
        csv_file = requests.get(source_url, allow_redirects=True)
        destination_file = f'{split}_new.csv'
        destination_path = os.path.join(LOCAL_DATA_PATH, 'raw', destination_file)
        with open(destination_path, 'wb') as file:
            print('💾 Saving CSV locally ...')
            file.write(csv_file.content)
        print('✅ Done\n')

        # Cloud
        table_id = f"{project}.{dataset}.{split}_new"
        print(f'☁️ Filling table {table_id} on BigQuery ...')
        uri = f"{base_source_uri}/{split}_{month}.csv"
        load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config
        )
        load_job.result()
        destination_table = client.get_table(table_id)
        print("✅ Loaded {} rows.\n".format(destination_table.num_rows))

    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get new data from month')
    parser.add_argument('month', type=str, help='A month within jan, feb, mar, apr, may & jun')
    args = parser.parse_args()
    month = sys.argv[1]
    get_new_data(month)
