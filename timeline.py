from www.init.init_app import app
from www.DB.db_script.init_db import db,User,ToDoDetails,EventTimeLine,datetime,and_,or_,not_
from flask import jsonify,request
import time

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
    curr_time = time.time()
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
    if not isinstance(res,list):
        temp = []
        temp.append(res)
        res = temp
    print("res=>",res)
    new_items = []
    if res:
        for todo in res:
            event_conn = []
            event_type = []
            print("rodo=>",todo)
            if todo.get("id") == None:
                print(f"插入的name是{todo['name']}")
                name=todo.get("name")
                status=todo.get("status","create")
                create_time=time.time()
                level=todo.get("level")
                sub_todo_id=todo.get("sub_todo_id")
                start_time=todo.get("start_time")
                end_time=todo.get("end_time")
                use_time=todo.get("use_time")
                progress_bar=todo.get("progress_bar")
                deadline=todo.get("deadline")
                reminder_time=todo.get("reminder_time")
                data = ToDoDetails(
                    name=name,
                    status=status,
                    create_time=create_time,
                    level=level,
                    sub_todo_id=sub_todo_id,
                    start_time=start_time,
                    end_time=end_time,
                    use_time=use_time,
                    progress_bar=progress_bar,
                    deadline=deadline,
                    reminder_time=reminder_time
                )
                event = EventTimeLine(
                    event_todo_id=None,
                    event_type="create_todo",
                    event_time=time.time(),
                    event_valid="True",
                    event_conn=f"新增了待办事项:\n\t子待办：{sub_todo_id}\n\t名称：{name}\n\t优先级：{level}\n\t截止时间：{deadline}\n\t提醒时间：{reminder_time}"
                )
                db.session.add(data)
                db.session.add(event)
            else:
                # 旧待办，要更新，现在是全量更新，以后再优化吧
                row = ToDoDetails.query.filter(ToDoDetails.id==todo["id"]).first()
                print(f"更改的ID是{row.id}")
                todo_id = todo.get("id")
                name=todo.get("name")
                status=todo.get("status")
                level=todo.get("level")
                sub_todo_id=todo.get("sub_todo_id")
                start_time=todo.get("start_time")
                end_time=todo.get("end_time")
                use_time=todo.get("use_time")
                progress_bar=todo.get("progress_bar")
                deadline=todo.get("deadline")
                reminder_time=todo.get("reminder_time")
                
                if row.name!=name:
                    event_conn.append(f"名称更新：\n\t《{row.name}》  ==>  《{name}》")
                    row.name=name
                if row.status!=status:
                    event_conn.append(f"状态更新：\n\t{row.status}  ==>  {status}")
                    row.status=status
                if row.level!=level:
                    event_conn.append(f"优先级更新：\n\t{row.level}  ==>  {level}")
                    row.level=level
                if row.sub_todo_id!=sub_todo_id:
                    event_conn.append(f"子任务更新：\n\t{row.sub_todo_id}  ==>  {sub_todo_id}")
                    row.sub_todo_id=sub_todo_id
                if row.start_time!=start_time:
                    row.start_time=start_time
                if row.end_time!=end_time:
                    row.end_time=end_time
                if row.use_time!=use_time:
                    row.use_time=use_time
                if row.progress_bar!=progress_bar:
                    event_conn.append(f"进度更新：\n\t{row.progress_bar}  ==>  {progress_bar}")
                    row.progress_bar=progress_bar
                if row.deadline!=deadline:
                    event_conn.append(f"截止时间更新：\n\t{row.deadline}  ==>  {deadline}")
                    row.deadline=deadline
                if row.reminder_time!=reminder_time:
                    event_conn.append(f"提醒时间更新：\n\t{row.reminder_time}  ==>  {reminder_time}")
                    row.reminder_time=reminder_time
                if len(event_conn) > 0:
                    ev_str = '\n'.join(event_conn)
                    event = EventTimeLine(
                        event_todo_id=todo_id,
                        event_type="update_todo",
                        event_time=datetime.now(),
                        event_valid="True",
                        event_conn=f"更新内容：\n{ev_str}"
                    )
                    db.session.add(event)
        try:
            db.session.commit()
            if new_items != []:
                for new_item in new_items:
                    print(f"new_item:{new_item}")
                    new_item = ToDoDetails.query.filter(
                        ToDoDetails.create_time==new_item[0]
                    ).first()
                    new_items.append(new_item.id)
            return {"code":0,"new_items":new_items}
        except Exception as e:
            return {"code":1,"message":f"{res}不是合法的输入","error":f"{e}"}
    return "{code:0}"