import sqlite3

conn = sqlite3.connect('netflix.sqlite')

c = conn.cursor()

c.execute("create table actor (id int not null primary key, name nvarchar(200))")
k = 0
f = []
for row in c.execute("SELECT [cast]  FROM netflix_titles"):
    data = row[0].split(',')
    for d in data:
        print(k)
        if len(d) != 0:
            f.append(d.strip())
            k = k + 1
f.sort()
i = 0

while i < k:
    fl = f[i]
    a = (i + 1, fl)
    c.execute("insert into actor (id,name) values (?,?)", a)
    while i < k and f[i] == fl:
        i = i + 1

c.execute(
    "create table actor_film (id int not null primary key, id_actor int, id_film int, FOREIGN KEY(id_actor) REFERENCES actor(id),FOREIGN KEY (id_film) REFERENCES netflix_titles (show_id))")