# Setup
1. Install dependencies
```bash
   pip install requirements.txt
```
2. Create a new database "envtracker" in mysql
3. Run the "schema.sql" file to create the required tables
4. Create a .env file in root folder and sample is given below
```env
MASTER_USER = "root"
MASTER_PASSWORD = "root" 
DB_HOST = "localhost:3306/"
```
5. Start the application
```bash
   python app.py
```



