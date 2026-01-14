import pandas as pd

from .config import PROCESSED_COUNTS_FILE, PROCESSED_LOCATIONS_FILE

def load_processed_count() -> pd.DataFrame:
    if PROCESSED_COUNTS_FILE.exists():
        sensor_counts = pd.read_parquet(PROCESSED_COUNTS_FILE)
        sensor_counts['sensor_id'] = sensor_counts['sensor_id'].astype('category')

        return sensor_counts
    else:
        raise FileExistsError("Processed counts does not exist")
    
def load_processed_locations() -> pd.DataFrame:
    if PROCESSED_COUNTS_FILE.exists():
        sensor_counts = pd.read_parquet(PROCESSED_LOCATIONS_FILE)
        sensor_counts['sensor_id'] = sensor_counts['sensor_id'].astype('category')

        return sensor_counts
    else:
        raise FileExistsError("Processed locations does not exist")