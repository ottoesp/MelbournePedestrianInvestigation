
import pandas as pd

from .load import load_sensor_counts, load_sensor_locations
from .clean import clean_sensor_counts, clean_sensor_locations
from .transform import get_loc_counts, categorise_as_pre_and_post_lockdowns

def run_pipeline():
    sensor_locations_raw = load_sensor_locations()
    sensor_counts_raw = load_sensor_counts()

    sensor_locations = clean_sensor_locations(sensor_locations_raw)
    sensor_counts = clean_sensor_counts(sensor_counts_raw)

    loc_counts = get_loc_counts(sensor_locations, sensor_counts)
    print(loc_counts.info())

    relative_to_lockdowns = categorise_as_pre_and_post_lockdowns(loc_counts)
    print(relative_to_lockdowns.info())

    print(loc_counts['sensing_date_time'].min())
    print(sensor_locations['installation_date'].min())

if __name__ == "__main__":
    run_pipeline()