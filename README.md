# VocabularyTrainer
In 2021, I started to code a "French vocabulary" trainer to help my friends and myself learn vocabularies more 
efficient and in a more fun way. It started as a small input program with only if, else and else if statements. 
Over the time I started to improve the program until it can take vocabularies from websites so my friends don't need to 
install new versions of the new vocabularies while I can change them for my friends via requests library. 
One of my first version "VocabularyQuery" is uploaded here on GitHub and you can see that it's not really usable in a fun way
because you always have to run the program to get one vocabulary.


With this program I want to make everyone access their own vocabulary trainer with the possibility to enter your own vocabularies 

VocabularyTrainer is a just for fun CLI (command line interface) project, where you can learn vocabularies with your own vocabularies, learn and make a test to get your own grade.

The current grading system used in this program is the german grading system from 1-6

## Why using VocabularyTrainer?
With VocabularyTrainer you can reflect your own mistakes and take a look on your own learning progress by analyzing your own grade and your difficulties in some vocabularies.

You also get to choose between chronological test or randomized test. 

Additionally, you can also invert the vocabularies, so you get a better understanding for the language you are currently learning
instead of asking you the language you are currently learning.

## Supported languages
For now, this program supports the german and english language

## Setup
1. Install the program
    - recommended: put the program in an extra folder
2. Start the program and let the program generate some files (`vocabulary.txt` and `settings.txt`)
3. Add your own vocabularies in `vocabulary.txt` like in the following example:
```
word1
translation1

word2
translation2

word3
translation3
```
You can add as many as you want. What you need to remember is to make a space between the words if you want to add a new word
4. Start the program again and learn with the vocabularies


## Test modes
chronological: Queries vocabulary in order
random: Queries vocabulary in mixed order


## You noticed some bugs?
Then write a [new issue](https://github.com/DramaLvl1/VocabularyTrainer/issues) on Github for me to fix it. Remember to describe the issue as precise as possible for me to replicate the bug and to help at your problem.
Every bug reports help the program to run better :)

## Suggestions?
You want to suggest something new like a new grading system?

Then you can also write a [new issue](https://github.com/DramaLvl1/VocabularyTrainer/issues) on GitHub so I can see if 
your suggestion is improving the program :)

If you are suggesting a new grading system, it would be helpful if you describe your grading system as good as possible for me to add into the program


## Todo/planned
- mixed mode: sometimes asks inverted vocabularies 
