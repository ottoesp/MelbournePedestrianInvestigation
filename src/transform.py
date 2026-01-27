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

    aggregation_rules = {
        'day': 'first',
        'hourly_count' : 'sum'
    }

    daily_count = (
        counts.groupby(['sensor_id', 'sensing_date_time'])
        .agg(aggregation_rules)
    )
    
    daily_count = daily_count.reset_index()

    daily_count = daily_count.rename(columns={
        'sensing_date_time' : 'sensing_date',
        'hourly_count' : 'daily_count'
    })

    return daily_count

def join_historic_current_counts(historic: pd.DataFrame, current: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([historic, current])

def limit_to_selected_years(counts: pd.DataFrame, year_1: int, year_2: int) -> pd.DataFrame:
    common_sensors = (
        set(counts[counts['sensing_date'].dt.year == year_1]['sensor_id'].unique()) 
        & set(counts[counts['sensing_date'].dt.year == year_2]['sensor_id'].unique())
    )

    # Filter to only those sensors
    counts_with_common_dates = counts[counts['sensor_id'].isin(common_sensors)]

    # Limit to only 2019 and 2025 with non-zero values
    selected_counts: pd.DataFrame = (
        counts_with_common_dates[
            counts_with_common_dates['sensing_date'].dt.year.isin([year_1, year_2])
        ].query('daily_count > 0')
    )
    selected_counts['year'] = selected_counts['sensing_date'].dt.year.astype('category')

    return selected_counts

def drop_unlocated_sensors(counts: pd.DataFrame, locations: pd.DataFrame):
    bad_sensors = pd.Index(counts['sensor_id']).difference(locations['sensor_id'])
    return counts[~counts['sensor_id'].isin(bad_sensors)]