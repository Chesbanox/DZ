from fastapi import FastAPI, HTTPException

app = FastAPI()

# Список для зберігання імен
users = []

@app.post("/add_user/")
def add_user(name: str):
    if name in users:
        raise HTTPException(status_code=400, detail="Ім'я вже існує.")
    users.append(name)
    return {"message": f"Ім'я '{name}' додано успішно."}

@app.get("/get_users/")
def get_users():
    return {"users": users}

@app.delete("/delete_user/")
def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="Ім'я не знайдено.")
    users.remove(name)
    return {"message": f"Ім'я '{name}' видалено успішно."}

@app.get("/")
def root():
    return {"message": "Веб-додаток працює!"}