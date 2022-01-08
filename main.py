from io import BytesIO

from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from starlette.responses import HTMLResponse
import pandas as pd
from data import parse_csv

app = FastAPI()


# Def to send a message after the task is done
def send_message(message):
    print("Sending message:", message)


@app.post("/uploadfile")
async def create_upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    try:
        content = pd.read_csv(BytesIO(file.file.read()))
        background_tasks.add_task(send_message, "File Uploaded")
        data1 = parse_csv(content)
        background_tasks.add_task(send_message, "Task Done")
        return {"Success ": send_message}
    except Exception as e:
        background_tasks.add_task(send_message, "Error")
        return {"Error ": send_message}


@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile" method="post" enctype="multipart/form-data">
<input name="file" type="file" >
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
