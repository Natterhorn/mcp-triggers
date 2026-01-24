"""
Routes for the dice roller web app
"""
from flask import Blueprint, render_template, request, jsonify
from .dice import OddsCalculator, DiceFace

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Main page"""
    return render_template('index.html', unique_faces=DiceFace.UNIQUE_FACES)


@main_bp.route('/api/odds', methods=['POST'])
def calculate_odds():
    """API endpoint to calculate odds for any combination of target faces"""
    data = request.json
    num_dice = int(data.get('num_dice', 1))
    num_dice = max(1, min(num_dice, 20))
    
    target_faces = data.get('target_faces', {})
    
    # Validate target faces
    if not target_faces:
        return jsonify({'error': 'Select at least one face'}), 400
    
    for face in target_faces.keys():
        if face not in DiceFace.UNIQUE_FACES:
            return jsonify({'error': f'Invalid face: {face}'}), 400
    
    calculator = OddsCalculator(num_dice)
    
    # Calculate odds for at least the target faces
    try:
        percentage = calculator.calculate_odds(target_faces)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({
        'num_dice': num_dice,
        'target_faces': target_faces,
        'percentage': round(percentage, 4)
    })

