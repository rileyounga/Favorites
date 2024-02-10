import os

"""
messy bad code to hackily generate an html file from the markdown files in the Favourites folder
I tried using js but I just know python better
"""

def initialize_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Favorites</title>
</head>
<body>
    <table id="showsTable">
        <thead>
            <tr>
                <th>Image</th>
                <th>Title</th>
                <th>Medium</th>
                <th>Genre</th>
                <th>Review</th>
                <th>Rating</th>
            </tr>
        </thead>
        <tbody>
"""
    return html

def generate_html():
    html = initialize_html()
    favs = []
    for file in os.listdir('Favourites'):
        if file.endswith('.md'):
            with open('Favourites/'+file, 'r') as f:
                content = f.read()
                photo = content.split('photo: ')[1].split('\n')[0]
                name = file.split('.md')[0]
                medium = content.split('Medium: ')[1].split('\n')[0]
                genre = content.split('Genre: ')[1].split('\n')[0]
                review = content.split('Review: ')[1].split('\n')[0]
                rating = content.split('Rating: ')[1].split('\n')[0]
                favs.append((name, photo, medium, genre, review, rating))
    favs = sorted(favs, key=lambda x: (x[5], x[4]), reverse=True)
    # update the html: make title h3, make genre wrap in a span with a width of 200, and make review and rating h4 and bold
    for fav in favs:
        html += f"""            <tr>
                <td><img src="{fav[1]}" alt="{fav[0]}" width="300"></td>
                <td><h3>{fav[0]}</h3></td>
                <td>{fav[2]}</td>
                <td><span style="width: 100px">{fav[3]}</span></td>
                <td><h4>{fav[4]}</h4></td>
                <td><b>{fav[5]}</b></td>
            </tr>
"""
    html += """        </tbody>
    </table>
</body>
</html>
"""
    return html

def main():
    html = generate_html()
    with open('index.html', 'w') as f:
        f.write(html)

if __name__ == '__main__':
    main()

