import time

from fun import *

session = returnDbSession()

category_count = session.query(Jobs.jobQualification, func.count(Jobs.jobQualification)).group_by(
    Jobs.jobQualification).all()
# 关闭Session
session.close()


def pyXueLI(items: list):
    i = 0
    otherCount = 0
    while i < len(items):
        if (items[i][0] == "NULL") or ("月" in items[i][0]):
            otherCount += items[i][1]
            i += 1
        else:
            i += 1
    items.append(("其他", otherCount))
    filtered_list = [item for item in items if "月" not in item[0] and item[0] != "NULL"]
    return filtered_list


# .filter(~Jobs.jobQualification.like('%月%')) \
# .filter(~Jobs.jobQualification.like('%NULL%')) \
# cpp_list = "{\n"
# for item in category_count:
#     cpp_list += f'    {{"{item[0]}", {item[1]}}},\n'
# cpp_list += "}"
# print(cpp_list)
# print(category_count)
# # 记录函数执行前的时间戳
# start_time = time.time()
# print(tools.xyeLi(category_count))
# time.sleep(1)
# # 记录函数执行后的时间戳
# end_time = time.time()
# # 计算函数执行所用的时间
# execution_time = end_time - start_time
#
# print(f"C++ Function executed in {execution_time} seconds")


start_time = time.time()
print(pyXueLI(category_count))
time.sleep(1)
# 记录函数执行后的时间戳
end_time = time.time()
# 计算函数执行所用的时间
execution_time = end_time - start_time
print(type(pyXueLI(category_count)))
print(f"PY Function executed in {execution_time} seconds")

# PY Function executed in 1.0065197944641113 seconds

#
# for category, count in category_count:
#     print(f'Category: {category}, Count: {count}')
