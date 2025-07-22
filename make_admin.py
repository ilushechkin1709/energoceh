from app import db, User, app

with app.app_context():
    user = User.query.filter_by(username='admin').first()
    if user:
        user.role = 'admin'
        db.session.commit()
        print("Пользователь 'admin' назначен администратором!")
    else:
        print("Пользователь 'admin' не найден.")