from fastapi import FastAPI,File,UploadFile
app=FastAPI()
from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Welcome to the CSV Analyzer API"}

@app.post('/analyze')
async def analyze_csv(file:UploadFile=File(...)):
    contents=await file.read()
    contents=contents.decode('utf-8')
    return contents

