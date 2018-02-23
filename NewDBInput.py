#-*- coding: utf-8-*-
import MySQLdb
import json
import collections

if __name__ == "__main__":
	connector = MySQLdb.connect(host="localhost", db="j14000", user="root", passwd="root",charset="utf8")
	cursor = connector.cursor()

	f = open('no.json', 'r')
	jsonData = json.load(f, object_pairs_hook=collections.OrderedDict)

	for num in jsonData:
		sql = "insert into calls (no) values(" + str(jsonData[num]) + ")"
		cursor.execute(sql)

	connector.commit()
	cursor.close()

