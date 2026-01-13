import pandas as pd

# Victorian government COVID-19 lockdown dates
# Source at https://lds.inspiredesign.au/timeline/
LOCKDOWN_DATES: pd.DataFrame = pd.DataFrame({
    'lockdown_start': ['30-03-2020 23:59', '08-07-2020 23:59', '12-02-2021 23:59', '27-05-2021 23:59', '15-07-2021 23:59', '05-08-2021 18:00'],
    'lockdown_end'  : ['12-05-2020 23:59', '27-10-2020 23:59', '17-02-2021 23:59', '10-06-2021 23:59', '27-07-2021 23:59', '21-10-2021 23:59']
})
for col in ['lockdown_start', 'lockdown_end']:
    LOCKDOWN_DATES[col] = pd.to_datetime(
        LOCKDOWN_DATES[col], format='%d-%m-%Y %H:%M'
    )

FIRST_LOCKDOWN_START = LOCKDOWN_DATES.min()['lockdown_start']
LAST_LOCKDOWN_END = LOCKDOWN_DATES.max()['lockdown_end']