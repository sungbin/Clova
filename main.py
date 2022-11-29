import json
import sys
import os

def load_json(path):
	with open(path, "r") as json_file:
		json_data = json.load(json_file)
		return json_data


def save_json(path, json_data):
	with open(path, 'w') as outfile:
		json.dump(json_data, outfile, indent=4)

def add_item(json_data, key, val):
	json_data[key] = val

def print_help():
	print("(1) add [key] [value]")
	print("\t [key]: an old word")
	print("\t [value]: a new word")
	print("(2) change a script into correct one")
	print("(3) exit (other characters)")
	opt = input()
	return opt

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print("USAGE: python ./main [json_path]")
		sys.exit(0)

	json_path = sys.argv[1]

	try:
		data = load_json(json_path)
	except:
		print("WRONG JSON PATH:", json_path)
		sys.exit(0)

	while True:
		opt = print_help()
		if (opt != "1" and opt != "2"):
			sys.exit(0)
	
		if (opt == "1"):
			while True:
				raw = input("[key] [value]: ")
				try:
					splited = raw.split(' ')
					key = splited[0]
					val = splited[1]
				except:
					print("wrong input:", txt)
					break
				data[key] = val	
				save_json(json_path, data)
	
		if (opt == "2"):
			f_list = os.listdir(os.getcwd()+"/transcript")
			print("select a transcript")
			for i in range(0, len(f_list)):
				print("{}) {}".format(i, f_list[i]))

			selected = input()
			script_path = "./transcript/" + f_list[int(selected)]

			with open("./{}".format(script_path), 'r') as script_file:
				lines = script_file.readlines()
				
			refined_lines = []
			for line in lines:
				words = line.split(' ')
				for word in words:
					if word in data.keys():
						line = line.replace(word, data[word])

				refined_lines.append(line)

			refined_script = ''.join(refined_lines)

			with open("./{}_refined".format(script_path), 'w') as script_file:
				script_file.write(refined_script)

			sys.exit(0)
	
