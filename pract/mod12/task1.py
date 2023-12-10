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

# Вспомогательная таблица
c.execute("create table af( actor varchar(200), id_film int)")

k = 0
f = []
for row in c.execute("SELECT show_id, [cast]  FROM netflix_titles"):
    data = row[1].split(',')
    for d in data:
        print(k)
        if len(d) != 0:
            f.append((row[0], d.strip()))
            k = k + 1

i = 0

while i < k:
    c.execute("insert into af (id_film,actor) values (?,?)", f[i])
    i = i + 1

c.execute(
    "create table actor_film (id int not null primary key, id_actor int, id_film int, FOREIGN KEY(id_actor) REFERENCES actor(id),FOREIGN KEY (id_film) REFERENCES netflix_titles (show_id))")
k = 0
f = []
for row in c.execute("SELECT af.id_film,  actor.id FROM af, actor where af.actor=actor.name"):
    print(k)
    f.append((k, row[1], row[0]))
    k = k + 1
i = 0

while i < k:
    c.execute("insert into actor_film (id,id_actor, id_film) values (?,?,?)", f[i])
    i = i + 1

#  Ищем наиболее часто работающую друг с другом пару актеров
c.execute(
    "select a.id_actor, b.id_actor, count() as cnt FROM actor_film a, actor_film b where a.id_film=b.id_film and a.id_actor<>b.id_actor group by a.id_actor, b.id_actor order by cnt desc")
c.fetchall()

John
Paul
Tremblay
Robb
Wells