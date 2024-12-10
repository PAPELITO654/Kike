<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD App</title>
</head>
<body>
    <h1>CRUD App</h1>
    <form method="POST" action="/add">
        <input type="text" name="name" placeholder="Item Name" required>
        <input type="text" name="description" placeholder="Description">
        <button type="submit">Add Item</button>
    </form>
    <ul>
        {% for item in items %}
        <li>
            <form method="POST" action="/edit/{{ item.id }}">
                <input type="text" name="name" value="{{ item.name }}">
                <input type="text" name="description" value="{{ item.description }}">
                <button type="submit">Edit</button>
            </form>
            <a href="/delete/{{ item.id }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
