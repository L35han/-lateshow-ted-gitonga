import os
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///your_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Episode, Guest, Appearance

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify({
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': [appearance.to_dict() for appearance in episode.appearances]
    }), 200

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

@app.route('/appearances', methods=['POST'])
def create_appearance():
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if not rating or not episode_id or not guest_id:
        return jsonify({"errors": ["Missing required fields"]}), 400

    try:
        new_appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(new_appearance)
        db.session.commit()
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

    return jsonify(new_appearance.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
