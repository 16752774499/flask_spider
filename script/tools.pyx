# 定义Cython函数
cpdef xyeLi(items: list):
    cdef int i = 0
    cdef int otherCount = 0
    while i < len(items):
        if (items[i][0] == "NULL") or ("月" in items[i][0]):
            otherCount += items[i][1]
            i += 1
        else:
            i += 1
    items.append(("其他", otherCount))
    filtered_list = [item for item in items if "月" not in item[0] and item[0] != "NULL"]
    return filtered_list
