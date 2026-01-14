
import pandas as pd
import sys

from .load import  load_historic_sensor_counts, load_sensor_locations
from .clean import clean_historic_sensor_counts, clean_sensor_locations
from .transform import aggregate_daily_count

from .config import PROCESSED_DATA_FILE

def run_pipeline(write_to_file = False) -> pd.DataFrame:
    sensor_counts_raw = load_historic_sensor_counts()

    sensor_counts_clean = clean_historic_sensor_counts(sensor_counts_raw)
    counts = aggregate_daily_count(sensor_counts_clean)
    
    print(counts.info())
    if write_to_file:
        counts.to_parquet(path=PROCESSED_DATA_FILE)

    return counts

if __name__ == "__main__":
    write_to_file = False
    if '-w' in sys.argv[1:]:
        write_to_file = True    

    run_pipeline(write_to_file)