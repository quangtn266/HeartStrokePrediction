# HeartStrokePrediction

The demo will use AI model to predict Heart Stroke.

# Configuration.
1. Gerate a .env file with configuration of database and fastapi.

2. Create a database.
```
createdb tdd -U postgres
```

3. cd to the postgres directory and run createdb.py to create table.
```
cd ./postgres

python createdb.py
```

4. cd to the stroke_api
```
uvicorn  main:app --host 0.0.0.0 --port 8005
```

5. main directory.
```
streamlit run web_interface.py --server.port 8010
```
