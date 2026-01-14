
import pandas as pd
import sys

from .load import  load_historic_sensor_counts, load_sensor_locations
from .clean import clean_historic_sensor_counts, clean_sensor_locations
from .transform import get_loc_counts, categorise_as_pre_and_post_lockdowns

from .config import PROCESSED_DATA_FILE

def run_pipeline(write_to_file = False) -> pd.DataFrame:
    sensor_locations_raw = load_sensor_locations()
    sensor_counts_raw = load_historic_sensor_counts()

    sensor_locations = clean_sensor_locations(sensor_locations_raw)
    sensor_counts = clean_historic_sensor_counts(sensor_counts_raw)

    sensor_count_by_location = get_loc_counts(sensor_locations, sensor_counts)

    if write_to_file:
        sensor_count_by_location.to_parquet(path=PROCESSED_DATA_FILE)

    return sensor_count_by_location

if __name__ == "__main__":
    write_to_file = False
    if '-w' in sys.argv[1:]:
        write_to_file = True    

    run_pipeline(write_to_file)