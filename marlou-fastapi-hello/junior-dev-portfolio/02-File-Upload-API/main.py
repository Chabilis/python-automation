# main.py - File Upload API (FIXED VERSION)
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import pandas as pd
import io

app = FastAPI(
    title="Marlou's File Upload API",
    description="Junior Web Dev Portfolio #2 – Upload Excel/CSV → Get JSON",
    version="1.0"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Marlou's File Upload API</h1>
    <p>Upload Excel (.xlsx) or CSV files only</p>
    <form action="/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file" accept=".xlsx,.csv">
        <input type="submit" value="Upload & Analyze">
    </form>
    <p><a href="/docs">Interactive Docs</a></p>
    """

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        
        if file.filename.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(contents))
        elif file.filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(io.BytesIO(contents))
        else:
            return {
                "error": "Unsupported file type",
                "filename": file.filename,
                "supported": [".csv", ".xlsx", ".xls"],
                "message": "Please upload Excel or CSV only"
            }

        return {
            "filename": file.filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "preview": df.head(5).to_dict(orient="records"),
            "message": "File processed successfully by Marlou!"
        }
        
    except Exception as e:
        return {
            "error": "Failed to process file",
            "details": str(e),
            "tip": "Make sure it's a valid Excel/CSV file"
        }