import json

if __name__ =="__main__":
	"""
	1、看明白了，json.load 就是处理文本IO包装器 textIOWrapper,也即在open打开的文件
	json.loads 是用来处理str,byte,等实际内容的，
	总结：loads也就是序列化文本,处理对象是直接的str.byte等
	load处理内存中的信息。最后作用其实一样。

	2、注意事项：https://blog.csdn.net/Z2572862506/article/details/129294425
	list 前面加星号代表将列表中的元素拆开变为独立的元素, 可以用来传入函数

	字典用一个星号代表字典的 key 键值

	字典用两个星号代表字典的 value


	"""

	with open("input.json",'r') as f:
		# print(f)
		# print(f.read())
		# data=json.load(f)
		data=json.loads(f.read())
	# print(f'data数据是:{data}')
	print(f'data数据是:{data}')
	
	
	print(data[0])
	print(type(data[0]) )
	print(*data[0])
	print(type(*data[0]))
	# print(data1[0]['Name'])
	# print(data1[1]['age'])
	output =','.join([*data[0]])
	print(output)
	print(type(output))
		


	