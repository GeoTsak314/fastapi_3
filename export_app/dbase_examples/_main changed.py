
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from export_app.file_converter import convert_to_json
import json
import os
import csv
import pandas as pd

app = FastAPI()

@app.post("/export")
async def export_data(file: UploadFile = File(...), format: str = "json"):
    try:
        data = await convert_to_json(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    output_path = f"exported_data.{format}"

    if format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    elif format == "csv":
        with open(output_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    elif format == "xlsx":
        df = pd.DataFrame(data)
        df.to_excel(output_path, index=False)
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")

    return FileResponse(output_path, filename=output_path)
