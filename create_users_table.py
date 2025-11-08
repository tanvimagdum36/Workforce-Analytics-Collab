import sqlite3
import os
import hashlib

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'workforce.db')
DB_PATH = os.path.abspath(DB_PATH)

# Ensure database folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create users table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'HR', 'Manager', 'Employee'))
)
""")

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create a default admin user
default_admin_username = "admin"
default_admin_password = hash_password("Admin@123")
default_admin_role = "Admin"

cursor.execute("SELECT * FROM users WHERE username = ?", (default_admin_username,))
if not cursor.fetchone():
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (default_admin_username, default_admin_password, default_admin_role))
    print("✅ Default admin user created (username: admin, password: Admin@123)")
else:
    print("ℹ️ Admin user already exists.")

conn.commit()
conn.close()

print(f"✅ Database setup completed at: {DB_PATH}")
