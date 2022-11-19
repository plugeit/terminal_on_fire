import os
def execute(string):
	if string=="":
		pass
	try:
		exec(f"""result={string}
print(result)""")
	except:
		try:
			if string[-2]=='(' and string[-1]==')':
				exec(f"""result=os.{string}
print(result)""")
				result=""
			else:
				exec(f"""result=os.{string}()
print(result)""")
				result=""
		except Exception as er:
			result=er
			print(result)
while True:
	execute(str(input(f"{os.getcwd()}>")))
