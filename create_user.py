from app import db, User, app  # Импортируем приложение и базу данных

# Создание нового пользователя
with app.app_context():  # Оборачиваем код в контекст приложения
    user = User(username="admin", password="admin123")
    db.session.add(user)
    db.session.commit()

    print("Пользователь admin успешно создан!")
