from fastapi import FastAPI


# Создание основного приложения АИС «Автосервис»
app = FastAPI(
    title="АИС Автосервис",
    description="Информационная система управления автосервисом",
    version="1.0.0"
)


# Главная страница API
@app.get("/", tags=["Главная"])
def read_root():
    return {
        "message": "Добро пожаловать в АИС Автосервис",
        "service": "main_app",
        "status": "Работает"
    }


# Проверка состояния приложения
@app.get("/health", tags=["Проверка"])
def health_check():
    return {
        "status": "ok",
        "service": "main_app"
    }
