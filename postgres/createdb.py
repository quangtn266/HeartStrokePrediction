from database import Base, engine
from datetime import datetime
import pandas as pd
print("Creating database")

Base.metadata.create_all(engine)

file_name = "/Users/quangtn/Desktop/01_work/01_job/02_ml/PySpark/HeartStrokePrediction/data/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(file_name)
df['time'] = datetime.now()
df.to_sql(con=engine, index=False, name='data_trained', if_exists='replace')