import pandas as pd
import re

def parse_message(field):
    subfields = re.split(r'\[nl\]|\[np\]', field)
    return ' '.join(subfields)

def parse_csv(file_path):
    df = pd.read_csv(file_path, sep=';', header=None).iloc[:, :-1]
    df.columns = ['Timestamp', 'Sign ID', 'Location', 'Logic State', 'Message', 'Transit Alert IDs', 'Transit Parking TT', 'Highway TT', 'Transit Departure Time', 'Transit Arrival Time', 'Total Transit TT', 'Highway/Transit Ratio']
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Message'] = df['Message'].apply(parse_message)
    df = df[(df['Timestamp'].dt.hour >= 6) & (df['Timestamp'].dt.hour <= 10)]
    faster_route = df[df['Message'].str.contains('FASTER ROUTE')]
    return df, faster_route