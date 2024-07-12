#include <iostream>
#include <vector>
#include <string>
#include <Windows.h>

void mergeItems(std::vector<std::pair<std::string, int>> &items)
{
    int otherCount = 0;
    int i = 0;
    while (i < items.size())
    {
        if (items[i].first.find("月") != std::string::npos || items[i].first == "NULL")
        {
            otherCount += items[i].second;
            items.erase(items.begin() + i);
        }
        else
        {
            i++;
        }
    }
    items.push_back({"其他", otherCount});
}

// int main()
// {
//     SetConsoleOutputCP(CP_UTF8); // 设置控制台输出为 UTF-8 编码
//     std::vector<std::pair<std::string, int>> items = {
//         {"10个月", 1}, {"12个月", 13}, {"1个月", 30}, {"2个月", 20}, {"3个月", 99}, {"4个月", 11}, {"5个月", 4}, {"6个月", 41}, {"8个月", 2}, {"NULL", 17}, {"中专/中技", 13}, {"初中及以下", 7}, {"博士", 2}, {"大专", 390}, {"学历不限", 153}, {"本科", 1239}, {"硕士", 30}, {"高中", 9}};
//
//     mergeItems(items);
//
//     for (const auto &item : items)
//     {
//         std::cout << item.first << ": " << item.second << std::endl;
//     }
//
//     return 0;
// }
