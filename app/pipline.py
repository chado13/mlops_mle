from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
from app.tables import iris_data_table
import sqlalchemy as sa
import pandas as pd

db = create_engine("postgresql://user:password@dg:5431/mydatabase")


def fetch_data() -> pd.DataFrame:
    """Fetch data from database"""
    with db.connect() as conn:
        query = sa.select([iris_data_table])
        df = pd.read_sql(query, conn)
    return df


def select_train_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select the data we want to use for modeling"""
    data = df.drop(columns=["id", "created_at", "target"], axis=1)
    return data

def select_vaild_data(df: pd.DataFrame) -> pd.DataFrame:
    data = df[]

