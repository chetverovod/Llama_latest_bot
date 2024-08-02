# Запускаем бот с ИИ
Ollama - фреймворк для запуска и управления большими языковыми моделями (LLM) на локальных вычислительных ресурсах. Он обеспечивает загрузку и развертывание выбранной LLM и доступ к ней через API.

## Установка Ollama
https://hostkey.ru/documentation/technical/gpu/ollama/

После установки Ollama будет доступна по адресу:
http://127.0.0.1:11434 или http://<IP_адрес_сервера>:11434.

### Установка модели Llama3.1 8B
При первом запуске модели будет выполнено её автоматическое скачивание:
```
ollama run llama3.1
```
Будет скачано 4,7ГБ
После скчивания модель запуститься и появится приглашение к диалогу с моделью.

# Llama_latest_bot

```shell
python3.11 -m venv venv_bot
echo "aiogram<4.0" > requirements.txt
echo "pydantic-settings" >> requirements.txt
echo "ollama" >> requirements.txt
source venv_bot/bin/activate
pip install -r requirements.txt 
```

## Регистрируем бота
Зайдите в Телеграм-канал @BotFather и зарегистрируйте своего
уникального бота и чкоаируйте токен который будет вам выдан.
его нужно будет подставить в скрипт *Llama_latest_bot.py* в строку:

```python
 bot = Bot(token="МЕСТО ДЛЯ ТОКЕНА")
```
Запускаем нашего бота
```shell
python  Llama_latest_bot.py
```
Бежим в Телеграм общаться с нашим ботом.

## Ollama REST API
https://github.com/ollama/ollama/blob/main/docs/api.md

## Ollama Python API
https://github.com/ollama/ollama-python

