```dataview
table without id 
	("![](" + photo + ")") as Photo, 
	file.link as Name, 
	Medium, 
	Genre, 
	Review, 
	Rating
from "Favourites"
sort Rating desc, Review desc
```