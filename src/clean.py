import pandas as pd

def clean_sensor_locations(locations: pd.DataFrame) -> pd.DataFrame:
    locations['installation_date'] = pd.to_datetime(
        locations['installation_date']
    )
    locations = locations.drop(
        columns=['note', 'direction_1', 'direction_2', 'latitude', 'longitude', 'status']
    )

    return locations

def clean_sensor_counts(counts: pd.DataFrame) -> pd.DataFrame:
    counts['sensing_date_time'] = (
        pd.to_datetime(counts['sensing_date'])
        + pd.to_timedelta(counts['hourday'], unit='h')
    )
    counts = counts.drop(
        # Dropping location as it is redundant with sensor_locations dataset
        columns=['direction_1', 'direction_2', 'location', 'sensing_date', 'hourday']
    )
    counts = counts.rename(columns={
        'total_of_directions' : 'count',
        'id' : 'count_id'
    })

    return counts