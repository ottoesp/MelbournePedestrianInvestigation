import pandas as pd
from pathlib import Path

# Victorian government COVID-19 lockdown dates
# Sourced at https://lds.inspiredesign.au/timeline/
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

# Australian Beaureu of Statistics Population estimates by SA2 and above, 2001 to 2024
# Sourced at https://www.abs.gov.au/statistics/people/population/regional-population/2023-24#interactive-maps
MELBOURNE_POPULATION = pd.DataFrame({
    'year': ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    'greater_melbourne' : [3500249, 3545579, 3594031, 3641951, 3697372, 3760760, 3841760, 3931438, 4031787, 4105857, 4169366, 4265843, 4370067, 4476030, 4586012, 4714387, 4820116, 4916589, 5006457, 5061107, 4975319, 5039661, 5208068, 5350705],
    'inner_melbourne' : [431549, 441412, 450686, 460547, 470414, 480345, 492684, 505194, 518026, 526230, 532351, 549795, 571493, 592422, 611882, 633471, 649010, 661331, 670256, 670684, 626913, 636905, 676193, 702853]
})

SRC_DIR = Path(__file__).resolve()
PROJECT_ROOT = SRC_DIR.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / 'data' / 'raw'

PROCESSED_DATA_DIR = PROJECT_ROOT / 'data' / 'processed'
PROCESSED_COUNTS_FILE = PROCESSED_DATA_DIR / 'counts.parquet'
PROCESSED_LOCATIONS_FILE = PROCESSED_DATA_DIR / 'locations.parquet'

WEBAPP_RESOURCES_DIR = PROJECT_ROOT / 'webapp' / 'resources'
