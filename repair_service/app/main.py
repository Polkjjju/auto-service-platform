from fastapi import FastAPI


# Создание микросервиса «Прозрачный ремонт»
app = FastAPI(
    title="Прозрачный ремонт",
    description=(
        "Микросервис контроля и истории "
        "выполненных ремонтных работ"
    ),
    version="1.0.0"
)


# Главная страница микросервиса
@app.get("/", tags=["Главная"])
def read_root():
    return {
        "message": "Микросервис Прозрачный ремонт работает",
        "service": "repair_service",
        "status": "Работает"
    }


# Проверка состояния микросервиса
@app.get("/health", tags=["Проверка"])
def health_check():
    return {
        "status": "ok",
        "service": "repair_service"
    }
