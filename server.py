from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import PlayerForm, GameForm, FlowerForm
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration from environment variables
db_user = os.environ.get('DB_USER', 'your_db_user')
db_password = os.environ.get('DB_PASSWORD', 'your_db_password')
db_endpoint = os.environ.get('DB_ENDPOINT', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'truco_db')

# Chatbot configuration
bot_workflow_id = os.environ.get('BOT_WORKFLOW_ID', 'your-bot-workflow-id')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'postgresql://{db_user}:{db_password}@{db_endpoint}:{db_port}/{db_name}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Defining the data models
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    games = db.relationship('Game', backref='player', lazy=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    win = db.Column(db.Boolean, nullable=False)  # True for win, False otherwise
    loss = db.Column(db.Boolean, nullable=False)  # True for loss, False otherwise

class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

@app.route('/')
def index():
    players = Player.query.order_by(Player.name).all()
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    if form.validate_on_submit():
        new_player = Player(name=form.name.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_player.html', form=form)

@app.route('/record_game', methods=['GET', 'POST'])
def record_game():
    form = GameForm()
    player_choices = [(p.id, p.name) for p in Player.query.all()]
    player_choices.insert(0, ('', 'Select player'))  # add a default option
    form.winner1.choices = player_choices
    form.winner2.choices = player_choices
    form.loser1.choices = player_choices
    form.loser2.choices = player_choices
    if form.validate_on_submit():
        new_game_winner1 = Game(player_id=form.winner1.data, win=True, loss=False)
        new_game_winner2 = Game(player_id=form.winner2.data, win=True, loss=False)
        new_game_loser1 = Game(player_id=form.loser1.data, win=False, loss=True)
        new_game_loser2 = Game(player_id=form.loser2.data, win=False, loss=True)
        db.session.add(new_game_winner1)
        db.session.add(new_game_winner2)
        db.session.add(new_game_loser1)
        db.session.add(new_game_loser2)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('record_game.html', form=form)

@app.route('/stats', methods=['GET'])
def stats():
    players = Player.query.all()
    stats = []
    for player in players:
        games = Game.query.filter_by(player_id=player.id).all()
        wins = [game for game in games if game.win]
        losses = [game for game in games if game.loss]
        flowers = Flower.query.filter_by(player_id=player.id).count()
        stats.append({
            'name': player.name,
            'games_played': len(games),
            'games_won': len(wins),
            'games_lost': len(losses),
            'flowers': flowers
        })
    return render_template('stats.html', stats=stats)

@app.route('/record_flower', methods=['GET', 'POST'])
def record_flower():
    form = FlowerForm()
    form.player.choices = [(player.id, player.name) for player in Player.query.all()]
    form.player.choices.insert(0, ('', 'Select player'))  # add default option
    if form.validate_on_submit():
        player_id = form.player.data
        if player_id:
            player = Player.query.get(int(player_id))
            new_flower = Flower(player_id=player.id)
            db.session.add(new_flower)
            db.session.commit()
            flash('Flower recorded!')
            return redirect(url_for('record_flower'))
    return render_template('record_flower.html', form=form)

@app.route('/rules_chatbot')
def rules_chatbot():
    return render_template('rules_chatbot.html', bot_workflow_id=bot_workflow_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

