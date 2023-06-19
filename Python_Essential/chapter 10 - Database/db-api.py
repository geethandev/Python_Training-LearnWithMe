import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('Python_Essential/chapter 10 -db/db-api.db')
    cur = db.cursor()
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
                CREATE TABLE TEST (
                    ID INTEGER PRIMARY KEY,
                    string TEXT,
                    number INTEGER
                )
                """)
    print('insert row')
    cur.execute("""
                INSERT INTO TEST(string, number) VALUES ('one', 1)
                """)
    cur.execute("""
                INSERT INTO TEST(string, number) VALUES ('two', 2)
                """)
    cur.execute("""
                INSERT INTO TEST(string, number) VALUES ('three', 3)
                """)
    db.commit()
    print('display all')
    
    for row in db.execute("""
               SELECT * FROM TEST
               """):
        print(row)
        
    print('display count')
    
    cur.execute("""
               SELECT COUNT(*) FROM TEST
               """)
    count = cur.fetchone()[0]
    print('Count:', count)
    
    print('close')
    db.close()

if __name__ == '__main__':
    main()
