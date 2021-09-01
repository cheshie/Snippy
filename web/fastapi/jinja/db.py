from hashlib import sha256
from os import devnull

def login(cur, username, password):
    try:
        db_response = cur.execute("SELECT * FROM users WHERE username = " + "\'" + username + "\'").fetchone()
    except Exception as err:
        return f"SQLite Syntax Error: {str(err)}"

    if db_response is not None:
        db_user, db_pass = db_response
        hashed_password = sha256(password.encode()).hexdigest()
        if db_pass == hashed_password:
            # Successfully logged in
            return (True, db_user)
        else:
            return (False, None)
    else:
        return (False, None)




