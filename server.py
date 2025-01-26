import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Переопределяем обработчик запросов
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Генерация HTML страницы с текстом "Привет"
        self.send_response(200)  # Статус 200 (OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Генерируем HTML с приветствием
        html_content = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Привет</title>
        </head>
        <body>
            <h1>Привет!</h1>
            <p>Добро пожаловать на наш сервер!</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))  # Отправляем HTML-контент

# Запускаем сервер на порту 8000
def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

