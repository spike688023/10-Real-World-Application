import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # 建立一個table 叫 store, 後面的() 是表格的column 以及每個column的屬性
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

"""
這裡不懂 ，為什麼少了， item, 後 面的, 就 會出現以下的錯誤。
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 6 supplied.

我把原本傳入的 (item) 改成[item] , 就 可以了。

img 是個74 chars list , 傳入的東西不一樣
>> len(img)
74
>>> len((img,))
1

Error 寫6 supplied 是因為 ，我傳入的item 是Coffee 它是6個字元，

不加, 它會以為我傳入6個參數， 但sqlite的語法，只有一個? 。

而且， 這裡刪，是把所 有Coffee item都刪了。

Reference:
https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
"""
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", [item])
    conn.commit()
    conn.close()


"""
sql 的語法，有個特色， 有關語 法的字，全都大寫。
不用大寫 sql的解析器 也會認 得 ， 但都大寫是給 人方便讀。
"""
def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", [quantity, price, item])
    conn.commit()
    conn.close()

create_table()
print( insert("Wine Glass",8,10.5) )
delete("Coffee" )
update(10, 12.5, "Wine Glass")

print(view())

