import time


# unix时间戳转为字符串
def timestamp_2_str(time_stamp):
    struct_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    print(str_time)
    return str_time


timestamp_2_str(758435343)
timestamp_2_str(1702348831)
