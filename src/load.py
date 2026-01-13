from pathlib import Path
import pandas as pd

CURRENT_PATH = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_PATH.parent.parent
DATA_DIR = PROJECT_ROOT / 'data'

def load_sensor_locations() -> pd.DataFrame:
    sensor_locations_path =  DATA_DIR / 'pedestrian-counting-system-sensor-locations.parquet'
    if sensor_locations_path.exists():
        sensor_locations = pd.read_parquet(sensor_locations_path)
        return sensor_locations
    else:
        raise FileExistsError("Sensor Location Data does not exist")
    
def load_sensor_counts() -> pd.DataFrame:
    sensor_count_path =  DATA_DIR / 'pedestrian-counting-system-monthly-counts-per-hour.parquet'
    if sensor_count_path.exists():
        sensor_counts = pd.read_parquet(sensor_count_path)
        return sensor_counts
    else:
        raise FileExistsError("Sensor Count Data does not exist")