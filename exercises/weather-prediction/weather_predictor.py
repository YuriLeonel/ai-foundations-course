import numpy as np
import random

class WeatherPredictor:
    """
    A Markov Chain-based weather prediction system.

    States: Sunny, Cloudy, Rainy
    """

    def __init__(self):
        # Define weather states
        self.states = ['Sunny', 'Cloudy', 'Rainy']
        self.state_index = {state: i for i, state in enumerate(self.states)}

        # Transition matrix: P[i][j] = probability of transitioning from state i to state j
        # Rows: current state | Columns: next state
        self.transition_matrix = np.array([
            [0.7, 0.2, 0.1],  # From Sunny: 70% sunny, 20% cloudy, 10% rainy
            [0.3, 0.4, 0.3],  # From Cloudy: 30% sunny, 40% cloudy, 30% rainy
            [0.2, 0.3, 0.5]   # From Rainy: 20% sunny, 30% cloudy, 50% rainy
        ])

    def predict_next_day(self, current_state):
        """
        Predict the weather for the next day based on current state.

        Args:
            current_state (str): Current weather state

        Returns:
            str: Predicted next state
        """
        if current_state not in self.state_index:
            raise ValueError(f"Invalid state: {current_state}. Must be one of {self.states}")

        # Get current state index
        current_idx = self.state_index[current_state]

        # Get transition probabilities for current state
        probabilities = self.transition_matrix[current_idx]

        # Select next state based on probabilities
        next_idx = np.random.choice(len(self.states), p=probabilities)

        return self.states[next_idx]

    def predict_sequence(self, initial_state, days):
        """
        Predict a sequence of weather states for multiple days.

        Args:
            initial_state (str): Starting weather state
            days (int): Number of days to predict

        Returns:
            list: Sequence of predicted weather states
        """
        sequence = [initial_state]
        current_state = initial_state

        for _ in range(days - 1):
            next_state = self.predict_next_day(current_state)
            sequence.append(next_state)
            current_state = next_state

        return sequence

    def get_probability_distribution(self, current_state):
        """
        Get the probability distribution for the next day given current state.

        Args:
            current_state (str): Current weather state

        Returns:
            dict: Probability distribution for next day
        """
        if current_state not in self.state_index:
            raise ValueError(f"Invalid state: {current_state}")

        current_idx = self.state_index[current_state]
        probabilities = self.transition_matrix[current_idx]

        return {state: prob for state, prob in zip(self.states, probabilities)}

    def steady_state_distribution(self, iterations=100):
        """
        Calculate the steady-state (long-term) probability distribution.

        Args:
            iterations (int): Number of matrix multiplications

        Returns:
            dict: Steady-state probability distribution
        """
        # Start with uniform distribution
        distribution = np.array([1/3, 1/3, 1/3])

        # Multiply by transition matrix repeatedly
        for _ in range(iterations):
            distribution = distribution @ self.transition_matrix

        return {state: prob for state, prob in zip(self.states, distribution)}

    def display_transition_matrix(self):
        """Display the transition matrix in a readable format."""
        print("\n" + "="*60)
        print("STATE TRANSITION MATRIX")
        print("="*60)
        print(f"\n{'Current State':<15} | {'Sunny':<12} | {'Cloudy':<12} | {'Rainy':<12}")
        print("-" * 60)

        for i, state in enumerate(self.states):
            probs = self.transition_matrix[i]
            print(f"{state:<15} | {probs[0]:<12.1%} | {probs[1]:<12.1%} | {probs[2]:<12.1%}")
        print("="*60 + "\n")


# Demonstration and usage examples
def main():
    # Create weather predictor instance
    predictor = WeatherPredictor()

    # Display transition matrix
    predictor.display_transition_matrix()

    # Example 1: Single day prediction with probabilities
    print("EXAMPLE 1: Next day prediction")
    print("-" * 60)
    current = "Sunny"
    probs = predictor.get_probability_distribution(current)
    print(f"Current weather: {current}")
    print("Probabilities for tomorrow:")
    for state, prob in probs.items():
        print(f"  {state}: {prob:.1%}")

    # Example 2: Multiple day sequence prediction
    print("\n" + "="*60)
    print("EXAMPLE 2: 7-day forecast")
    print("-" * 60)
    initial = "Cloudy"
    days = 7
    sequence = predictor.predict_sequence(initial, days)

    print(f"Initial weather: {initial}")
    print(f"\nPredicted sequence for the next {days} days:")
    for day, weather in enumerate(sequence, 1):
        print(f"  Day {day}: {weather}")

    # Example 3: Long-term probability distribution
    print("\n" + "="*60)
    print("EXAMPLE 3: Long-term probability distribution")
    print("-" * 60)
    steady_state = predictor.steady_state_distribution()
    print("After many days, regardless of the initial state:")
    for state, prob in steady_state.items():
        print(f"  {state}: {prob:.2%}")

    # Example 4: Multiple simulations comparison
    print("\n" + "="*60)
    print("EXAMPLE 4: Multiple forecast simulations (30 days)")
    print("-" * 60)
    initial = "Sunny"
    simulations = 5

    for sim in range(simulations):
        sequence = predictor.predict_sequence(initial, 30)
        counts = {state: sequence.count(state) for state in predictor.states}
        print(f"\nSimulation {sim + 1}:")
        for state, count in counts.items():
            print(f"  {state}: {count} days ({count/30:.1%})")


if __name__ == "__main__":
    # Set random seed for reproducibility (optional)
    np.random.seed(42)
    random.seed(42)

    main()