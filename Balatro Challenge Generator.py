import random

# Standard decks (excluding pure challenge decks)
decks = [
    "Red Deck (+1 Discard)", "Blue Deck (+1 Hand)", "Yellow Deck (+$10 start)",
    "Green Deck (+$ per unused Hand/Discard, no interest)", "Black Deck (-1 Discard, +1 Joker slot)",
    "Magic Deck (Start with 2 Tarot cards)", "Nebula Deck (Start with 2 Planet cards, -1 Consume slot)",
    "Ghost Deck (Start with a Spectral card)", "Abandoned Deck (No face cards)",
    "Checkered Deck (All Hearts & Spades)", "Zodiac Deck (Unlocks based on stakes)",
    "Painted Deck (Hand size +2, Joker slots -1)", "Anaglyph Deck (Double tags on skips)",
    "Plasma Deck (Chips & Mult averaged)", "Erratic Deck (Random ranks and suits)"
]

# Stake colors and names (cumulative difficulty)
stakes = [
    ("White", "Base difficulty"),
    ("Red", "Small Blind gives no money"),
    ("Green", "Score requirement scales faster"),
    ("Black", "Eternal Jokers can appear in shop"),
    ("Blue", "-1 Discard"),
    ("Purple", "Score scales even faster"),
    ("Orange", "Perishable Jokers appear"),
    ("Gold", "All previous + need to reach Ante 8 with $0 at end or similar high difficulty")
]

# Interesting side goals / mini-challenges (inspired by game mechanics and official challenges)
side_goals = [
    "Break at least 2 Glass cards during the run",
    "Trigger the 8 Ball Joker at least 3 times",
    "Play at least 5 Flush Fives",
    "Score a hand worth over 1,000,000 chips/mult by Ante 4",
    "Never buy a Joker that costs more than $8",
    "Destroy or sell at least 10 Jokers by Ante 8",
    "Win at least 3 Boss Blinds using only one hand type (e.g. only Straights)",
    "Have 5 or more Eternal Jokers at the same time",
    "Make $100+ from Interest in a single round",
    "Trigger a Polychrome card at least 8 times in one hand",
    "Clear Ante 8 without ever playing a Face card",
    "Get a Negative Joker and keep it until the end",
    "Play at least 20 Stone cards across the run",
    "Have 3+ Glass cards in your deck at once and don't let any break until Ante 6",
    "Win a round with exactly 69 chips (nice)",
    "Trigger the same Joker effect 10 times in a single hand",
    "Reach Ante 8 with no consumables left in your deck",
    "Build a deck with only one suit by Ante 5",
    "Score using only Bonus and Mult cards (no base chips from poker hands)",
    "Have a single card score over 100 Mult on its own"
]

def generate_challenge():
    deck = random.choice(decks)
    stake_color, stake_desc = random.choice(stakes)
    goal = random.choice(side_goals)
    
    print("🎲 Your Random Balatro Challenge 🎲\n")
    print(f"Deck:     {deck}")
    print(f"Stake:    {stake_color} Stake — {stake_desc}")
    print(f"Goal:     Reach Ante 8 while also {goal}\n")
    print("Good luck, Joker! 🃏")

# Generate one challenge
if __name__ == "__main__":
    random.seed()  # for fresh randomness
    generate_challenge()
    
    # Optional: generate multiple at once
    print("\nWant more? Run the script again or uncomment below:")
    # for _ in range(5):
    #     print("-" * 40)
    #     generate_challenge()
