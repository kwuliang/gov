import xlrd
import hashlib


def get_start_urls(path):

    print(f"Crawling sites from {path} ...")

    allowed_domains = []
    start_urls = []
    if path.endswith(".txt"):
        allowed_domains, start_urls = read_txt(path)
    elif path.endswith(".xls"):
        allowed_domains, start_urls = read_excel(path)
    else:
        print("站点格式请使用txt格式或者excel")


    return allowed_domains, start_urls

def read_txt(path):
    allowed_domains = []
    start_urls = []
    with open(path, 'r', encoding='utf-8') as infos:
        for info in infos:  # 跳过第一行
            # print(info)
            arrs = info.split('\t', 1)
            start_urls.append(arrs[-1].replace("\n", ""))
            allowed_domains.append(arrs[-1].split('/')[2])

    return allowed_domains, start_urls

def read_excel(path):
    allowed_domains = []
    start_urls = []

    workbook=xlrd.open_workbook(path)
    # 获取所有sheet
    # sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    cols = sheet.col_values(1) # 获取第2列内容

    for info in cols:  # 跳过第一行
        # print(info)
        start_urls.append(info)
        allowed_domains.append(info.split('/')[2])

    return allowed_domains, start_urls


def make_file_name(raw_name, extension):
    return md5_encode(raw_name) + "." + extension

def md5_encode(data):
    md5 = hashlib.md5()
    md5.update(str(data).encode("utf-8"))
    return md5.hexdigest() 
