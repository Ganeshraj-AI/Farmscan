"""
Database module for FarmScan
Using SQLite for local data storage
"""

import sqlite3
import os
import hashlib
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, 'farmscan.db')

print("📦 DATABASE PATH USED:", DATABASE_FILE)

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn


def init_db():
    """Initialize database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            language TEXT DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Scans table (history)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_phone TEXT NOT NULL,
            disease_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            severity TEXT NOT NULL,
            treatment TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_phone) REFERENCES users(phone)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(name, phone, password):
    """
    Create a new user

    Returns:
        User dictionary if successful, None if phone already exists
    """
    print("USING DB:", os.path.abspath(DATABASE_FILE))

    try:
        phone = phone.strip()

        conn = get_db_connection()
        cursor = conn.cursor()

        password_hash = hash_password(password)

        cursor.execute('''
            INSERT INTO users (name, phone, password_hash)
            VALUES (?, ?, ?)
        ''', (name, phone, password_hash))

        conn.commit()
        conn.close()

        return {
            'name': name,
            'phone': phone,
            'language': None
        }

    except sqlite3.IntegrityError as e:
        print("INTEGRITY ERROR:", e)
        return None

    except Exception as e:
        print("CREATE USER ERROR:", e)
        return None



def verify_user(phone, password):
    try:
        phone = phone.strip()
        password_hash = hash_password(password)

        print("🔐 LOGIN ATTEMPT")
        print("PHONE:", phone)
        print("HASH:", password_hash)

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name, phone, language, password_hash FROM users WHERE phone = ?",
            (phone,)
        )

        row = cursor.fetchone()
        conn.close()

        if not row:
            print("❌ USER NOT FOUND")
            return None

        if row["password_hash"] != password_hash:
            print("❌ PASSWORD MISMATCH")
            return None

        print("✅ LOGIN SUCCESS")
        return {
            "name": row["name"],
            "phone": row["phone"],
            "language": row["language"]
        }

    except Exception as e:
        print("VERIFY USER ERROR:", e)
        return None

def update_user_language(phone, language):
    """
    Update user's preferred language
    
    Args:
        phone: User's phone number
        language: Language code (en, hi, ta)
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE users
            SET language = ?
            WHERE phone = ?
        ''', (language, phone))
        
        conn.commit()
        conn.close()
        return True
        
    except Exception as e:
        print(f"Error updating language: {e}")
        return False


def save_scan(scan_data):
    """
    Save a crop scan to history
    
    Args:
        scan_data: Dictionary with scan information
            - user_phone
            - disease_name
            - confidence
            - severity
            - treatment
    
    Returns:
        Scan ID if successful, None otherwise
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO scans (user_phone, disease_name, confidence, severity, treatment)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            scan_data['user_phone'],
            scan_data['disease_name'],
            scan_data['confidence'],
            scan_data['severity'],
            scan_data['treatment']
        ))
        
        scan_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return scan_id
        
    except Exception as e:
        print(f"Error saving scan: {e}")
        return None


def get_user_scans(phone, limit=50):
    """
    Get user's scan history
    
    Args:
        phone: User's phone number
        limit: Maximum number of scans to return
    
    Returns:
        List of scan dictionaries
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, disease_name, confidence, severity, treatment, date
            FROM scans
            WHERE user_phone = ?
            ORDER BY date DESC
            LIMIT ?
        ''', (phone, limit))
        
        scans = []
        for row in cursor.fetchall():
            scans.append({
                'id': row['id'],
                'disease_name': row['disease_name'],
                'confidence': row['confidence'],
                'severity': row['severity'],
                'treatment': row['treatment'],
                'date': row['date']
            })
        
        conn.close()
        return scans
        
    except Exception as e:
        print(f"Error getting scans: {e}")
        return []


def get_scan_by_id(scan_id, user_phone):
    """
    Get a specific scan by ID for a user
    
    Args:
        scan_id: Scan ID
        user_phone: User's phone number (for security)
    
    Returns:
        Scan dictionary or None
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, disease_name, confidence, severity, treatment, date
            FROM scans
            WHERE id = ? AND user_phone = ?
        ''', (scan_id, user_phone))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row['id'],
                'disease_name': row['disease_name'],
                'confidence': row['confidence'],
                'severity': row['severity'],
                'treatment': row['treatment'],
                'date': row['date']
            }
        return None
        
    except Exception as e:
        print(f"Error getting scan by ID: {e}")
        return None


def get_all_users():
    """Get all users (for admin purposes)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT name, phone, language, created_at FROM users')
        users = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return users
        
    except Exception as e:
        print(f"Error getting users: {e}")
        return []


if __name__ == '__main__':
    # Initialize database when run directly
    init_db()
    print("Database setup complete!")
