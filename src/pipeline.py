
import pandas as pd
import sys

from .load import  load_historic_sensor_counts, load_sensor_locations, load_sensor_counts
from .clean import clean_historic_sensor_counts, clean_sensor_locations, clean_current_sensor_counts
from .transform import aggregate_daily_count, join_historic_current_counts, limit_to_selected_years, drop_unlocated_sensors

from .config import PROCESSED_COUNTS_FILE, PROCESSED_LOCATIONS_FILE, PROCESSED_DATA_DIR

def run_counts_pipeline() -> tuple[pd.DataFrame, pd.DataFrame]:
    historic_counts_raw = load_historic_sensor_counts()
    historic_counts_clean = clean_historic_sensor_counts(historic_counts_raw)

    current_counts_raw = load_sensor_counts()
    current_counts_clean = clean_current_sensor_counts(current_counts_raw)

    counts_hourly = join_historic_current_counts(current_counts_clean, historic_counts_clean)
    counts = aggregate_daily_count(counts_hourly)

    selected_counts = limit_to_selected_years(counts, 2019, 2025)
    
    print(counts.info())
    print(selected_counts.info())

    return counts, selected_counts

def run_locations_pipeline() -> pd.DataFrame:
    locations_raw = load_sensor_locations()
    locations = clean_sensor_locations(locations_raw)

    

    return locations

def run_pipline(write_to_file = False):
    counts, selected_counts = run_counts_pipeline()
    locations = run_locations_pipeline()

    selected_counts = drop_unlocated_sensors(selected_counts, locations)

    if write_to_file:
        counts.to_parquet(path=PROCESSED_COUNTS_FILE)
        selected_counts.to_parquet(path=PROCESSED_DATA_DIR / 'selected_counts.parquet')

    if write_to_file:
        locations.to_parquet(path=PROCESSED_LOCATIONS_FILE)

if __name__ == "__main__":
    write_to_file = False
    if '-w' in sys.argv[1:]:
        write_to_file = True    

    run_pipline(write_to_file)