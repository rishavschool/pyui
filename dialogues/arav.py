from colors import TerminalColors

arav_dialogue = {
  "dialogue": f"Yo boul got some {TerminalColors.MAGENTA}polyester{TerminalColors.RESET} for me?",
  "audio": "gotsomepolyester.mp3",
  "responses": {
    "Nah, sorry Arav.": {
      "dialogue": "Alright bro sybau.",
      "audio": "alrightbrosybau.mp3",
      "responses": "END1"
    },
    f"Yeah, I got 3 {TerminalColors.MAGENTA}polyester{TerminalColors.RESET} scraps": {
      "dialogue": "Thanks young boul.",
      "responses": "END2",
      "audio": "thanksyoungboul.mp3",
      "condition": "user.inventory['polyester scraps'] >= 3"
    }
  }
}