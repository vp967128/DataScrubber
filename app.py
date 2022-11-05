# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# from sqlalchemy import create_engine
# from sqlalchemy import MetaData, Table, Column, Integer, String, text

# engine = create_engine("postgresql://postgres:Passw0rd@localhost:5432/postgres")
# connection = engine.connect()

# with engine.connect() as conn:
#     conn = conn.execution_options(stream_results=True, max_row_buffer=100)
#     result = conn.execute(text("select * from table"))

#     for row in result:
#         print(f"{row}")

# metadata_obj = MetaData()
# users_table = Table(
#     "users",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(50)),
# )
# connection = engine.connect()

# print(engine.table_names())
  # ['census, 'state_fact']
# census = Table('', metadata, autoload = True, autoload_with=engine)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/files', methods=["GET"])
# '/' URL is bound with hello_world() function.
def hello_world():
    response = jsonify(message="OAF")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/', methods=["GET"])
# '/' URL is bound with hello_world() function.
def unique():
    response = jsonify(message="OAF")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", port="5000", debug=True)
