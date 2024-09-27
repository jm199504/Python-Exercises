## 5.9-YAML转字典

### 问题描述

有一份YAML格式，需要转为python的字典（dict）对象。

### 输入示例

```python
kind: Tkex
manifest:
  apiVersion: v1
  kind: Namespace
  metadata:
    creationTimestamp: '2019-08-07T09:08:57Z'
    labels:
      clusterId: cls-lq3pomd8
      clusterName: cls-lq3pomd8
      env: test
      moduleFourId: '402937'
      projectName: prj55t97
    name: ns-prj55t97-402937-test
    resourceVersion: '262400554'
    selfLink: /api/v1/namespaces/ns-prj55t97-402937-test
    uid: fc9c53b5-b8f2-11e9-9ed1-525400197aa3
  spec:
    finalizers:
    - kubernetes
  status:
    phase: Active
```

### 输出示例

```yaml
{
            'kind': 'Tkex',
            'manifest': {
                'kind': 'Namespace',
                'apiVersion': 'v1',
                'metadata': {
                    'name': 'ns-prj55t97-402937-test',
                    'selfLink': '/api/v1/namespaces/ns-prj55t97-402937-test',
                    'uid': 'fc9c53b5-b8f2-11e9-9ed1-525400197aa3',
                    'resourceVersion': '262400554',
                    'creationTimestamp': '2019-08-07T09:08:57Z',
                    'labels': {
                        'clusterId': 'cls-lq3pomd8',
                        'clusterName': 'cls-lq3pomd8',
                        'env': 'test',
                        'moduleFourId': '402937',
                        'projectName': 'prj55t97'
                    },
                },
                'spec': {
                    'finalizers': [
                        'kubernetes'
                    ]
                },
                'status': {
                    'phase': 'Active'
                },
            },
        }
```

### 示例代码

```python
import yaml
import json

# YAML文件预处理（部分关键字，本文输入示例不包含）
f = open("trigger.yaml", encoding="utf-8")
x = yaml.safe_load(f)
x = str(x).replace("\'", "\"").replace("None","\"None\"").replace("True","\"True\"").replace("False","\"False\"")
print(x)


test_yaml_file= 'sc-5.yaml'
test_file = open(test_yaml_file,"r")

# #先将yaml转换为dict格式
generate_dict = yaml.load(test_file,Loader=yaml.FullLoader)
generate_json = json.dumps(generate_dict,sort_keys=False,indent=4,separators=(',',': '))
print(generate_json)
```

