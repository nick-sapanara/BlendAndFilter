from app import app, db

from app.models import User, Shop, User2Shop, City, ReviewDetails

@app.shell_context_processor
def make_shell_context():
   return {'db': db, 'User': User, 'Shop': Shop, 'U2S': User2Shop, 'City': City, 'ReviewDetails': ReviewDetails}
