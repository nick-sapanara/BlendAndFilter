user = User.get(current_user.id)
user.about_me = form.about_me.data
db.session.add(user)
db.session.commit()