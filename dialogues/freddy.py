from colors import TerminalColors

freddy_dialogue = {
  "dialogue": f"Hail, how art thou on this fair day?",
  "audio": "howartthou.mp3",
  "responses": {
    "What are you saying??": {
      "audio": "thickofwit.mp3",
      "dialogue": "Thou art thick of wit, art thou not? What I speak is plainly lost on thee, fool.",
      "responses": "END1"
    },
    "I do well, lad": {
      "audio": "purchasesomegarments.mp3",
      "dialogue": f"Excellent! Wouldst thou like to purchase some {TerminalColors.CYAN}garments{TerminalColors.RESET}?",
      "responses": {
        "Ay": {
          "audio": "hastaste.mp3",
          "dialogue": "Aye, good choice! Thou hast taste, I see. Come, let us make the bargain swift!",
          "responses": "END2"
        },
        "Nay": {
          "audio": "awaywithtee.mp3",
          "dialogue": "Get thee gone, then! Away with thee, thou scoundrel!",
          "responses": "END1"
        }
      }
    }
  }
}

freddy_happy_dialogue = {
  "audio": "wisechoicegoodsir.mp3",
  "dialogue": "A wise choice, good sir.",
  "responses": "END1"
}

freddy_mad_dialogue = {
  "audio": "ruffian.mp3",
  "dialogue": "Begone thou ruffian!",
  "responses": "END1"
}