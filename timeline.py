from www.init.init_app import app
from www.DB.db_script.CRUD import db,User,ToDoDetails,datetime,insert_ToDoDetails
from flask import jsonify,request
from datetime import datetime

@app.route("/",methods=["GET"],endpoint="home_page")
def home_page():
    return "<h1> 欢迎来到时间线 </h1>"

@app.route("/api/<int:index>",methods=["GET"],endpoint="index")
def index(index):
    if User.query.get(index):
        return User.query.get(1).username
    else:
        return "查无此ID"

@app.route("/api/todo",methods=["GET"],endpoint="get_todo_details_all")  
def get_todo_details_all():
    res = ToDoDetails.query.filter().all()
    GMT_FORMAT =  '%a, %d %b %Y %H:%M:%S GMT'
    curr_time = datetime.now()
    if res:
        json_data = []
        for res_temp in res:
            # datetime_create_time = res_temp.create_time
            # if res_temp.create_time:
            #     res_temp.create_time=res_temp.create_time.strftime("%Y-%m-%d %X")
            # if res_temp.deadline: # 截止时间
            #     res_temp.deadline=res_temp.deadline.strftime("%Y-%m-%d %X")
            # if res_temp.reminder_time:
            #     res_temp.reminder_time=res_temp.reminder_time.strftime("%Y-%m-%d %X")
            data = {
                "id": res_temp.id,
                "name": res_temp.name,
                "create_time": res_temp.create_time,
                "status": res_temp.status,
                "level": res_temp.level,
                "sub_todo_id": res_temp.sub_todo_id,
                "start_time": res_temp.start_time,
                "end_time": res_temp.end_time,
                "use_time": res_temp.use_time,
                "progress_bar": res_temp.progress_bar,
                "deadline": res_temp.deadline,
                "reminder_time": res_temp.reminder_time
            }
            json_data.append(data)
            print(json_data)
        return jsonify(json_data)
    else:
        return {"code":0}

@app.route("/api/todo/<status>",methods=["GET"],endpoint="get_todo_details")  
def get_todo_details(status):
    res = ToDoDetails.query.filter(ToDoDetails.status==status).all()
    if res:
        json_data = []
        for res_temp in res:
            data = {
                "id": res_temp.id,
                "name": res_temp.name,
                "create_time": res_temp.create_time,
                "status": res_temp.status,
                "level": res_temp.level,
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



@app.route("/api/todo/post",methods=["POST"],endpoint="post_todo_details")
def post_todo_details():
    # 判断数据有没有ID 字段，有的话就更新ID，没有就insert
    res = request.json
    print(res)
    if res:
        for todo in res:
            # Tue, 01 Dec 2020 16:44:13 GMT
            GMT_FORMAT =  '%a, %d %b %Y %H:%M:%S GMT'
            dayjs_FORMAT = '%Y-%m-%d %H:%M:%S'            
            if todo.get("id") == None:
                # 新待办，要插入
                if todo.get("deadline"):
                    todo["deadline"] = datetime.strptime(todo["deadline"],dayjs_FORMAT)
                    print(type(todo["deadline"]))
                if todo.get("reminder_time"):
                    todo["reminder_time"] = datetime.strptime(todo["reminder_time"],dayjs_FORMAT)
                    print(type(todo["reminder_time"]))

                print(f"插入的name是{todo['name']}")
                data = ToDoDetails(
                    name=todo.get("name"),
                    status=todo.get("status"),
                    create_time=datetime.now(),
                    level=todo.get("level"),
                    sub_todo_id=todo.get("sub_todo_id"),
                    start_time=todo.get("start_time"),
                    end_time=todo.get("end_time"),
                    use_time=todo.get("use_time"),
                    progress_bar=todo.get("progress_bar"),
                    deadline=todo.get("deadline"),
                    reminder_time=todo.get("reminder_time")
                )
                db.session.add(data)
            else:
                # 旧待办，要更新，现在是全量更新，以后再优化吧
                row = ToDoDetails.query.filter(ToDoDetails.id==todo["id"]).first()
                print(f"更改的ID是{row.id}")
                row.name=todo.get("name")
                row.status=todo.get("status")
                row.level=todo.get("level")
                row.sub_todo_id=todo.get("sub_todo_id")
                row.start_time=todo.get("start_time")
                row.end_time=todo.get("end_time")
                row.use_time=todo.get("use_time")
                row.progress_bar=todo.get("progress_bar")
                row.deadline=todo.get("deadline")
                row.reminder_time=todo.get("reminder_time")
        try:
            db.session.commit()
            return "{code:0}"
        except Exception as e:
            return "{code:1,message:" + f"{e}" + "}"
    return "{code:0}"