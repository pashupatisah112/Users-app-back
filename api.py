from flask import request, jsonify
from utils import read_json, write_json


def load_api(app):

    @app.route("/users/list/<int:num>", methods=["GET"])
    def getUsersList(num):
        try:
            data = read_json()
            if num == 0:
                response = data
            else:
                sorted_json = sorted(data, key=lambda x: x["name"])
                response = sorted_json[:3]
            return jsonify({"status": "success", "data": response})
        except Exception as e:
            print(e)
            return jsonify({"status": "failed", "msg": "Internal server error"})

    @app.route("/user/add", methods=["POST"])
    def addUser():
        try:
            userData = request.json["userData"]
            data = read_json()
            userData["id"] = len(data) + 1
            data.append(userData)
            write_json(data)
            return jsonify({"status": "success", "data": userData})
        except Exception as e:
            print(e)
            return jsonify({"status": "failed", "msg": "Internal server error"})

    @app.route("/user/update/<int:user_id>", methods=["PUT"])
    def updateUsersList(user_id):
        try:
            userData = request.json["userData"]
            data = read_json()
            for user in data:
                if user["id"] == user_id:
                    user.update(userData)
                    write_json(data)
            return jsonify({"status": "success", "data": userData})
        except Exception as e:
            print(e)
            return jsonify({"status": "failed", "msg": "Internal server error"})

    @app.route("/user/delete/<int:user_id>", methods=["DELETE"])
    def deleteUser(user_id):
        try:
            data = read_json()
            userdata = [user for user in data if user["id"] != user_id]
            for index, ud in enumerate(userdata):
                userdata[index]["id"] = index + 1
            write_json(userdata)
            return jsonify({"status": "success", "data": data})
        except Exception as e:
            print(e)
            return jsonify({"status": "failed", "msg": "Internal server error"})

    @app.route("/user/<int:user_id>", methods=["GET"])
    def getUserDetails(user_id):
        try:
            data = read_json()
            data = [user for user in data if user["id"] == user_id]
            return jsonify({"status": "success", "data": data[0]})
        except Exception as e:
            return jsonify({"status": "failed", "msg": "Internal server error"})

    @app.route("/users/count", methods=["GET"])
    def getUsersCount():
        try:
            data = read_json()
            return jsonify({"status": "success", "data": len(data)})
        except Exception as e:
            return jsonify({"status": "failed", "msg": "Internal server error"})
