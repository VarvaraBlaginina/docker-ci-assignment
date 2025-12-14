# CI процесс с созданием Docker-образа

## ВЫПОЛНЕНО:

1. СОЗДАН GIT РЕПОЗИТОРИЙ:
   - URL: https://github.com/VarvaraBlaginina/docker-ci-assignment.git
   - Содержит файлы:
   - Dockerfile - конфигурация Docker образа
   - Jenkinsfile - Pipeline скрипт CI/CD
   - build.sh - скрипт сборки
   - app.py - исходный код приложения

2. НАСТРОЕН CI/CD PROCESS В JENKINS:
   - Pipeline: docker-ci-pipeline
   - Автоматически получает код из Git репозитория
   - Собирает Docker образ по Dockerfile
   - Запускает тесты приложения

3. ПРОЦЕСС РАБОТЫ:
   1) Jenkins клонирует репозиторий из GitHub
   2) Выполняет сборку Docker образа
   3) Запускает контейнер для проверки
   4) Выводит результат работы приложения

4. ДОКАЗАТЕЛЬСТВА (скриншоты):
   - Git репозиторий с файлами
   - Успешная сборка в Jenkins
   - <img width="1185" height="589" alt="image" src="https://github.com/user-attachments/assets/57cfaa0b-477c-42b8-9d51-9d4746ea780a" />
   - Логи выполнения (Console Output)
     <img width="691" height="703" alt="image" src="https://github.com/user-attachments/assets/e2e76296-ca4e-4ccf-a6f8-7eed74de80a9" />
   - Созданные Docker образы
     <img width="890" height="70" alt="image" src="https://github.com/user-attachments/assets/f287d4b2-47cc-41de-a6d3-73220912a531" />

