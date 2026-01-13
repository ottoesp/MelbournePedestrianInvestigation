import pandas as pd

def get_loc_counts(sensor_locations: pd.DataFrame, sensor_counts: pd.DataFrame) -> pd.DataFrame:
    loc_counts = pd.merge(
        sensor_locations, sensor_counts,
        how='inner', on='location_id'
    )

    return loc_counts