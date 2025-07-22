# временный скрипт admin_set.py
from app import db, User, app

with app.app_context():
    user = User.query.filter_by(username='admin').first()
    if user:
        user.role = 'admin'
        db.session.commit()
        print("Роль обновлена до admin")