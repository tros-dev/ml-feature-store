from feast import FeatureStore

store = FeatureStore(repo_path=".")

def get_user_features(user_id: int):
    entity_rows = [{"user_id": user_id}]
    feature_refs = [
        "user_features:avg_session_length",
        "user_features:total_sessions",
    ]
    features = store.get_online_features(feature_refs, entity_rows)
    result = {k: v for k, v in features.to_dict().items()}
    if not result['user_id']:
        return None
    return result
