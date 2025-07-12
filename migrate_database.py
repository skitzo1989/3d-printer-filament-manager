#!/usr/bin/env python3
"""
Database migration script to add new columns for recommended temperature and print speed
"""

import sqlite3
import os

def migrate_database():
    """Add new columns to existing filament database"""
    db_path = "filament_inventory.db"
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found. No migration needed.")
        return
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if the new columns already exist
        cursor.execute("PRAGMA table_info(filaments)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print(f"Current columns: {columns}")
        
        # Add nozzle_temp_recommended column if it doesn't exist
        if "nozzle_temp_recommended" not in columns:
            print("Adding nozzle_temp_recommended column...")
            cursor.execute("ALTER TABLE filaments ADD COLUMN nozzle_temp_recommended INTEGER")
            print("✓ Added nozzle_temp_recommended column")
        else:
            print("✓ nozzle_temp_recommended column already exists")
        
        # Add print_speed_recommended column if it doesn't exist
        if "print_speed_recommended" not in columns:
            print("Adding print_speed_recommended column...")
            cursor.execute("ALTER TABLE filaments ADD COLUMN print_speed_recommended INTEGER")
            print("✓ Added print_speed_recommended column")
        else:
            print("✓ print_speed_recommended column already exists")
        
        # Commit changes
        conn.commit()
        print("\n✅ Database migration completed successfully!")
        
        # Show updated table structure
        cursor.execute("PRAGMA table_info(filaments)")
        columns = cursor.fetchall()
        print("\nUpdated table structure:")
        for column in columns:
            print(f"  {column[1]} ({column[2]})")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_database()