import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from feature_store.ingestion import ingest_batch_features

def run_batch_feature_computation():
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=7)
    data = fetch_raw_data(start_date, end_date)
    features = engineer_features(data)
    ingest_batch_features(features)

def fetch_raw_data(start_date, end_date):
    # Imagine SQL query or data lake fetch here
    dates = pd.date_range(start_date, end_date)
    data = pd.DataFrame({
        'user_id': np.random.randint(1000, 2000, size=len(dates)),
        'session_length': np.random.rand(len(dates)) * 100,
        'event_date': dates
    })
    return data

def engineer_features(df):
    agg = df.groupby('user_id').agg(
        avg_session_length=pd.NamedAgg(column='session_length', aggfunc='mean'),
        total_sessions=pd.NamedAgg(column='session_length', aggfunc='count'),
    ).reset_index()
    agg['event_timestamp'] = pd.Timestamp.utcnow()
    return agg
