from feast import Entity
from feast.types import Int64

user = Entity(
    name="user_id",
    description="Unique user identifier",
    value_type=Int64,
)
