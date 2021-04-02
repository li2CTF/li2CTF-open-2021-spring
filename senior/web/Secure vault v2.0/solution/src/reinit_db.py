import sqlite3
import os


def reinit():
    DATABASE_NAME = 'vault.db'

    os.system('rm {} && touch {}'.format(DATABASE_NAME, DATABASE_NAME))
    conn = sqlite3.connect(DATABASE_NAME)

    c = conn.cursor()
    c.execute('''CREATE TABLE users
                (id INTEGER PRIMARY KEY,
                username text, 
                password text)''')


    users =  [
        ('user', 'user'),
        ('dima', 'qwerty123'),
        ('vasya', 'Zxp0-aD1bMDl'),
        ('admin', 'admin'),
        ('alex', '1_4M_N07_4_FL4G_L0L'),
        ('sultanowskii', 'h0w_d1d_y0u_g07_7h3r3')
    ]


    c.executemany('INSERT INTO users(username, password) VALUES (?,?)', users)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    reinit()
