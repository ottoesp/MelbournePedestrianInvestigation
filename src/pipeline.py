
import pandas as pd
import sys

from .load import  load_historic_sensor_counts, load_sensor_locations, load_sensor_counts
from .clean import clean_historic_sensor_counts, clean_sensor_locations, clean_current_sensor_counts
from .transform import aggregate_daily_count, join_historic_current_counts

from .config import PROCESSED_COUNTS_FILE, PROCESSED_LOCATIONS_FILE

def run_counts_pipeline(write_to_file = False) -> pd.DataFrame:
    historic_counts_raw = load_historic_sensor_counts()
    historic_counts_clean = clean_historic_sensor_counts(historic_counts_raw)

    current_counts_raw = load_sensor_counts()
    current_counts_clean = clean_current_sensor_counts(current_counts_raw)

    counts_hourly = join_historic_current_counts(current_counts_clean, historic_counts_clean)
    counts = aggregate_daily_count(counts_hourly)
    
    print(counts.info())
    if write_to_file:
        counts.to_parquet(path=PROCESSED_COUNTS_FILE)

    return counts

def run_locations_pipeline(write_to_file = False) -> pd.DataFrame:
    locations_raw = load_sensor_locations()
    locations = clean_sensor_locations(locations_raw)

    # print(locations.info())
    if write_to_file:
        locations.to_parquet(path=PROCESSED_LOCATIONS_FILE)

    return locations

if __name__ == "__main__":
    write_to_file = False
    if '-w' in sys.argv[1:]:
        write_to_file = True    

    run_counts_pipeline(write_to_file)
    run_locations_pipeline(write_to_file)