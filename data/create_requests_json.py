# -*- encoding: utf-8 -*-
import json
import pymysql.cursors

JSON_FILE_PATH = "data/multi-request.json"

REAL_DB_CONFIG = {
    "name": "dcos_circle",
    "host": "172.24.6.216",
    "port": 40006,
    "user": "dcos_circle",
    "password": "dcos_circle",
    "charset": "utf8"
}

TEST_DB_CONFIG = {
    "name": "circle",
    "host": "192.168.13.21",
    "port": 3306,
    "user": "circle",
    "password": "circle",
    "charset": "utf8"
}
DB_CONFIG = TEST_DB_CONFIG

MULTI_REQUEST_PATH = "/v1.0/cicd/api/project/{}/build"
MULTI_REQUEST_BODY = '{"description": "This is description"}'
MULTI_REQUEST_METHOD = "POST"
MULTI_REQUEST_HEADERS = {
    "Content-Type": "application/json",
    "X-Auth-Token": ""
}

# Connect to the database
connection = pymysql.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    db=DB_CONFIG["name"],
    charset=DB_CONFIG["charset"],
    cursorclass=pymysql.cursors.DictCursor
)


def get_data():
    SQL = "SELECT `id`, `name` FROM `project`"
    data = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(SQL)
            data = cursor.fetchmany()
    finally:
        connection.close()
    return data


def dump_json(data):
    req_template = {
        "path": None,
        "body": None,
        "method": None,
        "headers": None
    }
    result = []
    for project in data:
        req = req_template.copy()
        req["path"] = MULTI_REQUEST_PATH.format(project['id'])
        req["body"] = MULTI_REQUEST_BODY
        req["method"] = MULTI_REQUEST_METHOD
        req["headers"] = MULTI_REQUEST_HEADERS
        result.append(req)

    with open(JSON_FILE_PATH, "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    projects = get_data()
    dump_json(projects)