import random
import os
import time
import Translator
import keyboard


version = "1.0.0"

def main():
    generate_file()
    send_voclist()
    # abfrage folgt
    inp = input(Translator.getMessage(getLanguage(), "learn_again")).lower()  # ID learn_again
    if inp == "ja" or inp == "yes":
        main()


# first the functions
def generate_file():
    if not os.path.exists("vocabulary.txt"):
        print(Translator.getMessage(getLanguage(), "check_file"))
        time.sleep(1)
        print(Translator.getMessage(getLanguage(), "file_not_exists"))
        vocfile = open("vocabulary.txt", "w")
        vocfile.writelines("example\n"
                           "Beispiel\n"
                           "\n"
                           "example2"
                           "Beispiel2"
                           "\n"
                           "spain\n"
                           "Spanisch")
        vocfile.close()

    else:
        print(Translator.getMessage(getLanguage(), "file_exists"))
        time.sleep(1)  # to let the user realize, what is happening in this program

    if not os.path.exists("settings.txt"):
        settings_file = open("settings.txt", "w")
        settings_file.writelines(["# Info: do not change the settings if you don't know, what you are doing with that\n",
                         "# available languages: german, english\n",
                         "setting_version: 1.0.0\n",
                         "language: german"])
        settings_file.close()

    elif checkSettingVersion() != version:  # if settings exists but wrong setting version
        settings_file = open("settings.txt", "w")
        settings_file.writelines(["# Info: do not change the settings if you don't know, what you are doing with that\n",
                                  "# available languages: german, english\n",
                                  "setting_version: 2.0.0\n",
                                  "language: german"])
        settings_file.close()


def checkSettingVersion():
    with open("settings.txt", "r") as settings:
        return settings.readlines()[len(settings.readlines()) - 2].split(":")[1].replace(" ", "").replace("\n", "")


def getLanguage():
    with open("settings.txt", "r") as settings:
        settings = settings.readlines()
        language_line = settings[len(settings) - 1].split(":")[1]

        return language_line.replace(" ", "")


# Calculate the grade out of your correct answers and the amount of the existing vocabularies
def calculate_grade(r, vx):  # add different grading system later
    accuracy = round(r / vx * 100, 2)
    text = Translator.getMessage(getLanguage(), "result_score1") + f" {r}/{vx} " + Translator.getMessage(getLanguage(), "result_score2") + "\n"

    text += Translator.getMessage(getLanguage(), "result_accuracy") + f": {accuracy}%\n"
    noten = [
        (95, Translator.getMessage(getLanguage(), "grade_name") + " 1+"),
        (90, Translator.getMessage(getLanguage(), "grade_name") + " 1"),
        (85, Translator.getMessage(getLanguage(), "grade_name") + " 1-"),
        (80, Translator.getMessage(getLanguage(), "grade_name") + " 2+"),
        (75, Translator.getMessage(getLanguage(), "grade_name") + " 2"),
        (70, Translator.getMessage(getLanguage(), "grade_name") + " 2-"),
        (65, Translator.getMessage(getLanguage(), "grade_name") + " 3+"),
        (60, Translator.getMessage(getLanguage(), "grade_name") + " 3"),
        (55, Translator.getMessage(getLanguage(), "grade_name") + " 3-"),
        (50, Translator.getMessage(getLanguage(), "grade_name") + " 4+"),
        (45, Translator.getMessage(getLanguage(), "grade_name") + " 4"),
        (40, Translator.getMessage(getLanguage(), "grade_name") + " 4-"),
        (33, Translator.getMessage(getLanguage(), "grade_name") + " 5+"),
        (27, Translator.getMessage(getLanguage(), "grade_name") + " 5"),
        (20, Translator.getMessage(getLanguage(), "grade_name") + " 5-"),
        (0, Translator.getMessage(getLanguage(), "grade_name") + " 6")
    ]

    for grenze, note in noten:
        if accuracy >= grenze:
            text += note + "\n"
            break

    return text


# get the amount of lines in the file
def lines():
    return len(voc)


file = open("vocabulary.txt", "r")
voc = file.readlines()


def voc_amount():
    if lines() % 3 == 2:
        return (lines() // 3) + 1


def send_voclist():
    # Send voc list
    num = 0  # amount voc
    index = 0  # list index
    print(Translator.getMessage(getLanguage(), "list_vocab"))  # ID list_vocab
    time.sleep(1)
    while num != voc_amount():
        if voc[index] and voc[index + 1] != "\n":
            num += 1
            print(str(num) + ". " + str(voc[index].replace("\n", "")) + " - " + str(voc[index + 1].replace("\n", "")))
            index += 3

    print("======================")
    print(Translator.getMessage(getLanguage(), "any_key"))  # ID any_key
    # detect space button
    while True:
        if keyboard.is_pressed('shift'):
            os.system("cls")
            break

    valid_mode = ["chronologisch", "chronological", "zufall", "random"]
    mode = input(Translator.getMessage(getLanguage(), "mode_select"))  # ID mode_select
    if mode not in valid_mode:
        print(Translator.getMessage(getLanguage(), "invalid_mode"))  # ID Invalid_mode
        mode = input(Translator.getMessage(getLanguage(), "mode_select"))  # ID mode_select
        while mode not in valid_mode:
            print(Translator.getMessage(getLanguage(), "invalid_mode"))  # ID Invalid_mode
            mode = input(Translator.getMessage(getLanguage(), "mode_select"))  # ID mode_select

    perform_test(mode)


# for formatting reasons
def add_space(message):
    output = ""
    addspace = 0
    for i in message:
        if i != "█":
            addspace += 1
        else:
            break
    i = 0
    while i < addspace:
        output += " "
        i += 1

    return output


def check_result(answers: list | dict, v_amount: int, mode: str):
    msg = ""
    amount = 1
    voc_index = 0
    if mode == "chronological":  # answers: list
        while amount <= v_amount:
            if answers[amount - 1].lower() == voc[voc_index + 1].lower().replace("\n", ""):   # formatting correct
                base_correct = f"{amount}.  " + Translator.getMessage(getLanguage(), "correct_vocab") + "\n"  # ID correct_vocab
                msg += (base_correct +
                        f"{add_space(base_correct)}" + Translator.getMessage(getLanguage(), "asked_vocab") + " " + voc[voc_index].replace("\n", "") + "\n"  # ID asked_vocab
                        f"{add_space(base_correct)}" + Translator.getMessage(getLanguage(), "answered_vocab") + f" {answers[amount - 1]}\n\n")   # ID your_answer

            else:
                base_wrong = f"{amount}.  " + Translator.getMessage(getLanguage(), "wrong_vocab") + "\n"  # ID wrong_vocab
                msg += (base_wrong +
                        f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "asked_vocab") + " " + voc[voc_index].replace("\n", "") + "\n"
                        f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "answered_vocab") + f" {answers[amount - 1]}\n"
                        f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "corrected_answer_vocab") + " " + voc[voc_index + 1].replace("\n", "") + "\n\n")

            amount += 1
            voc_index += 3

    if mode == "random":  # answers: dict
        while amount <= v_amount:
            # {"voc": "my answer"}
            # {"voc": ["my answer", "correct_voc"]}
            # answers: dict
            # v_amount: int
            # mode: str
            for v in voc:
                print(v)
                if v.replace("\n", "") not in answers:
                    continue

                if answers[v.replace("\n", "")] is None:
                    continue

                v = v.replace("\n", "")
                if len(answers[v.replace("\n", "")]) != 2:
                    base_correct = f"{amount}.  " + Translator.getMessage(getLanguage(), "correct_vocab") + "\n"  # ID correct_vocab
                    msg += (base_correct +
                            f"{add_space(base_correct)}" + Translator.getMessage(getLanguage(), "asked_vocab") + " " + v + "\n"  # ID asked
                            f"{add_space(base_correct)}" + Translator.getMessage(getLanguage(), "answered_vocab") + f" {answers[v]}\n\n")  # ID your_answer

                else:
                    base_wrong = f"{amount}.  " + Translator.getMessage(getLanguage(), "wrong_vocab") + "\n"  # ID wrong_vocab
                    msg += (base_wrong +
                            f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "asked_vocab") + " " + v + "\n"
                            f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "answered_vocab") + f" {answers[v][0]}\n"
                            f"{add_space(base_wrong)}" + Translator.getMessage(getLanguage(), "corrected_answer_vocab") + " " + answers[v][1].replace("\n", "") + "\n\n")

                amount += 1

    return msg


# no Translate.getMessage needed here
def perform_test(mode):
    vocs = 0
    correct = 0
    index = 0

    if mode == "chronologisch" or mode == "chronological":
        answer_list = []
        while vocs < voc_amount():
            if voc[index] and voc[index + 1] != "\n":
                ask = input(voc[index].replace("\n", "") + "\n => ")
                vocs += 1
                if ask.lower() == voc[index + 1].replace("\n", "").lower():
                    correct += 1
                    index += 3
                    answer_list.append(ask)
                    print(vocs)
                else:
                    index += 3
                    answer_list.append(ask)
                    print(vocs)
                    continue

        print(check_result(answer_list, voc_amount(), "chronological"))

    answer_history = {}
    if mode == "zufall" or mode == "random":
        voclist = []

        # copy from old version: FranzBotV3
        for i in range(lines()):
            if i % 3 == 0:
                voclist.append(i)

        while vocs < voc_amount():
            vocs += 1
            randomize = random.randint(0, len(voclist) - 1)
            ask = input(voc[voclist[randomize]].replace("\n", "") + "\n => ")  # [voc1, voc2, voc3, voc4]
            if ask.lower() == voc[voclist[randomize] + 1].lower().replace("\n", ""):  # if ask == voc.answer
                correct += 1
                index += 3
                answer_history[voc[voclist[randomize]].replace("\n", "")] = ask  # {"voc": "my answer"}
            else:
                index += 3
                answer_history[voc[voclist[randomize]].replace("\n", "")] = [ask, voc[voclist[randomize] + 1].replace("\n", "")]  # {"voc": ["my answer", "correct_voc"]}

            voclist.remove(voclist[randomize])

        print(check_result(answer_history, voc_amount(), "random"))
    print(calculate_grade(correct, voc_amount()))


main()
