
## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/player-api.git
    cd player-api
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your MySQL database:**

    - Ensure MySQL is running on your local machine.
    - Create a database and import your player data.

    ```sql
    CREATE DATABASE playerdb;
    USE playerdb;
    -- Import your data into a table named 'players'
    ```

6. **Update the MySQL configuration in `app.py`:**

    ```python
    app.config['MYSQL_HOST'] = 'your_mysql_host'
    app.config['MYSQL_USER'] = 'your_mysql_user'
    app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
    app.config['MYSQL_DB'] = 'playerdb'
    ```

## Running the Application

1. **Navigate to your project directory:**

    ```bash
    cd project_directory
    ```

2. **Activate the virtual environment (if not already activated):**

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Run the Flask application:**

    ```bash
    python app.py
    ```

4. **Open your browser and navigate to:**

    ```plaintext
    http://127.0.0.1:5000/
    ```

## API Endpoints

1. **Fetch All Players:**

    ```plaintext
    GET /api/players?page=1&limit=25
    ```

    - Returns a list of all players, paginated.
    - Query parameters:
        - `page` (optional): The page number (default is 1).
        - `limit` (optional): The number of players per page (default is 25).

2. **Fetch Player by ID:**

    ```plaintext
    GET /api/players/<player_id>
    ```

    - Returns a single player by ID.
    - URL parameter:
        - `player_id`: The ID of the player to fetch.

## HTML Pages

1. **Fetch All Players:**

    - Navigate to `http://127.0.0.1:5000/fetch_all` to view a table of all players with pagination.

2. **Fetch Player by ID:**

    - Navigate to `http://127.0.0.1:5000/fetch_by_id` to fetch and display a player by their ID.

## Testing

1. **Run the tests:**

    ```bash
    pytest test_app.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
