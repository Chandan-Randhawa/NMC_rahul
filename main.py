from fastapi import FastAPI , HTTPException
import csv
import os
import uvicorn

app = FastAPI()

origins = ['*']


@app.get('/csvtojson' )
def csv_to_json():
    try:
        datas = []
        with open('NMC data v2.csv', encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                datas.append(rows)
        # print(datas)
        return datas
    except Exception as e:
        print (e)
        raise HTTPException(status_code= 404 , detail='Internal server error')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
