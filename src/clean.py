import pandas as pd

def clean_sensor_locations(locations: pd.DataFrame) -> pd.DataFrame:
    locations = locations.rename(columns={
        'location_id' : 'sensor_id'
    })
    locations['installation_date'] = pd.to_datetime(
        locations['installation_date']
    )
    locations = locations.drop(
        columns=['note', 'direction_1', 'direction_2', 'latitude', 'longitude', 'status', 'location_type']
    )

    # Dataset includes the same id for multiple directions of a single sensor
    locations = locations.drop_duplicates(subset=['sensor_id'])

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

def clean_historic_sensor_counts(counts: pd.DataFrame) -> pd.DataFrame:
    
    # Rename and convert types first
    counts = counts.rename(columns={
        'Date_Time': 'sensing_date_time',
        'ID': 'count_id',
        'Sensor_ID' : 'sensor_id',
        'Hourly_Counts' : 'hourly_count',
        'Day': 'day'
    })

    counts['sensing_date_time'] = pd.to_datetime(
        counts['sensing_date_time'], 
        format='%B %d, %Y %I:%M:%S %p'
    )

    # Drop unnecessary columns
    counts = counts.drop(columns=['Year', 'Month', 'Mdate', 'Time', 'Sensor_Name'])

    # Set the index last (this moves 'count_id' out of the columns list)
    counts = counts.set_index('count_id')

    return counts