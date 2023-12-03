import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "smrithy123",
  database = "mydatabase",
  auth_plugin = "mysql_native_password"
)

if db.is_connected():
  print("Connected to database") #debug
  cursor = db.cursor()
  cursor.execute("SELECT * FROM tasks")

  #for debuging - printing values in a table
  for c in cursor.fetchall():
    print(c)
    print("\n")

  #Add task
  def add_task(taskid, task, completed, priority):
    query = "INSERT INTO `mydatabase`.`tasks` (`taskID`, `description`, `completed`, `priority`) VALUES (%s, %s, %s, %s)"
    value = (taskid,task,completed,priority)
    cursor.execute(query,value)
    db.commit()

  #Mark task as completed
  def mark_task(taskid,completed):
    query = "UPDATE `mydatabase`.`tasks` SET `completed` = %s WHERE (`taskID` = %s)"
    value = (completed,taskid)
    cursor.execute(query,value)
    db.commit()

  #deleting task from database
  def del_task(taskid):
    query = "DELETE FROM `mydatabase`.`tasks` WHERE `taskID` = %s"
    value = (taskid)
    cursor.execute(query,value)
    db.commit()

#To update the description of an existin task
  def edit_task(taskid,taskName):
    query = "UPDATE `mydatabase`.`tasks` SET `description` = %s WHERE (`taskID` = %s)"
    value = (taskName,taskid)
    cursor.execute(query,value)
    db.commit()
    
  #exit application should clear the table
  def exit():
    query = "TRUNCATE TABLE mydatabase.tasks"
    cursor.execute(query)
    db.commit()


