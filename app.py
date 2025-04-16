from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# SQLite database connection function
def get_db_connection():
    conn = sqlite3.connect(r"D:\python\flaskproject\amazon_products.db")
    conn.row_factory = sqlite3.Row  # To fetch data by column names
    return conn


@app.route("/")
def index():
    # Fetch all products from the database
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    # Pass the products data to the index.html
    return render_template("index.html", products=products)


# Route for Computers category
@app.route("/computers")
def computers():
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE category LIKE '%Computers%'"
    ).fetchall()
    conn.close()
    return render_template("computers.html", products=products)


# Route for Electronics category
@app.route("/electronics")
def electronics():
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE category LIKE '%Electronics%'"
    ).fetchall()
    conn.close()
    return render_template("electronics.html", products=products)


# Route for Accessories & Peripherals category
@app.route("/accessories_peripherals")
def home_kitchen():
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE category LIKE '%Home & Kitchen%'"
    ).fetchall()
    conn.close()
    return render_template("Accessories & Peripherals.html", products=products)


# Route for Hometheater category
@app.route("/Accessories_Peripherals")
def home_theater():
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE category LIKE '%Hometheaters%'"
    ).fetchall()
    conn.close()
    return render_template("home_theater.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
