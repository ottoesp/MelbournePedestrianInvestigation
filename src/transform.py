import pandas as pd

def get_loc_counts(sensor_locations: pd.DataFrame, sensor_counts: pd.DataFrame) -> pd.DataFrame:
    # Join location and count
    loc_counts = pd.merge(
        sensor_locations, sensor_counts,
        how='inner', on='sensor_id'
    )
    return loc_counts

def aggregate_daily_count(counts: pd.DataFrame) -> pd.DataFrame:
    counts['sensing_date_time'] = counts['sensing_date_time'].dt.normalize() # pyright: ignore[reportAttributeAccessIssue]
    daily_count = (
        counts.groupby(['sensor_id', 'sensing_date_time'])
        .sum(numeric_only=True)
    )
    
    daily_count = daily_count.reset_index()

    daily_count = daily_count.rename(columns={
        'sensing_date_time' : 'sensing_date',
        'hourly_count' : 'daily_count'
    })

    return daily_count