import sqlalchemy as sa

metadata = sa.MetaData()

iris_data_table = sa.Table(
    "iris_data",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column("sepal_length", sa.Float),
    sa.Column("sepal_width", sa.Float),
    sa.Column("petal_length", sa.Float),
    sa.Column("petal_width", sa.Float),
    sa.Column("target", sa.Integer),
)
