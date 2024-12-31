"""
With this function you can access the messages needed for the main function.
The reason for this file to exist is due to multiple language support purposes
language: string - provided language
msg_id: string - gets the message type
def getMessage(language, msg_id)

more language probably planned in the future
"""


def getMessage(language: str, msg_id: str):
    # 0 = german, 1 = english
    # messages = {msg_id, [0, 1]}
    messages = {"check_file": ["Prüfe, ob die Datei existiert", "Check, if the file exists"],
                "file_exists": ["Datei existiert", "File exists"],
                "file_not_exists": ["Datei existiert nicht", "File does not exists"],
                "result_score1": ["Du hast", "You got"],  # Teil 1
                "result_score2": ["richtig", "correct"],  # Teil 2
                "result_accuracy": ["Genauigkeit im Test", "Accuracy in the vocabulary test"],
                "grade_name": ["Note", "Grade"],
                "list_vocab": ["Deine eingetragene Vokabeln werden nun aufgelistet",
                               "Your entered vocabularies will be listed now"],
                "learn_again": ["Willst du nochmal lernen? (ja/nein)\n => ", "Do you want to learn again? (yes/no)\n => "],
                "any_key": ["Gebe 'shift' ein, wenn du fertig bist mit dem Lernen",
                            "Press 'shift' if you are finished with your learning"],
                "mode_select": ["Wähle ein Modus aus (chronologisch/zufall)\n => ",
                                "Choose the test mode (chronological/random)\n => "],
                "invalid_mode": ["Ungültiger Modus", "invalid mode"],
                "correct_vocab": ["██████████ Richtig [+] ██████████", "██████████ Correct [+] ██████████"],
                "wrong_vocab": ["██████████ Falsch [-] ██████████", "██████████ Incorrect [-] ██████████"],
                "asked_vocab": ["Abgefragt:", "Asked:"],
                "answered_vocab": ["Deine Antwort:", "Your answer:"],
                "corrected_answer_vocab": ["Richtige Antwort:", "Correct answer:"]}

    if language == "german":
        setlang = 0

    elif language == "english":
        setlang = 1

    else:
        setlang = 0

    if msg_id not in messages:
        return "missing message error: " + msg_id

    return messages[msg_id][setlang]

# example: print(getMessage("german", "file_exists"))

# idea
# german, file exists
# -> types[german][file_exists]
# -> {"german": {"file_exists": "Datei existiert", "file_not_exists": "Datei existiert nicht"},
# "english": {"file_exists": "File exists", "file_not_exists": "File does not exists"}}
