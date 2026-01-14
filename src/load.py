import pandas as pd
from .config import RAW_DATA_DIR, PROCESSED_DATA_FILE

def load_sensor_locations() -> pd.DataFrame:
    sensor_locations_path =  RAW_DATA_DIR / 'pedestrian-counting-system-sensor-locations.parquet'
    if sensor_locations_path.exists():
        sensor_locations = pd.read_parquet(sensor_locations_path)

        return sensor_locations
    else:
        raise FileExistsError("Sensor Location Data does not exist")

def load_historic_sensor_counts(n_entries=-1) -> pd.DataFrame:
    sensor_count_path =  RAW_DATA_DIR / 'Pedestrian_Counting_System_Monthly_counts_per_hour_may_2009_to_14_dec_2022.csv'
    if sensor_count_path.exists():
        if (n_entries >= 0):
            sensor_counts = pd.read_csv(sensor_count_path, nrows=n_entries)
        else:
            sensor_counts = pd.read_csv(sensor_count_path)
        
        return sensor_counts
    else:
        raise FileExistsError("Sensor Count Data does not exist")

def load_sensor_counts() -> pd.DataFrame:
    sensor_count_path =  RAW_DATA_DIR / 'pedestrian-counting-system-monthly-counts-per-hour.parquet'
    if sensor_count_path.exists():
        sensor_counts = pd.read_parquet(sensor_count_path)
        
        return sensor_counts
    else:
        raise FileExistsError("Sensor Count Data does not exist")
    
def load_processed() -> pd.DataFrame:
    if PROCESSED_DATA_FILE.exists():
        sensor_counts = pd.read_parquet(PROCESSED_DATA_FILE)
        sensor_counts['sensor_id'] = sensor_counts['sensor_id'].astype('category')

        return sensor_counts
    else:
        raise FileExistsError("Processed data does not exist")