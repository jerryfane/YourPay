from bottle import route, install, run, template
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='data.db'))

@route('/show/<Amount:int>')
def show(db, Amount):
    c = db.execute('SELECT * FROM Data WHERE Amount = ?', (Amount,))
    row = c.fetchone()
    return template('show_post', title=row['Date'], text=row['Amount'])

@route('/contact')
def contact_page():
    ''' This callback does not need a db connection. Because the 'db'
        keyword argument is missing, the sqlite plugin ignores this callback
        completely. '''
    return template('contact')


run(host='localhost', port=8080)
