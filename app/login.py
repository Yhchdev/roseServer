from flask import Flask,request,jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

from model import *

app = Flask(__name__)
api = Api(app)
# 支持跨域
CORS(app, supports_credentials=True)

TODOS = {
    'todo1': {'task': '国赛'},
    'todo2': {'task': '公司'},
    'todo3': {'task': '学校'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

##################################################################################################################

class Sing(Resource):
    # 根据用户名和密码查询，用于登录
    def post(self):

        # 获取用户名和密码
        name = request.json.get("name")
        password = request.json.get("password")

        # 调用User类的查询方法
        user = User()
        one = user.queryObject(name,password)
        if(one!=None):

            return {"msg": "ok"}
        else:
            return {"msg": "error"}





api.add_resource(Sing, '/login')





if __name__ == '__main__':
    app.run(debug=True)