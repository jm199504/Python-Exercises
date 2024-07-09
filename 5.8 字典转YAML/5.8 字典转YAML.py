import yaml

meta = {"name": "45621", "kind": "number-percent-mixed"}
resource = {
    "platform.stke/v1alpha1|StatefulSetPlus|nginx": [
        {
            "key": "dc6be390-9b4c-11eb-be21-09de30598e2d",
            "kind": "StatefulSetPlus",
            "spec": {
                "replicas": 1,
                "selector": {
                    "matchLabels": {
                        "env": "test",
                        "region": "ap-nanjing",
                        "k8s-app": "nginx",
                        "clusterId": "cls-ggyxim0q",
                        "qcloud-app": "nginx",
                        "projectName": "prj8n2xb",
                        "moduleFourId": "1085185"
                    }
                },
                "template": {
                    "spec": {
                        "volumes": [
                            {
                                "name": "cgroup",
                                "hostPath": {
                                    "path": "/sys/fs/cgroup",
                                    "type": ""
                                }
                            },
                            {
                                "name": "shm",
                                "emptyDir": {
                                    "medium": "Memory"
                                }
                            },
                            {
                                "name": "kongpodinfo",
                                "downwardAPI": {
                                    "items": [
                                        {
                                            "path": "cpu",
                                            "resourceFieldRef": {
                                                "divisor": "1",
                                                "resource": "limits.cpu",
                                                "containerName": "kong"
                                            }
                                        },
                                        {
                                            "path": "memory",
                                            "resourceFieldRef": {
                                                "divisor": "1Mi",
                                                "resource": "limits.memory",
                                                "containerName": "kong"
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "name": "kong-yml",
                                "configMap": {
                                    "name": "kong",
                                    "items": [
                                        {
                                            "key": "kong.yml",
                                            "mode": 420,
                                            "path": "kong.yml"
                                        }
                                    ]
                                }
                            }
                        ],
                        "affinity": {
                            "podAntiAffinity": {
                                "preferredDuringSchedulingIgnoredDuringExecution": [
                                    {
                                        "weight": 100,
                                        "podAffinityTerm": {
                                            "topologyKey": "kubernetes.io/hostname",
                                            "labelSelector": {
                                                "matchExpressions": [
                                                    {
                                                        "key": "k8s-app",
                                                        "values": [
                                                            "nginx"
                                                        ],
                                                        "operator": "In"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        "containers": [
                            {
                                "env": [
                                    {
                                        "name": "TZ",
                                        "value": "Asia/Shanghai"
                                    },
                                    {
                                        "name": "KONG_PLUGINS",
                                        "value": "cors"
                                    },
                                    {
                                        "name": "KONG_PROXY_ERROR_LOG",
                                        "value": "/dev/stderr"
                                    },
                                    {
                                        "name": "KONG_PROXY_ACCESS_LOG",
                                        "value": "/dev/stdout"
                                    },
                                    {
                                        "name": "NODE_IP",
                                        "valueFrom": {
                                            "fieldRef": {
                                                "fieldPath": "status.hostIP"
                                            }
                                        }
                                    },
                                    {
                                        "name": "POD_IP",
                                        "valueFrom": {
                                            "fieldRef": {
                                                "fieldPath": "status.podIP"
                                            }
                                        }
                                    },
                                    {
                                        "name": "POD_NAMESPACE",
                                        "valueFrom": {
                                            "fieldRef": {
                                                "fieldPath": "metadata.namespace"
                                            }
                                        }
                                    },
                                    {
                                        "name": "POD_UID",
                                        "valueFrom": {
                                            "fieldRef": {
                                                "fieldPath": "metadata.uid"
                                            }
                                        }
                                    },
                                    {
                                        "name": "POD_NAME",
                                        "valueFrom": {
                                            "fieldRef": {
                                                "fieldPath": "metadata.name",
                                                "apiVersion": "v1"
                                            }
                                        }
                                    }
                                ],
                                "tty": True,
                                "name": "kong",
                                "image": "csighub.tencentyun.com/coding/coding-kong:1.5.2",
                                "stdin": True,
                                "resources": {
                                    "limits": {
                                        "cpu": "2",
                                        "memory": "4Gi"
                                    },
                                    "requests": {
                                        "cpu": "2",
                                        "memory": "4Gi"
                                    }
                                },
                                "volumeMounts": [
                                    {
                                        "name": "cgroup",
                                        "readOnly": True,
                                        "mountPath": "/sys/fs/cgroup"
                                    },
                                    {
                                        "name": "shm",
                                        "mountPath": "/dev/shm"
                                    },
                                    {
                                        "name": "kongpodinfo",
                                        "mountPath": "/etc/podinfo"
                                    },
                                    {
                                        "name": "kong-yml",
                                        "mountPath": "/etc/kong/conf/"
                                    }
                                ],
                                "imagePullPolicy": "Always",
                                "securityContext": {
                                    "privileged": False,
                                    "capabilities": {
                                        "add": [
                                            "SYS_RESOURCE",
                                            "NET_ADMIN",
                                            "SYS_ADMIN",
                                            "IPC_LOCK",
                                            "SYS_PTRACE"
                                        ]
                                    }
                                }
                            }
                        ],
                        "restartPolicy": "Always",
                        "imagePullSecrets": [
                            {
                                "name": "csighub-xianyunlan"
                            }
                        ]
                    },
                    "metadata": {
                        "labels": {
                            "env": "test",
                            "region": "ap-nanjing",
                            "k8s-app": "nginx",
                            "clusterId": "cls-ggyxim0q",
                            "qcloud-app": "nginx",
                            "projectName": "prj8n2xb",
                            "moduleFourId": "1085185"
                        },
                        "annotations": {
                            "tke.cloud.tencent.com/vpc-eni-cni-ip": "True",
                            "tke.cloud.tencent.com/device-type-cmdb": "VNCLOUD-2-4-50",
                            "tke.cloud.tencent.com/vpc-ip-claim-delete-policy": "Never"
                        },
                        "creationTimestamp": None
                    }
                },
                "serviceName": "nginx",
                "updateStrategy": {
                    "type": "OnDelete",
                    "rollingUpdate": {
                        "partition": 0
                    }
                },
                "batchDeployConfig": {},
                "podManagementPolicy": "Parallel",
                "revisionHistoryLimit": 10
            },
            "status": {
                "replicas": 1,
                "labelSelector": "clusterId=cls-ggyxim0q,env=test,k8s-app=nginx,moduleFourId=1085185,projectName=prj8n2xb,qcloud-app=nginx,region=ap-nanjing",
                "readyReplicas": 1,
                "collisionCount": 0,
                "updateRevision": "nginx-54c464cc69",
                "currentReplicas": 1,
                "currentRevision": "nginx-54c464cc69",
                "updatedReplicas": 1,
                "batchDeployStatus": {},
                "observedGeneration": 4
            },
            "metadata": {
                "uid": "0b2543e6-bb6c-11ea-88ad-525400b848ec",
                "name": "nginx",
                "labels": {
                    "env": "test",
                    "region": "ap-nanjing",
                    "k8s-app": "nginx",
                    "clusterId": "cls-ggyxim0q",
                    "qcloud-app": "nginx",
                    "projectName": "prj8n2xb",
                    "moduleFourId": "1085185"
                },
                "selfLink": "/apis/platform.stke/v1alpha1/namespaces/ns-prj8n2xb-1085185-test/statefulsetpluses/nginx",
                "namespace": "ns-prj8n2xb-1085185-test",
                "generation": 4,
                "annotations": {
                    "deployImageSource": "hub",
                    "stkeUpateVersionTag": "v3",
                    "tke.cloud.tencent.com/enable-static-ip": "True"
                },
                "resourceVersion": "4107565216",
                "creationTimestamp": "2020-07-01T07:25:30Z"
            },
            "apiVersion": "platform.stke/v1alpha1"
        }
    ]
}
templates = {
    "platform.stke/v1alpha1|StatefulSetPlus|nginx": {
        "name": "platform.stke/v1alpha1|StatefulSetPlus|nginx",
        "kind": "StatefulSetPlus",
        "apiVersion": "",
        "metadata": {
            "name": "",
            "labels": {
                "coding-cd.tencent.com/dependent": "[]"
            }
        }
    }
}
spec = {
    "batches": [
        {
            "value": 2,
            "kind": "number",
            "preConfirm": {
                "enable": False,
                "waitBeforeConfirm": 0
            }
        },
        {
            "value": 100,
            "kind": "percent",
            "preConfirm": {
                "enable": True,
                "waitBeforeConfirm": 4
            }
        }
    ],
    "selectors": {
        "labels": {}
    }
}
manifest = {"metadata": {
                "name": "api-server-env1111111",
                "labels": {
                    "coding-cd.tencent.com/dependent": "[]"
                }
            ,
    "content": {
        "namespace": "ns-prjxjd-123456-production1",
        "tkex_cluster_id": "cls-xxxx"
    }}}
config = {"estimate_type": "today"}
approve_config = {
    "title": "1123",
    "creator": [],
    "startTime": "2021-04-13 00:00:00",
    "endTime": "2021-04-13 23:59:59",
    "estimateTime": [
        "2021-04-13 00:00:00",
        "2021-04-13 23:59:59",
        "today"
    ],
    "approveflow": 1,
    "content": ""

}

orchestration_template = {
    "orchestrationId": 44,
    "template": {
        "platform.stke/v1alpha1|StatefulSetPlus|oa-trigger-server-junmingguo": {
            "kind": "StatefulSetPlus",
            "name": "platform.stke/v1alpha1|StatefulSetPlus|oa-trigger-server-junmingguo",
            "metadata": {
                "name": "",
                "labels": {
                    "coding-cd.tencent.com/dependent": "[]",
                    "enabled": True
                }
            },
            "apiVersion": ""
        }
    }
}
artifacts = {
        "platform.stke/v1alpha1|StatefulSetPlus|oa-trigger-server-junmingguo": [
            {
                "artifact_type": "docker",
                "meta": {
                    "docker_url": "csighub.tencentyun.com/coding/cd-scheduler"
                },
                "version": "latest-625d964f"
            }
        ]
    }

clusters = {
    "platform.stke/v1alpha1|StatefulSetPlus|oa-trigger-server-junmingguo": [
            {
                "key": "9cc2b6f0-a1d3-11eb-af81-cfeba85695d1",
                "kind": "StatefulSetPlus",
                "spec": {
                    "replicas": 1,
                    "selector": {
                        "matchLabels": {
                            "env": "production",
                            "region": "ap-nanjing",
                            "k8s-app": "oa-trigger-server-junmingguo",
                            "clusterId": "cls-elrc7cfq",
                            "qcloud-app": "oa-trigger-server-junmingguo",
                            "projectName": "prj8n2xb",
                            "moduleFourId": "1085185",
                            "workload-kind": "statefulsetplus"
                        }
                    },
                    "template": {
                        "spec": {
                            "volumes": [
                                {
                                    "name": "shm",
                                    "emptyDir": {
                                        "medium": "Memory"
                                    }
                                },
                                {
                                    "name": "trigger-serverpodinfo",
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "path": "cpu",
                                                "resourceFieldRef": {
                                                    "divisor": "1",
                                                    "resource": "limits.cpu",
                                                    "containerName": "trigger-server"
                                                }
                                            },
                                            {
                                                "path": "memory",
                                                "resourceFieldRef": {
                                                    "divisor": "1Mi",
                                                    "resource": "limits.memory",
                                                    "containerName": "trigger-server"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "name": "logs-path",
                                    "emptyDir": {
                                        "medium": "Memory"
                                    }
                                },
                                {
                                    "name": "filebeat-config",
                                    "configMap": {
                                        "name": "filebeat-custom-trigger-server"
                                    }
                                }
                            ],
                            "containers": [
                                {
                                    "env": [
                                        {
                                            "name": "ASYNC_TASK_TIMEOUT_DELTA",
                                            "value": "600"
                                        },
                                        {
                                            "name": "ASYNC_TASK_EXPIRE_DELTA",
                                            "value": "300"
                                        },
                                        {
                                            "name": "CELERYD_TIME_LIMIT",
                                            "value": "150"
                                        },
                                        {
                                            "name": "DEPLOY_CALENDAR_URL",
                                            "value": "http://9.149.123.79"
                                        },
                                        {
                                            "name": "DEBUG",
                                            "value": "true"
                                        },
                                        {
                                            "name": "SENTRY_DSN",
                                            "value": "http://9f8ef2b3da5c42b4a3c3bad1fb5ec050@sentry.oa.com/2984"
                                        },
                                        {
                                            "name": "ENVIRONMENT",
                                            "value": "TEST"
                                        },
                                        {
                                            "name": "DJANGO_DEBUG_LEVEL",
                                            "value": "INFO"
                                        },
                                        {
                                            "name": "FEATURES",
                                            "value": "dev"
                                        },
                                        {
                                            "name": "SECRET_KEY",
                                            "value": "dev"
                                        },
                                        {
                                            "name": "DB_NAME",
                                            "value": "coding-oa-junmingguo"
                                        },
                                        {
                                            "name": "DB_USER",
                                            "value": "coding"
                                        },
                                        {
                                            "name": "DB_PASSWORD",
                                            "value": "Z=j^yD#bbKnm"
                                        },
                                        {
                                            "name": "DB_HOST",
                                            "value": "10.101.206.20"
                                        },
                                        {
                                            "name": "DB_PORT",
                                            "value": "5432"
                                        },
                                        {
                                            "name": "MESSAGE_CENTER_NAME",
                                            "value": "CD"
                                        },
                                        {
                                            "name": "MESSAGE_CENTER_TOKEN",
                                            "value": "b9c91bbd-0624-4b63-80ac-640f2d14176f"
                                        },
                                        {
                                            "name": "MESSAGE_CENTER_URL",
                                            "value": "http://message.csig.oa.com"
                                        },
                                        {
                                            "name": "API_SETTING_BASE_URI",
                                            "value": "http://9.139.30.23"
                                        },
                                        {
                                            "name": "API_DEBUG",
                                            "value": "true"
                                        },
                                        {
                                            "name": "ASYNC_TASK_HEART_BEAT_QUERY_INTERVAL",
                                            "value": "30"
                                        },
                                        {
                                            "name": "RIO_SMARTY_TOKEN",
                                            "value": "3R5HgUOEdaDpTdcXMeqbRnFDmdkU0rOm"
                                        },
                                        {
                                            "name": "QFLOW_BASE_URI",
                                            "value": "http://dev.qflow.tencent.coding.oa.com"
                                        },
                                        {
                                            "name": "QFLOW_TOKEN",
                                            "value": "9ecfd01e-d9b8-11e9-9f48-309c23c29cd9"
                                        },
                                        {
                                            "name": "CELERY_BROKER_URL",
                                            "value": "amqp://guestCd:guestCd@9.139.151.91:5672/junmingguo"
                                        },
                                        {
                                            "name": "REDIS_DEFAULT_LOCATION",
                                            "value": "redis://:SUQKh*5628rg@9.149.123.199:6379/1"
                                        },
                                        {
                                            "name": "CODING_AUTHENTICATION_TOKEN",
                                            "value": "ce6c827f-a5d6-4b91-ba39-7a7d329300c7"
                                        },
                                        {
                                            "name": "CODING_GRPC_ENDPOINT",
                                            "value": "http://api.dq.oa.com/cggt/"
                                        },
                                        {
                                            "name": "CODING_GRPC_PROXY_HEADER",
                                            "value": "X-DQAPI-AUTHENTICATION"
                                        },
                                        {
                                            "name": "CODING_GRPC_PROXY_TOKEN",
                                            "value": "hbuWbkiFmBn2ThMLseEwhUmBj"
                                        },
                                        {
                                            "name": "TOF_APP_ID",
                                            "value": "20720"
                                        },
                                        {
                                            "name": "TOF_APP_KEY",
                                            "value": "4565000ad59b4d929cbeda87596bc256"
                                        },
                                        {
                                            "name": "TOF_API_HOST",
                                            "value": "http://oss.api.tof.oa.com"
                                        },
                                        {
                                            "name": "DISPATCH_BASE_URI",
                                            "value": "http://dev.qcd.oa.com"
                                        },
                                        {
                                            "name": "CO_TOKEN",
                                            "value": "7d6ea637-ae7e-4d77-abcb-49437786e73f"
                                        },
                                        {
                                            "name": "NODE_IP",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "status.hostIP"
                                                }
                                            }
                                        },
                                        {
                                            "name": "POD_IP",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "status.podIP"
                                                }
                                            }
                                        },
                                        {
                                            "name": "POD_NAMESPACE",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "metadata.namespace"
                                                }
                                            }
                                        },
                                        {
                                            "name": "POD_UID",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "metadata.uid"
                                                }
                                            }
                                        },
                                        {
                                            "name": "POD_UID",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "metadata.uid"
                                                }
                                            }
                                        }
                                    ],
                                    "tty": True,
                                    "args": [
                                        "-c",
                                        "/etc/supervisord.celery-trigger.conf"
                                    ],
                                    "name": "trigger-server",
                                    "image": "csighub.tencentyun.com/coding/cd-scheduler:close-release-timeout-check",
                                    "stdin": True,
                                    "command": [
                                        "supervisord"
                                    ],
                                    "resources": {
                                        "limits": {
                                            "cpu": "1",
                                            "memory": "1Gi"
                                        },
                                        "requests": {
                                            "cpu": "1",
                                            "memory": "1Gi"
                                        }
                                    },
                                    "workingDir": "/app",
                                    "volumeMounts": [
                                        {
                                            "name": "trigger-serverpodinfo",
                                            "mountPath": "/etc/podinfo"
                                        },
                                        {
                                            "name": "shm",
                                            "mountPath": "/dev/shm"
                                        },
                                        {
                                            "name": "logs-path",
                                            "mountPath": "/app/logs"
                                        }
                                    ],
                                    "imagePullPolicy": "Always",
                                    "securityContext": {
                                        "privileged": True
                                    }
                                },
                                {
                                    "env": [
                                        {
                                            "name": "PROJECT_NAME",
                                            "value": "cd-trigger-server-test"
                                        },
                                        {
                                            "name": "ES_URL",
                                            "value": "http://10.101.205.52:9200"
                                        },
                                        {
                                            "name": "ES_USER",
                                            "value": "coding-cd"
                                        },
                                        {
                                            "name": "POD_NAME",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "metadata.name",
                                                    "apiVersion": "v1"
                                                }
                                            }
                                        },
                                        {
                                            "name": "POD_UID",
                                            "valueFrom": {
                                                "fieldRef": {
                                                    "fieldPath": "metadata.uid"
                                                }
                                            }
                                        },
                                        {
                                            "name": "ES_PWD",
                                            "valueFrom": {
                                                "secretKeyRef": {
                                                    "key": "ES_PWD",
                                                    "name": "custom-filebeat-output",
                                                    "optional": False
                                                }
                                            }
                                        }
                                    ],
                                    "tty": True,
                                    "name": "filebeat",
                                    "image": "csighub.tencentyun.com/sdet_dev/filebeat:6.8.9-o2e-1.0",
                                    "stdin": True,
                                    "resources": {
                                        "limits": {
                                            "cpu": "1",
                                            "memory": "1Gi"
                                        },
                                        "requests": {
                                            "cpu": "1",
                                            "memory": "1Gi"
                                        }
                                    },
                                    "volumeMounts": [
                                        {
                                            "name": "shm",
                                            "mountPath": "/dev/shm"
                                        },
                                        {
                                            "name": "logs-path",
                                            "mountPath": "/app/logs"
                                        },
                                        {
                                            "name": "filebeat-config",
                                            "mountPath": "/usr/share/filebeat/inputs.d/"
                                        }
                                    ],
                                    "imagePullPolicy": "Always",
                                    "securityContext": {
                                        "privileged": True
                                    }
                                }
                            ],
                            "restartPolicy": "Always",
                            "imagePullSecrets": [
                                {
                                    "name": "csighub-feiyuegeng"
                                },
                                {
                                    "name": "csighub-junmingguo"
                                }
                            ],
                            "terminationGracePeriodSeconds": 30
                        },
                        "metadata": {
                            "labels": {
                                "env": "production",
                                "region": "ap-nanjing",
                                "k8s-app": "oa-trigger-server-junmingguo",
                                "clusterId": "cls-elrc7cfq",
                                "qcloud-app": "oa-trigger-server-junmingguo",
                                "projectName": "prj8n2xb",
                                "moduleFourId": "1085185",
                                "workload-kind": "statefulsetplus"
                            },
                            "annotations": {
                                "tke.cloud.tencent.com/enable-cmdb": "true",
                                "tke.cloud.tencent.com/zone-id-cmdb": "4",
                                "tke.cloud.tencent.com/vpc-eni-cni-ip": "true",
                                "tke.cloud.tencent.com/bk-operator-cmdb": "feiyuegeng",
                                "tke.cloud.tencent.com/device-type-cmdb": "VNCLOUD-2-2-100",
                                "tke.cloud.tencent.com/business3-id-cmdb": "1085185",
                                "tke.cloud.tencent.com/pri-operator-cmdb": "feiyuegeng",
                                "internal.eks.tke.cloud.tencent.com/pod_eth_idx": "1"
                            },
                            "creationTimestamp": None
                        }
                    },
                    "serviceName": "oa-trigger-server-junmingguo",
                    "updateStrategy": {
                        "type": "RollingUpdate",
                        "rollingUpdate": {
                            "partition": 0
                        }
                    },
                    "batchDeployConfig": {},
                    "podManagementPolicy": "Parallel",
                    "revisionHistoryLimit": 10
                },
                "status": {
                    "replicas": 1,
                    "labelSelector": "clusterId=cls-elrc7cfq,env=production,k8s-app=oa-trigger-server-junmingguo,moduleFourId=1085185,projectName=prj8n2xb,qcloud-app=oa-trigger-server-junmingguo,region=ap-nanjing,workload-kind=statefulsetplus",
                    "readyReplicas": 1,
                    "collisionCount": 0,
                    "updateRevision": "oa-trigger-server-junmingguo-798b8c5f54",
                    "currentReplicas": 1,
                    "currentRevision": "oa-trigger-server-junmingguo-798b8c5f54",
                    "updatedReplicas": 1,
                    "batchDeployStatus": {},
                    "observedGeneration": 21
                },
                "metadata": {
                    "uid": "040e621b-4feb-11eb-864c-0e788566d7be",
                    "name": "oa-trigger-server-junmingguo",
                    "labels": {
                        "env": "production",
                        "region": "ap-nanjing",
                        "k8s-app": "oa-trigger-server-junmingguo",
                        "clusterId": "cls-elrc7cfq",
                        "qcloud-app": "oa-trigger-server-junmingguo",
                        "projectName": "prj8n2xb",
                        "moduleFourId": "1085185",
                        "workload-kind": "statefulsetplus"
                    },
                    "selfLink": "/apis/platform.stke/v1alpha1/namespaces/ns-prj8n2xb-1085185-production/statefulsetpluses/oa-trigger-server-junmingguo",
                    "namespace": "ns-prj8n2xb-1085185-production",
                    "generation": 21,
                    "annotations": {
                        "deployImageSource": "hub",
                        "stkeUpateVersionTag": "v3",
                        "platform.stke/stsp-is-updating": "false",
                        "platform.stke/upgrade-in-place": "false",
                        "tke.cloud.tencent.com/enable-static-ip": "true"
                    },
                    "resourceVersion": "8736416907",
                    "creationTimestamp": "2021-01-06T06:47:16Z"
                },
                "apiVersion": "platform.stke/v1alpha1"
            }
        ]
}
strategies = {
    "platform.stke/v1alpha1|StatefulSetPlus|oa-trigger-server-junmingguo": {
            "apiVersion": "coding-cd.tencent.com/v1",
            "kind": "Strategy",
            "metadata": {
                "kind": "number-percent-mixed",
                "name": "默认策略"
            },
            "spec": {
                "batches": [
                    {
                        "kind": "percent",
                        "value": 50,
                        "preConfirm": {
                            "enable": True,
                            "waitBeforeConfirm": 0
                        }
                    },
                    {
                        "kind": "percent",
                        "value": 100,
                        "preConfirm": {
                            "enable": True,
                            "waitBeforeConfirm": 0
                        }
                    }
                ]
            }
        }
}
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
f = open('cluster.yaml', 'w+')
yaml.dump(aa, f, allow_unicode=True)