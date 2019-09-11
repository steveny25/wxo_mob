def read_txt(filename):
    with open("../data/"+filename,"r", encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt("login.txt"))
    print("--" * 50)

    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple((data.strip().split(","))))
    print(arrs[1::])

    """
        1. 字符串.strip(): 去除字符串前后空格、回车
        2. 字符串.split("指定符号"): 根据指定符号分隔字符串，以列表形式返回
    """