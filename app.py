from flask import Flask, jsonify, render_template, request
import pymysql.cursors

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'playerdb'

def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return render_template('fetch_all.html')

@app.route('/fetch_all')
def fetch_all():
    return render_template('fetch_all.html')

@app.route('/fetch_by_id')
def fetch_by_id():
    return render_template('fetch_by_id.html')

@app.route('/api/players', methods=['GET'])
def get_players():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    offset = (page - 1) * limit
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) as total FROM players')
            total = cursor.fetchone()['total']
            cursor.execute('SELECT * FROM players LIMIT %s OFFSET %s', (limit, offset))
            players = cursor.fetchall()
        connection.close()
        return jsonify({'players': players, 'total': total})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM players WHERE id = %s', (player_id,))
            player = cursor.fetchone()
        connection.close()
        if not player:
            return jsonify({'error': 'Player not found'}), 404
        return jsonify(player)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
