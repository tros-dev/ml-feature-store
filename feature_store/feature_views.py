from feast import FeatureView, Field
from feast.types import Int64, Float64
from entities import user

user_features_view = FeatureView(
    name="user_features",
    entities=["user_id"],
    ttl=None,
    schema=[
        Field(name="avg_session_length", dtype=Float64),
        Field(name="total_sessions", dtype=Int64),
    ],
)
