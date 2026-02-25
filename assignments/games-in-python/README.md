
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python to practice string manipulation, loops, conditionals, and handling user input.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Create a console-based Hangman game that randomly selects a secret word from a predefined list and lets a single player guess letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Accept single-letter guesses and reveal correct letters in a `_ _ _` style display
- Track and display the number of incorrect guesses remaining
- Prevent repeated processing of the same guessed letter
- End when the word is fully guessed or attempts are exhausted
- Display appropriate win/lose messages
- Organize code into functions (for example: `choose_word()`, `display_progress()`, `process_guess()`)

#### Example
```
Secret word: _ _ _ _ _
Guess: a
Progress: _ a _ _ _
Incorrect guesses left: 5
```

