csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list():
    data = _read_users()
    sorted_data = _sort_users(data)
    filtered_data = _filter_users(sorted_data)
    return filtered_data

def _read_users():
    data = [x.split(";") for x in csv.split("\n")]
    return data


def _sort_users(data):
    data = sorted(data, key= lambda x: int(x[1]))
    return data


def _filter_users(sorted_data):
    filtered_data = [x for x in sorted_data if int(x[1]) > 10]
    return filtered_data


if __name__ == '__main__':
    print(get_users_list())
