#!/usr/bin/env python2.7

import psycopg2
import bleach

DBNAME = "news"

cmd1 = """
select title, v.views
from articles,
(
select path, count(path) as views
from log where path <> '/' and status = '200 OK'
group by path order by views desc
) as v
where v.path = concat('/article/', articles.slug)
limit 3;
"""

cmd2 = """
select name, sum(tmp.views) as totalViews
from authors join
(select author, totalViews.views
from articles join
(select path, count(path) as views from log
where path <> '/' and status = '200 OK'
group by path) as totalViews
on totalViews.path = concat('/article/', articles.slug)
) as tmp
on authors.id = tmp.author
group by authors.name
order by totalViews desc;
"""

cmd3 = """
with viewCountsByDate as
(
select to_char(date(time), 'FMMonth DD, YYYY') as date, status, count(status)
from log group by date(time), status
)
select c1.date,
concat(round((100.0 * c2.count / (c1.count + c2.count)), 2), '%') error_Ratio
from viewCountsByDate c1, viewCountsByDate c2
where c1.status = '200 OK' and c2.status = '404 NOT FOUND'
and c1.date = c2.date
and (100.0 * c2.count / (c1.count + c2.count)) > 1;
"""


def get_posts(cmd):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(cmd)
    posts = c.fetchall()
    db.close()
    return posts


if __name__ == '__main__':
    print '1. Most viewed articles:'
    for name, count in get_posts(cmd1):
        print('"{}" -- {} views'.format(name, count))

    print "\n2. Most popular article authors of all time:"
    for name, count in get_posts(cmd2):
        print('{} -- {} views'.format(name, count))

    print "\n3. Date when more than 1% of requests lead to errors:"
    for name, count in get_posts(cmd3):
        print('{} -- {} errors'.format(name, count))
