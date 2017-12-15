# coding: utf-8

def parse_file(file_path):
    content = open(file_path, encoding='utf8', errors='ignore');
    result = ''
    import json
    c = content.read()
    c_list = json.loads(c)
    index = 2

    for c_content in c_list:
        temp = "('" + c_content["value"] + "', 6, 1),"
        result += temp

    # for c_content in c_list:
    #     for c_content2 in c_content["values"]:
    #         temp = "('" + c_content2["name"] + "'," + str(index) + ", 1),"
    #         result += temp
    #     index += 1
    return result


if __name__ == "__main__":
    file_base_path = r"C:\Users\admin\Documents\WeChat Files\wxid_ncqrrpdqdj3o22\Files\tag\tag\\"
    name = "sport.cn"
    print(parse_file(file_base_path + name))
