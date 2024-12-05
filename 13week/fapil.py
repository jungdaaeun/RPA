from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}

from fastapi import Form
@app.post("/user")
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    return {"msg": f"{major} {name}님 ({studentcode})"}

from fastapi import File, UploadFile
import shutil
from pathlib import Path

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"filename": file.filename, "location": str(save_path)}

from fastapi import File, UploadFile
import shutil
from pathlib import Path
from fastapi.responses import FileResponse

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = Path("static/uploads") / filename
    if file_path.is_file():
        return FileResponse(path=file_path, filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")

def loginDB(userId, userPassword):
    import sqlite3
    
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(query, (userId, userPassword))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print("Login successful!")
        print("User Info:", result)
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False
    
@app.post("/login")
def login_form(userid: str = Form(...), userpassword: str = Form(...)):
    result = loginDB (userid, userpassword)
    
    if result == True :
        return {"msg": f"{userid}님 반갑습니다."}
    else :
        return {"msg": f"로그인에 실패했습니다."}


from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001, log_level="info")