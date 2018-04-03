#coding=utf-8
import time,requests,schedule
from baseDao import BaseDao

def  getRequireTasks():
	rs = getattr(BaseDao('get_tasks'),"retrieve")()
	for item in rs["rows"]:
		doTask(item)


def doTask(params):
	body = {"text":params['title'], "desp": params['desc']}
	response = requests.post(params['server'], data = body)
	print (type(response.text))
	rs = getattr(BaseDao('task_log'),'create')({"task_id":params["id"],"resp":response.text},[],{})
	print(rs)

# 开始的循环任务，一分钟执行一次
schedule.every(1).minutes.do(getRequireTasks)
while True:
    schedule.run_pending()
    time.sleep(1)
