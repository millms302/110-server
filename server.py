from flask import Flask, jsonify, request
from http import HTTPStatus

app =Flask(__name__) #Instance of Flask#


# http://127.0.0.1:5000/ <= Visit this endpoint
@app.route("/", methods=["GET"])
def index():
    return "Welcome To Flask Framework"

# http://127.0.0.1:5000/cohort-62 <= Visit this endpoint.
@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = ["Michael", "Tyler", "Carlos", "Jonathan", "Kirt"]
    return students_list



# http://127.0.0.1.5000/cohort-100
@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = ["Pam", "Dwight", "Michael", "Oscar"]
    return students_list

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "blink18mike@gmail.com", "home": "314-867-5309"}
    return information

# http://127.0.0.1:5000/course_information
@app.route("/course_information", methods=["GET"])
def course_information():
    course_information = {
        "title": "Introduction Web API with Flask",
        "duration": "4 sessions",
        "level": "beginner"
        }
    return course_information

# MINI CHALLENGE 1
@app.route("/api/user", methods=["GET"])
def user():
    user = {"name": "Mike", "role": "Student", "is_active": True, "favorite_technologies": "python"}
    return user, HTTPStatus.OK

# Path Paremeter
# Is a dynamic part of the url used to identify A specific item or recource withing the API.
@app.route("/greet/<string:name>")
def greet(name):
    return {"message": f"Hello {name}"}

# -----PRODUCTS-----
products = [
  {
    "_id": 1,
    "title": "Nintendo Switch",
    "price": 299.99,
    "category": "Entertainment",
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2,
    "title": "Smart Refrigerator SE",
    "price": 999.99,
    "category": "Kitchen",
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3,
    "title": "Bluetooth Speaker",
    "price": 79.99,
    "category": "Electronics",
    "image": "https://picsum.photos/seed/3/300/300"
  }
]

# GET /api/products Endpoint that returns a list of products.
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieves successfully",
        "data": products
        }), HTTPStatus.OK

# GET /api/products/2 Gets the item by the number
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
        print(product)
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Products retrieves successfully",
                "data": product
            }), HTTPStatus.OK # 200

    return jsonify({
        "success": False,
        "message": "Product Not Found"
    }), HTTPStatus.NOT_FOUND # 404

# POST /api/products
@app.route("/api/products/", methods=["POST"])
def create_product():
    print(request.get_json())
    new_product = request.get_json()
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Products retrieves successfully",
        "data": new_product
    }), HTTPStatus.CREATED # 201
    
# PUT /api/products
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    print(data)

    for product in products:
        if product["_id"] == product_id:
            product["title"] = data["title"]
            product["price"] = data["price"]
            product["category"] = data["category"]
            product["image"] = data["image"]
            return jsonify({
                "success": True,
                "message": "Product Updated Successfully",
                "data": data
            }), HTTPStatus.OK
    return jsonify({
        "success": False,
        "message": "Product Not Found"
    }), HTTPStatus.NOT_FOUND

# DELETE /api/products
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for index, product in enumerate(products):
        if product["_id"]  == product_id:
            products.pop(index)
            return jsonify({
                "success": True,
                "message": "Product Deleted Successfully"
            }), HTTPStatus.OK # 200
    return jsonify({
        "success": False,
        "Message": "Product Not Found" 
    }), HTTPStatus.NOT_FOUND # 404



# ----------Coupons---------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]


    #GET
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return {"coupons": coupons}

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return {"get_coupons_count": len(coupons)}

@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    print(request.get_json())
    new_coupon = request.get_json()
    coupons.append(new_coupon)
    return jsonify({
        "success":True,
        "message": "Coupon Created Successfully",
        "data": new_coupon
    }), HTTPStatus.CREATED

@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):
    for coupon in coupons:
        print(coupon)
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "Products retrieves successfully",
                "data": coupon
            }), HTTPStatus.OK

    return "Not Found"

# PUT /api/coupons
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon(coupon_id):
    data = request.get_json()
    print(data)

    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupon["code"] = data["code"]
            coupon["discount"] = data["discount"]
            return jsonify({
                "success": True,
                "message": "Coupon Updated Successfully",
                "data": data
            }), HTTPStatus.OK
    return jsonify({
        "success": False,
        "message": "Coupon Not Found"
    }), HTTPStatus.NOT_FOUND


# DELETE /api/coupons
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon(coupon_id):
    for index, coupon in enumerate(coupons):
        if coupon["_id"]  == coupon_id:
            coupons.pop(index)
            return jsonify({
                "success": True,
                "message": "Coupon Deleted Successfully"
            }), HTTPStatus.OK # 200
    return jsonify({
        "success": False,
        "Message": "Product Not Found" 
    }), HTTPStatus.NOT_FOUND # 404



if __name__ =="__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module:__name == "server.py"