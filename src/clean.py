import pandas as pd

def clean_sensor_locations(locations: pd.DataFrame) -> None:
    locations['installation_date'] = pd.to_datetime(
        locations['installation_date']
    )

