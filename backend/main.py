
from flask import Flask, render_template, jsonify, request, abort
import pymysql

#from flask_cors import CORS
#from flaskext.mysql import MySQL

#mysql = MySQL()
app = Flask(__name__)

#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
#app.config['MYSQL_DATABASE_DB'] = 'flaskpy'
#app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
#mysql.init_app(app)
con = pymysql.connect(host='127.0.0.1', user='root', password='jinling', db='flaskpy', charset='utf8', port=3306)




@app.route('/')
def index():
    return True


@app.route('/tasks', methods=['GET'])
def tasks():
    cur = con.cursor()
    cur.execute("select id, name, priority from tasks order by priority desc")
    con.commit()
    tasks = []
    for id, name, pr in cur.fetchall():
        task =dict()
        task['id'] = id
        task['name'] = name
        task['priority'] = pr
        tasks.append(task)
    return jsonify(tasks)


@app.route('/tasks/delete/<task_id>', methods=['POST'])
def delete(task_id):
    cur = con.cursor()
    cur.execute('delete from tasks where id=' + task_id)
    con.commit()
    return jsonify({'result': True})




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
