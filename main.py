from fastapi import FastAPI, File, UploadFile
from dectector import gunDetector

app = FastAPI()

@app.post('/uploadfile')
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as image :
        content = await file.read()
        image.write(content)
        image.close()

    gunDetector(file.filename)
    return {"filename": file.filename}