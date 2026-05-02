import json 
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    
    # FIX: Handle empty birthday strings safely for PostgreSQL
    if birthday.strip() == "":
        birthday = None

    group = input("Group: ")
    
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    g = cur.fetchone()
    group_id = g[0] if g else None
    
    if not g and group.strip() != "":
        cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group,))
        group_id = cur.fetchone()[0]
        
    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (name, email, birthday, group_id))
    
    contact_id = cur.fetchone()[0]
    
    while True:
        phone = input("Phone (enter to stop): ")
        if not phone:
            break
        ptype = input("Type (home/work/mobile): ")
        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s,%s,%s)
        """, (contact_id, phone, ptype))
        
    conn.commit()
    print(f"\nContact '{name}' added successfully!")
    
def view_contacts():
    cur.execute("""
        SELECT c.id, c.name, c.email, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.name
    """)
    
    rows = cur.fetchall()
    if not rows:
        print("Phonebook is empty.")
    else:
        for row in rows:
            print(row)
        
def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    rows = cur.fetchall()
    if not rows:
        print("No matches found.")
    else:
        for r in rows:
            print(r)
    
def filter_group():
    g = input("Group: ")
    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name=%s         
    """, (g,))
    rows = cur.fetchall()
    if not rows:
        print(f"No contacts found in group '{g}'.")
    else:
        for r in rows:
            print(r)
        
def pagination():
    limit = 3
    offset = 0
    
    while True:
        cur.execute("""
            SELECT name, email FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s          
        """, (limit, offset))
    
        rows = cur.fetchall()
        if not rows and offset == 0:
            print("Phonebook is empty.")
            break
            
        for r in rows:
            print(r)
        
        cmd = input("n-next, p-prev, q-quit: ").lower()
        if cmd == "n":
            offset += limit
        elif cmd == "p" and offset >= limit:
            offset -= limit
        else:
            break
        
def export_json():
    cur.execute("SELECT * FROM contacts")
    contacts = []
    
    for c in cur.fetchall():
        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (c[0],))
        phones = [{"phone":p,"type":t} for p,t in cur.fetchall()]
        
        contacts.append({
            "id": c[0],
            "name": c[1],
            "email": c[2],
            "birthday": str(c[3]) if c[3] else None, 
            "group_id": c[4],
            "phones": phones
        })
        
    # FIX: Write to file ONCE after the loop finishes
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts exported to contacts.json")
            
def import_json():
    try:
        with open("contacts.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 'contacts.json' not found.")
        return
        
    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (c["name"],))
        ex = cur.fetchone()
            
        if ex:
            ans = input(f"Contact '{c['name']}' exists. Overwrite? y/n: ")
            if ans.lower() == "n":
                continue
            cid = ex[0]
            # FIX: Clear old phones and update the contact record properly
            cur.execute("DELETE FROM phones WHERE contact_id=%s", (cid,))
            cur.execute("""
                UPDATE contacts 
                SET email=%s, birthday=%s, group_id=%s 
                WHERE id=%s
            """, (c.get("email"), c.get("birthday"), c.get("group_id"), cid))
        else:
            # FIX: Changed VALUE to VALUES
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id) 
                VALUES(%s, %s, %s, %s) RETURNING id
            """, (c["name"], c.get("email"), c.get("birthday"), c.get("group_id")))
            cid = cur.fetchone()[0]
                
        for p in c.get("phones", []):
            cur.execute("INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)",
                        (cid, p["phone"], p["type"]))
            
    conn.commit()
    print("Import successful!")
    

while True:
    print("\n=== PhoneBook ===")
    print("1-Add | 2-View | 3-Search | 4-Filter | 5-Page | 6-Export | 7-Import | 0-Exit")
    chc = input("Choose: ")
    
    if chc == "1": add_contact()
    elif chc == "2": view_contacts()
    elif chc == "3": search()
    elif chc == "4": filter_group()
    elif chc == "5": pagination()
    elif chc == "6": export_json()
    elif chc == "7": import_json()
    elif chc == "0": break
    else: print("Invalid choice.")

conn.commit()
cur.close()
conn.close()