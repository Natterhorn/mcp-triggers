# Dice Triggers - 8-Sided Dice Odds Calculator

A Python web application for calculating odds and probabilities of rolling 8-sided dice with faces: Hit (2x), Blank (2x), Shield, Wild, Skull, and Crit.

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

### Calculate Odds
1. Set the **Number of Dice** (1-20)
2. Enter how many of **each face** you want to find odds for
   - Example: 1 Hit + 2 Shield = find the probability of rolling at least 1 Hit AND at least 2 Shield
3. Click **Calculate Odds** to get the probability percentage
4. Use **Reset Form** to clear all inputs and start over

## How It Works

- The calculator uses Monte Carlo simulation (100,000 trials) to estimate accurate probabilities
- Results show the probability of rolling **at least** the target face combination
- Crit faces automatically trigger bonus die rolls (which cannot explode further)

## API Endpoints

- `POST /api/odds` - Calculate odds for a specific target face combination
  - Request: `{ num_dice: int, target_faces: { face: count, ... } }`
  - Response: `{ num_dice: int, target_faces: {...}, percentage: float }`

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

To modify the dice faces, edit the `FACES` tuple in [app/dice.py](app/dice.py#L11).

To change how odds are calculated, modify the `calculate_odds()` method in [app/dice.py](app/dice.py#L70).

## License

This project is provided as-is for educational and entertainment purposes.

