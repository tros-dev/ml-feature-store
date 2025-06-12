import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")

def ingest_batch_features(df: pd.DataFrame):
    df = df.rename(columns={"user_id": "user_id"})
    df = df[['user_id', 'avg_session_length', 'total_sessions', 'event_timestamp']]
    store.apply([user_features_view])
    store.write_offline_features(df, user_features_view.name)
