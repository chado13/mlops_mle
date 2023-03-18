import time
from typing import Any

import pandas as pd
import sqlalchemy as sa
from sklearn.datasets import load_iris
from sqlalchemy import create_engine

from app.config import DB_URL
from app.tables import iris_data_table

engine = create_engine(DB_URL)


def get_data() -> pd.DataFrame:
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
    }
    df = df.rename(columns=rename_rule)
    return df


def insert_data(data: dict[str, Any]) -> None:
    query = sa.insert(iris_data_table).values(**data)
    with engine.begin() as conn:
        conn.execute(query)


def generate_data(df: pd.DataFrame) -> None:
    while True:
        data = df.sample(1).to_dict(orient="records")[0]
        insert_data(data)
        time.sleep(1)


def main() -> None:
    data = get_data()
    generate_data(data)


if __name__ == "__main__":
    main()
