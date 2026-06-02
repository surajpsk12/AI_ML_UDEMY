'''
PUT and DELETE methods in Flask are used to handle HTTP requests that modify resources on the server.
working with api json data and flask

'''


from flask import Flask, render_template, request , jsonify


app = Flask(__name__)




#initial data 
items = [
    {'id':1, 'name':'item1', 'description': 'This is item 1'},
    {'id':2, 'name':'item2', 'description': 'This is item 2'},
    {'id':3, 'name':'item3', 'description': 'This is item 3'}
]

@app.route('/')
def home():
    return "Welcome to TODO app"

#get : retrive all the items 

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Accept trailing slash as well (helps clients that include it)
@app.route('/items/', methods=['GET'])
def get_items_slash():
    return get_items()

#get : retrive a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}) 
    
#post : create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': data['name'],
        'description': data['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201


#put : update an existing item by id
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item['name'] = data.get('name', item['name'])
        item['description'] = data.get('description', item['description'])
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'})
    
#delete : delete an item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

 











if __name__ == '__main__':
    import sys
    print('=== Flask URL Map ===')
    print(app.url_map)
    sys.stdout.flush()
    app.run(debug=True)
