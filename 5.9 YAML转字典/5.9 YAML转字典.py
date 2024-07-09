import yaml
f = open("trigger.yaml", encoding="utf-8")
x = yaml.safe_load(f)
x = str(x).replace("\'", "\"").replace("None","\"None\"").replace("True","\"True\"").replace("False","\"False\"")
print(x)

#
# import json,yaml
# test_yaml_file= 'sc-5.yaml'
# test_file = open(test_yaml_file,"r")
#
# #先将yaml转换为dict格式
# generate_dict = yaml.load(test_file,Loader=yaml.FullLoader)
# generate_json = json.dumps(generate_dict,sort_keys=False,indent=4,separators=(',',': '))
# print(generate_json)