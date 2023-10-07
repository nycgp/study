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

	3、python 中join 使用：
	https://baijiahao.baidu.com/s?id=1763111179091591311&wfr=spider&for=pc
	Python中的join()函数用于连接<<字符串序列>>，且字符串序列的分隔符可以自定义，返回连接后的新字符串。其语法为：
	str.join(sequence)
	其中，str表示分隔符，sequence表示需要连接的字符串序列。
	join函数的使用方法


	"""

	try:
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
		# print(type(*data[0]))
		# print(data1[0]['Name'])
		# print(data1[1]['age'])
		output =','.join([*data[0]])
		print("11111111111111111@@",output)
		print(type(output))

		for obj in data:
			print("222222222222222222",obj)
			output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
			print(f'这里是{output}')
			# print(type(output))
		with open("output.csv",'w') as f2:
			print(f'f2是什么？ {f2}')
			f2.write(output)


	except Exception as e:
		print(f'异常报错提示是：{e}')
	# print(data)
	# print(type(data) )
	# print(data[0])
	# print(type(data[0]) )
	# a=data[0]['Name']
	# b=data[1]['Name']
	# print(a)
	# print("第一个人的名字是：",a)
	# print(f's第一个人的名字是：{a},s1第二个人的名字是：{b}') 