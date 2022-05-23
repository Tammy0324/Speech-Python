from fastapi import FastAPI, UploadFile, File
import shutil
from typing import List

app = FastAPI()

@app.post('/')
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {"file_name":file.filename}

# @app.post('/play')
# async def upload_play(file: List[UploadFile] = File(...)):
#     for play in files:
#         with open(f'{play.filename}',"wb") as buffer:
#             shutil.copyfileobj(file.file,buffer)
#
#     return {"file_name":file.filename}

@app.get('/')
def index():
    return 'hi!!!'
