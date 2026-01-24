"""
Dice simulation and odds calculation module
"""
import random
from collections import Counter


class DiceFace:
    """Represents the faces of an 8-sided die"""
    FACES = ["Hit", "Hit", "Blank", "Blank", "Shield", "Wild", "Skull", "Crit"]
    UNIQUE_FACES = ["Hit", "Crit", "Wild", "Shield", "Skull", "Blank"]


class DiceRoller:
    """Simulates rolling multiple 8-sided dice"""
    
    def __init__(self, num_dice=1):
        """Initialize with number of dice to roll"""
        self.num_dice = max(1, min(num_dice, 20))  # Limit 1-20 dice
        
    def roll(self, allow_crit_explosion=True):
        """
        Roll the dice and return results.
        If a Crit is rolled and allow_crit_explosion is True, roll an additional die.
        The additional die will not cause further explosions.
        """
        results = [random.choice(DiceFace.FACES) for _ in range(self.num_dice)]
        
        # Check for Crit faces and roll bonus dice (but don't let them explode)
        if allow_crit_explosion:
            crit_count = results.count("Crit")
            for _ in range(crit_count):
                bonus_die = random.choice(DiceFace.FACES)
                results.append(bonus_die)
        
        return results
    
    def roll_multiple(self, times=1000):
        """Roll dice multiple times and return all results"""
        return [self.roll() for _ in range(times)]


class OddsCalculator:
    """Calculate odds of specific face combinations"""
    
    def __init__(self, num_dice=1):
        """Initialize calculator for specific number of dice"""
        self.num_dice = num_dice
        self.total_outcomes = 8 ** num_dice
    
    def count_face_occurrences(self, outcome):
        """Count occurrences of each face in an outcome"""
        return dict(Counter(outcome))
    
    def calculate_odds(self, target_faces):
        """
        Calculate odds of getting at least the target faces
        target_faces: list like ['Hit', 'Shield'] or dict like {'Hit': 2, 'Shield': 1}
        Returns: percentage of outcomes that contain at least these faces
        """
        # Convert list to dict with count of 1 for each face
        if isinstance(target_faces, list):
            target_dict = {face: 1 for face in target_faces}
        else:
            target_dict = target_faces
        
        matching_outcomes = 0
        total_test_outcomes = 0
        
        # Use Monte Carlo simulation to estimate odds
        num_simulations = 100000
        for _ in range(num_simulations):
            roller = DiceRoller(self.num_dice)
            result = roller.roll()
            result_counts = self.count_face_occurrences(result)
            
            # Check if result contains at least the target faces
            has_all_targets = True
            for face, required_count in target_dict.items():
                if result_counts.get(face, 0) < required_count:
                    has_all_targets = False
                    break
            
            if has_all_targets:
                matching_outcomes += 1
            
            total_test_outcomes += 1
        
        # Calculate percentage from simulation
        percentage = (matching_outcomes / total_test_outcomes) * 100 if total_test_outcomes > 0 else 0
        
        return percentage