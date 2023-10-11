from flask import (
    jsonify,
    render_template,
    request,
)

from app import app, db

from app.models.models import (
    User,
    Post,
)
from app.schemas.schema import (
    PostSchema,
    UserSchema,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<id_user>',methods=['PUT','DELETE','PATCH'])
def users(id_user):
    if request.method == 'GET':
        return jsonify(Mensaje=f'Recibi un GET')

    if request.method == 'PUT':
        return jsonify(Mensaje=f'Recibi un PUT')
    
    if request.method == 'DELETE':
        return jsonify(Mensaje=f'Recibi un DELETE')
    
    if request.method == 'PATCH':
        return jsonify(Mensaje=f'Recibi un PATCH')
    

@app.route('/user', methods=['POST', 'GET'])
def users():

    if request.method == "POST":
        data = request.get_json()
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el usuario {username}")

    if request.method == "GET":
        users = User.query.all()
        users_schema = UserSchema().dump(users, many=True)
        return jsonify(users_schema)


@app.route('/post', methods=['POST', 'GET'])
def posts():
    if request.method == "POST":
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        user = data.get('user_id')

        new_post = Post(
            title=title,
            content=content,
            user=user
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify(Mensaje="Nuevo post creado")

    if request.method == "GET":
        posts = Post.query.all()
        posts_schema = PostSchema().dump(posts, many=True)
        return jsonify(posts_schema)
    

