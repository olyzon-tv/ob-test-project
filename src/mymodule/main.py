from pydantic import BaseModel
from pyiceberg.catalog import load_catalog


def add(a, b):
    return a + b


class AddRequest(BaseModel):
    a: int
    b: int


warehouse_path = "/tmp/warehouse"
catalog = load_catalog(
    "default",
    **{
        "type": "sql",
        "uri": f"sqlite:///{warehouse_path}/pyiceberg_catalog.db",
        "warehouse": f"file://{warehouse_path}",
    },
)
