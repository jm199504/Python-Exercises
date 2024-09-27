## 5.8-字典转YAML

### 问题描述

有一份python的字典（dict）对象，需要转为YAML格式。

### 输入示例

```python
aa={
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

### 输出示例

```yaml
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

### 示例代码

```python
import yaml

f = open('cluster.yaml', 'w+')
yaml.dump(aa, f, allow_unicode=True)
```

