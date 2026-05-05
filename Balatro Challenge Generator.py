import random

# Standard decks (excluding pure challenge decks)
decks = [
    "Red Deck (+1 Discard)", "Blue Deck (+1 Hand)", "Yellow Deck (+$10 start)",
    "Green Deck (+$ per unused Hand/Discard, no interest)", "Black Deck (-1 Discard, +1 Joker slot)",
    "Magic Deck (Start with 2 Tarot cards)", "Nebula Deck (Start with 2 Planet cards, -1 Consumable slot)",
    "Ghost Deck (Start with a Spectral card)", "Abandoned Deck (No face cards)",
    "Checkered Deck (All Hearts & Spades)", "Zodiac Deck",
    "Painted Deck (Hand size +2, Joker slots -1)", "Anaglyph Deck (Double tag awarded after defeating Boss Blind)",
    "Plasma Deck (Chips & Mult averaged)", "Erratic Deck (Random ranks and suits)"
]

# Stakes with accurate descriptions
stakes = [
    ("White", "Base difficulty"),
    ("Red", "Small Blind gives no reward money"),
    ("Green", "Required score scales faster"),
    ("Black", "Jokers can appear with Eternal sticker"),
    ("Blue", "-1 Discard"),
    ("Purple", "Required score scales even faster"),
    ("Orange", "Jokers can appear with Perishable sticker"),
    ("Gold", "Jokers can appear with Rental sticker ($3 per round)")
]

# Interesting side goals / mini-challenges
side_goals = [
    "Breaking at least 2 Glass cards during the run",
    "Triggering 8 Ball at least 3 times",
    "Playing at least 2 Flush Fives by ante 8",
    "Scoring a hand worth over 500,000 chips/mult by Ante 4",
    "Never buying a Joker that costs more than $8",
    "Destroying or selling at least 10 Jokers by Ante 8",
    "Winning at least 3 Boss Blinds using only one hand type",
    "Having 5 or more Eternal Jokers at the same time",
    "Making $100+ in a single round",
    "Triggering a Polychrome card at least 2 times in one hand",
    "Clearing Ante 8 without ever playing a Face card",
    "Getting a Negative Joker and keeping it until the end",
    "Playing at least 20 Stone cards across the run",
    "Having 3+ Glass cards in your deck at once without breaking any until Ante 6",
    "Triggering the same Joker effect 3 times in a single hand",
    "Reaching Ante 8 with no consumables left in your inventory",
    "Building a deck with only one suit by Ante 6",
    "Scoring using only Bonus and Mult cards (Jokerless style)",
    "Having a single card score over 100 Mult on its own",
    "Having at least 15 Steel cards in deck by Ante 8",
    "Triggering a retrigger Joker (Hanging Chad, Photograph, etc.) at least 4 times in one hand",
    "Having 4 or more Mult cards active at the same time",
    "Winning a round with a High Card hand after Ante 5",
    "Using The Fool, The Magician, or The Empress Tarot at least 6 times total",
    "Collecting at least 3 different Planet cards",
    "Never skipping a Blind after Ante 3",
    "Selling at least 5 Jokers that have a sticker",
    "Triggering the Steel Card X1.5 Mult at least 8 times in a single hand",
    "Playing only hands that contain at least one enhanced card",
    "Reaching Ante 8 without ever buying a Voucher",
    "Having at least 2 Legendary Jokers at the same time",
    "Scoring a Flush House or Flush Five using only one suit"
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

if __name__ == "__main__":
    random.seed()   # fresh randomness
    generate_challenge()
    
    print("\nRun the script again for a new challenge!")
