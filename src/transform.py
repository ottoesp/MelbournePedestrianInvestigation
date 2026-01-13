import pandas as pd
from .config import FIRST_LOCKDOWN_START, LAST_LOCKDOWN_END

def get_loc_counts(sensor_locations: pd.DataFrame, sensor_counts: pd.DataFrame) -> pd.DataFrame:
    loc_counts = pd.merge(
        sensor_locations, sensor_counts,
        how='inner', on='location_id'
    )
    return loc_counts

def categorise_as_pre_and_post_lockdowns(counts: pd.DataFrame) -> pd.DataFrame:
    # counts = counts[(counts['sensing_date_time'] < FIRST_LOCKDOWN_START) | (LAST_LOCKDOWN_END < counts['sensing_date_time'])]
    counts = counts[(counts['sensing_date_time'] > FIRST_LOCKDOWN_START) & (LAST_LOCKDOWN_END > counts['sensing_date_time'])]
    return counts