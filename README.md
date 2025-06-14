# Truco Game Management System 🃏

A comprehensive web application for managing and tracking Truco games, built with Flask and PostgreSQL. This system allows players to record games, track statistics, and get help with game rules through an AI-powered chatbot.

## About Truco

Truco is a popular South American card game, typically played in teams of two. This application helps groups of friends or clubs track their games, maintain player statistics, and resolve rule disputes through an intelligent chatbot.

## 🚀 Key Features

### Game Management
- **Player Registration**: Add and manage players in the system
- **Game Recording**: Record team-based games (2v2 format) with winners and losers
- **Game History**: Automatic timestamping and storage of all game records

### Statistics & Analytics
- **Player Statistics**: Comprehensive stats showing:
  - Total games played
  - Games won and lost
  - Win/loss ratio
  - "Flor" penalties tracked
- **Leaderboard**: Sortable player rankings and performance metrics

### Special Features
- **Flor Tracking**: Record "Flor Quemada" (burned flower) penalties
- **Rules Chatbot**: AI-powered assistant that answers Truco rules questions in Spanish
- **Responsive Design**: Mobile-friendly interface with Bootstrap styling

### User Experience
- **Clean Interface**: Modern, intuitive web interface
- **Data Tables**: Interactive, sortable player lists
- **Flash Messages**: User feedback for successful operations
- **Multi-language Support**: Spanish language interface

## 🛠 Technical Stack

- **Backend**: Flask (Python web framework)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 4, jQuery
- **Forms**: Flask-WTF with WTForms validation
- **AI Integration**: External chatbot API (tryneum.com)
- **Deployment**: Docker, Fly.io, Heroku-compatible

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd truco-public
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env with your actual values
   nano .env  # or use your preferred editor
   ```
   
   Required environment variables:
   - `SECRET_KEY`: Flask secret key for session security
   - `BOT_WORKFLOW_ID`: Chatbot workflow ID for tryneum.com integration
   - `DATABASE_URL`: Full PostgreSQL connection string, OR individual DB settings:
     - `DB_USER`: Database username
     - `DB_PASSWORD`: Database password
     - `DB_ENDPOINT`: Database host
     - `DB_PORT`: Database port (default: 5432)
     - `DB_NAME`: Database name

5. **Run the application**
   ```bash
   python server.py
   ```

The application will be available at `http://localhost:8080`

## 🗄 Database Schema

### Players
- `id`: Primary key
- `name`: Unique player name

### Games
- `id`: Primary key
- `date`: Game timestamp
- `player_id`: Foreign key to player
- `win`: Boolean (True if player won)
- `loss`: Boolean (True if player lost)

### Flowers
- `id`: Primary key
- `date`: Timestamp
- `player_id`: Foreign key to player

## 🚀 Deployment

### Docker
```bash
docker build -t truco-app .
docker run -p 8080:8080 truco-app
```

### Fly.io
```bash
fly deploy
```

### Heroku
The application is Heroku-ready with the included `Procfile`.

## 📱 Usage

1. **Add Players**: Start by adding players to your group
2. **Record Games**: After each game, record the winners and losers
3. **View Statistics**: Check the stats page to see player performance
4. **Record Penalties**: Track "Flor Quemada" incidents
5. **Ask Questions**: Use the chatbot for rule clarifications

## 🎯 API Endpoints

- `GET /` - Home page with player list
- `GET/POST /add_player` - Add new player
- `GET/POST /record_game` - Record game results
- `GET /stats` - View player statistics
- `GET/POST /record_flower` - Record flor penalties
- `GET /rules_chatbot` - Access rules chatbot

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔒 Security Features

This application implements several security best practices:
- **Environment Variables**: All sensitive data (database credentials, secret keys) are stored in environment variables
- **No Hardcoded Secrets**: No sensitive information is committed to version control
- **Secure Configuration**: Production-ready configuration with proper secret management

### Production Deployment Security Checklist:
- ✅ Use strong, unique `SECRET_KEY`
- ✅ Use secure database credentials
- ✅ Enable HTTPS (handled by Fly.io)
- ✅ Set `FLASK_ENV=production`
- ✅ Use environment variables for all sensitive data
- ✅ Review and update `.gitignore` to exclude sensitive files

## 🎮 Game Rules Support

The integrated chatbot can help with Truco rules and questions. Ask questions in Spanish for best results, such as:
- "¿Cuántos puntos vale una flor?"
- "¿Qué es el envido?"
- "¿Cómo se juega el truco?"

---

Built with ❤️ for the Truco community 