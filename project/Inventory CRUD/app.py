from flask import Flask, render_template, request,redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcom to Invetory Management App"

@app.route('/inventory')
def inventory():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()

    return render_template('inventory.html',items=items)

@app.route('/admin')
def admin():
    # Fetch inventory items from the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    
    return render_template('admin.html', items=items)

@app.route('/admin/add_item',methods=["POST"])
def add_item():
    name = request.form['name']
    quantity = request.form['quantity']

    #inset into database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name,quantity) VALUES (?, ?)', (name,quantity))
    conn.commit()
    conn.close()
    return redirect('/admin')

@app.route('/admin/edit_item/<int:id>',methods=['GET','POST'])
def edit_item(id):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        item = cursor.fetchone()
        conn.commit()
        conn.close()
        return render_template('edit_item.html',item=item)
    # elif request.method == 'POST':
    #     name = request.form['name']
    #     quantity= request.form['quantity']
    #     conn = sqlite3.connect('database.db')
    #     cursor = conn.cursor()
    #     cursor.execute('UPDATE items SET name=?, quantity=? WHERE id=?', (name,quantity,id))
    #     conn.commit()
    #     conn.close()
    #     return redirect('/admin')
    
    elif request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        
        # Update the item in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE items SET name=?, quantity=? WHERE id=?', (name, quantity, id))
        conn.commit()
        conn.close()
        
        return redirect('/admin')
    
@app.route('/admin/delete_item/<int:id>',methods=['GET','POST'])
def delete_item(id):
    if request.method == 'GET':
        #fetch data from database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items WHERE id=?',(id,))
        item = cursor.fetchone()
        conn.close()
        return render_template('delete_item.html',item=item)

    elif request.method == 'POST':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id=?',(id,))
        conn.commit()
        conn.close()
        return redirect('/admin')
    
if __name__ == '__main__':
    app.run(debug=True)
