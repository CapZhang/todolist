from .init_db import db,User,ToDoDetails,EventTimeLine,ReportLimit10
import time,datetime

def insert_user(username,pswd):
    data = User(username=username,pswd=pswd)
    try:
        db.session.add(data)
        db.session.commit()
        return "{code:0}"
    except Exception as e:
        return "{code:1,message:" + f"{e}" + "}"

def insert_ToDoDetails(name,status="index",level="IN",sub_todo_id=None):
    '''
    @status:
        1. index
        2. start
        3. stop
        4. done
        5. drop
    @level:
        1. IN Important but non-urgent,重要紧急
        2. IU Important but non-urgent,重要不紧急
        3. UN UNImportant and non-urgent, 不重要不紧急
        4. UU Unimportant and urgent,不重要紧急
    '''
    # create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    create_time = datetime.datetime.now()
    data = ToDoDetails(name=name,create_time=create_time,status=status,level=level,sub_todo_id=sub_todo_id,start_time=None,end_time=None,use_time=None,progress_bar="0",deadline=None,reminder_time=None)
    try:
        db.session.add(data)
        db.session.commit()
        return "{code:0}"
    except Exception as e:
        return "{code:1,message:" + f"{e}" + "}"

def insert_EventTimeLine(event_todo_id=None,event_type="creatEvent",event_conn="",event_valid="yes"):
    event_time =  datetime.datetime.now()
    data = EventTimeLine(event_todo_id=event_todo_id,event_type=event_type,event_conn=event_conn,event_time=event_time,event_valid=event_valid)
    try:
        db.session.add(data)
        db.session.commit()
        return "{code:0}"
    except Exception as e:
        return "{code:1,message:" + f"{e}" + "}"

def insert_ReportLimit10(report_type="day",report_conn=""):
    reprot_time = datetime.datetime.now()
    data = ReportLimit10(reprot_time=reprot_time,report_type=report_type,report_conn=report_conn)
    try:
        db.session.add(data)
        db.session.commit()
        return "{code:0}"
    except Exception as e:
        return "{code:1,message:" + f"{e}" + "}"

