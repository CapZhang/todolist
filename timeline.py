from www.init.init_app import app
from www.DB.db_script.CRUD import db,User,ToDoDetails,insert_ToDoDetails
from flask import jsonify

@app.route("/<int:index>",methods=["GET"],endpoint="index")
def index(index):
    if User.query.get(index):
        return User.query.get(1).username
    else:
        return "查无此ID"

@app.route("/todo/<status>",methods=["GET"],endpoint="get_todo_details")  
def get_todo_details(status):
    res = ToDoDetails.query.filter(ToDoDetails.status==status).all()
    if res:
        json_data = []
        for res_temp in res:
            data = {
                "name": res_temp.name,
                "create_time": res_temp.create_time,
                "status": res_temp.status,
                "level": res_temp.status,
                "sub_todo_id": res_temp.sub_todo_id,
                "start_time": res_temp.start_time,
                "end_time": res_temp.end_time,
                "use_time": res_temp.use_time,
                "progress_bar": res_temp.progress_bar,
            }
            json_data.append(data)
            print(json_data)
        return jsonify(json_data)
    else:
        return "没有这个状态"