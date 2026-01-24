# Dice Triggers - 8-Sided Dice Roller & Odds Calculator

A Python web application for simulating rolls of 8-sided dice with faces: Hit (2x), Blank (2x), Shield, Wild, Skull, and Crit. Calculate odds and probabilities for specific face combinations.

## Features

- **Dice Roller**: Roll 1-20 dice and see the results
- **Odds Calculator**: Calculate exact odds for specific face combinations
- **Face Statistics**: Get probability of rolling a specific face at least once
- **Monte Carlo Simulation**: Run simulations to analyze outcome distributions
- **Interactive Web UI**: Beautiful, responsive interface built with Flask and vanilla JavaScript

## Die Specification

Each 8-sided die has the following faces:
- **Hit** (2 faces)
- **Blank** (2 faces)
- **Shield** (1 face)
- **Wild** (1 face)
- **Skull** (1 face)
- **Crit** (1 face)

## Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or navigate to the project directory:
```bash
cd c:\Users\captc\source\dice-triggers
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python run.py
```

The application will start on `http://127.0.0.1:5000`

Open your browser and navigate to `http://localhost:5000` to use the app.

## Usage

### Roll Dice
- Specify the number of dice (1-20)
- Click "Roll Dice" to simulate the roll
- See individual results and face counts

### Calculate Odds
- Specify the number of dice
- Select the target combination of faces
- Get exact probability percentage and odds ratio

### Face Statistics
- Specify the number of dice
- Select a specific face (Hit, Blank, Shield, Wild, Skull, Crit)
- Get the probability of rolling at least one of that face

### Monte Carlo Simulation
- Specify the number of dice
- Choose the number of simulation runs (1-10000)
- View the top 10 most common outcomes and their frequencies

## API Endpoints

- `POST /api/roll` - Roll dice
- `POST /api/odds` - Calculate odds for specific combinations
- `POST /api/face-stats` - Get statistics for a specific face
- `POST /api/simulate` - Run Monte Carlo simulation

## Project Structure

```
dice-triggers/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── dice.py              # Dice simulation and odds calculation
│   ├── routes.py            # API routes
│   ├── templates/
│   │   └── index.html       # Main web interface
│   └── static/              # Static files (CSS, JS)
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Development

To modify the dice faces, edit the `FACES` tuple in [app/dice.py](app/dice.py#L9).

To add new API endpoints, edit [app/routes.py](app/routes.py).

## License

This project is provided as-is for educational and entertainment purposes.
