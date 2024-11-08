import sqlite3

def print_db_tables_and_data(db_file):
    # Connect to the database file
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # Fetch all tables in the database
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    
    # Print out the list of tables
    print("Tables in the database:")
    for i, table in enumerate(tables, start=1):
        print(f"{i}. {table[0]}")
    
    # Ask user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    
    if 0 <= table_index < len(tables):
        selected_table = tables[table_index][0]
        
        # Fetch all data from the selected table
        c.execute(f"SELECT * FROM {selected_table}")
        rows = c.fetchall()
        
        # Print data from the selected table
        print(f"\nData from table '{selected_table}':")
        for row in rows:
            print(row)
    else:
        print("Invalid table selection.")
    
    # Close the connection
    conn.close()

# Example usage
print_db_tables_and_data('quiz.db')
