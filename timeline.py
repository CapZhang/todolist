from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///www/DB/db/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pswd = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# 待办事项明细
class ToDoDetails(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # 待办事项名称，不可为空
    name = db.Column(db.String, unique=False, nullable=False)
    # 待办事项创建时间，不可为空
    create_time = db.Column(db.DateTime, unique=False, nullable=False)
    # 待办事项状态，可为空
    status = db.Column(db.String, unique=False, nullable=True)
    # 优先级，可为空
    level = db.Column(db.Integer, unique=False, nullable=True)
    # 子待办ID，可为空
    sub_todo_id = db.Column(db.Integer, nullable=True)

# 发生的事件的时间线
class EventTimeLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 时间发生的todo的ID
    event_todo_id = db.Column(db.Integer,nullable=False)
    # 事件类型
    event_type = db.Column(db.String, unique=False, nullable=False)
    # 事件备注
    event_conn = db.Column(db.String, unique=False, nullable=False)
    # 事件发生的时间
    event_time = db.Column(db.DateTime, unique=False, nullable=False)
    # 事件是否参与统计
    event_valid = db.Column(db.String, unique=False, nullable=False)

# 最近生成的10条报告
class ReportLimit10(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 报告生成时间
    report_time = db.Column(db.String, unique=False, nullable=True)
    # 报告类型
    report_type = db.Column(db.String, unique=False, nullable=True)
    # 报告内容
    report_conn = db.Column(db.String, unique=False, nullable=True)