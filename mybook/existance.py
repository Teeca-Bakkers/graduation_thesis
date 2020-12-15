#existance.py

def existance(c,name):
    c.execute("""
        SELECT COUNT(*) FROM sqlite_master 
        WHERE TYPE='table' AND name=name
        """)
    if c.fetchone()[0] == 0:
        return False
    return True

def index_existance(c,name):
    c.execute("""
        SELECT COUNT(*) FROM sqlite_master 
        WHERE TYPE='index' AND name=name
        """)
    if c.fetchone()[0] == 0:
        return False
    return True

