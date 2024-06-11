import csv
from app import app
from models import db, Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        db.create_all()

        # Seed episodes
        episodes = [
            {'id': 1, 'date': '1/11/99', 'number': 1},
            {'id': 2, 'date': '1/12/99', 'number': 2}
        ]
        for ep in episodes:
            episode = Episode(id=ep['id'], date=ep['date'], number=ep['number'])
            db.session.add(episode)

        # Seed guests
        guests = [
            {'id': 1, 'name': 'Michael J. Fox', 'occupation': 'actor'},
            {'id': 2, 'name': 'Sandra Bernhard', 'occupation': 'Comedian'},
            {'id': 3, 'name': 'Tracey Ullman', 'occupation': 'television actress'}
        ]
        for guest in guests:
            g = Guest(id=guest['id'], name=guest['name'], occupation=guest['occupation'])
            db.session.add(g)

        # Seed appearances
        appearances = [
            {'id': 1, 'rating': 4, 'guest_id': 1, 'episode_id': 1}
        ]
        for appearance in appearances:
            a = Appearance(id=appearance['id'], rating=appearance['rating'], guest_id=appearance['guest_id'], episode_id=appearance['episode_id'])
            db.session.add(a)

        db.session.commit()

if __name__ == "__main__":
    seed_data()
