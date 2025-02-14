from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

POST_ID = 3 # Simple counter to create unique ID's


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    Adds a new post to the list of posts.

    Request Body:
        JSON containing 'title' and 'content' fields.

    Returns:
        Response: The new post or an error message if required fields are missing."""

    # Making sure POST_ID is modified as a global variable
    global POST_ID

    # Extract json data sent by the client in the body of the POST request
    data = request.get_json()

    # Validate input
    if not data or 'title' not in data or 'content' not in data:
        missing_fields = [field for field in ['title', 'content'] if field not in data]
        return jsonify({'error': 'Missing fields', 'fields': missing_fields}), 400

    # Create a new blog post and add it to the list
    new_post = {
        "id": POST_ID,
        "title": data["title"],
        "content": data["content"]
    }

    # Add new post to the list of posts
    POSTS.append(new_post)

    # Increment the unique id counter
    POST_ID += 1

    # Return the newly created post as JSON
    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
