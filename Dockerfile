# Используем базовый образ с Python
FROM python:3.9-slim

# Создаем пользователя с UID 1001 (без имени пользователя)
RUN adduser --uid 1001 --disabled-password --gecos "" --no-create-home myuser

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Изменяем владельца файлов на пользователя с UID 1001
RUN chown -R 1001:1001 /app

# Переключаемся на пользователя с UID 1001
USER 1001

# Открываем порт 8000
EXPOSE 8000

# Указываем точку входа для контейнера
ENTRYPOINT ["python3", "server.py"]

