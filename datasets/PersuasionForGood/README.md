# Persuasion for Good 
A large metadata-rich collection of online conversations between two people where one participant ("persuader") is trying to convince the other ("persuadee") to donate to a charity. This dataset contains 1017 dialogues, each with several conversational turns. Additionally, every user has a personality vector associated with them generated through psycological surveys.

Distributed together with:
"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good" https://arxiv.org/pdf/1906.06725.pdf. Xuewei Wang et al. ACL 2019.

## Dataset details
Original data: https://gitlab.com/ucdavisnlp/persuasionforgood/tree/master/data

## User-level information
Users in this dataset are Amazon Turks. For each user, the authors provide a 23-dimension characteristic vector based on a pre-task psychological survey. Each of these personality characteristics take on a value from 1 to 6; in addition, demographic info such as age, sex, race, education, marital status, employment, income, religion, and ideology are also included as user-level metadata: 

| Type      |  Type        | Data Type  | Range of Possible Values | Other Notes | 
| ------------- |:-------------:| :-----:| :----------------------:|  :------------:| 
| extrovert.x   | Personality | Numerical | {1, 6} |
| agreeable.x  | Personality  |   Numerical | {1, 6} |
| conscientious.x | Personality  |    Numerical | {1, 6} |
| neurotic.x   | Personality | Numerical | {1, 6} |
| open.x   | Personality  |   Numerical | {1, 6} |
| care.x | Personality  |    Numerical | {1, 6} |
| fairness.x   | Personality | Numerical | {1, 6} |
| loyalty.x   | Personality  |   Numerical | {1, 6} |
| conscientious.x | Personality  |    Numerical | {1, 6} |
| authority.x  | Personality | Numerical | {1, 6} |
| purity.x   | Personality  |   Nuerical | {1, 6} |
| freedom.x | Personality  |    Numerical | {1, 6} |
| conform.x | Personality  |    Numerical | {1, 6} |
| tradition.x   | Personality | Numerical | {1, 6} |
| benevolence.x  | Personality  |   Numerical | {1, 6} |
| universalism.x   | Personality | Numerical | {1, 6} |
| self_direction.x  | Personality  | Numerical | {1, 6} |
| stimulation.x  | Personality | Numerical | {1, 6} |
| hedonism.x | Personality  |   Numerical | {1, 6} |
| achievement.x   | Personality | Numerical | {1, 6} |
| power.x  | Personality  |   Numerical | {1, 6} |
| security.x  | Personality | Numerical | {1, 6} |
| rational.x  | Personality  |   Numerical | {1, 6} |
| intuitive.x   | Personality | Numerical | {1, 6} |
| age.x | Demographic |   Numerical | {3, 82} | The age 3 is probably a typo. |
| sex.x   | Demographic | Categorical | {Male, Female, Other}| 
| race.x   | Demographic  |   Categorical | {White, Other} |
| edu.x   | Demographic | Categorical | {Four year college, Less than four-year college, Postgraduate} |
| marital.x  | Demographic |  Categorical | {Married, Unmarried} |
| employment.x  | Demographic |   Categorical | {Employed for wages, Other} |
| income.x  | Demographic | Numerical | {1, 12} | 
| religion.x  | Demographic  |   Categorical | { Atheist, Catholic, Other religion, Protestant} |
| ideology.x | Demographic  |   Categorical | {Conservative, Liberal, Moderate} |


Additionally, the metadata includes the final amount that the user donated following a particular dialogue along with the intended donatation that the user specified in a dialogue. 

## Utterance-level information
For each utterance, we provide:

* id: index of the utterance
* user: the user who authored the utterance
* root: index of the conversation root of the utterance
* reply_to: index of the utterance to which this utterance replies to (None if the utterance is the first utterance in a conversation.)
* text: textual content of the utterance
* er_label_1: first persuasion strategy used by the persuader
* ee_label_1: first persuasion strategy used by the persuadee
* er_label_2: second persuasion strategy used by the persuader
* ee_label_2: second persuasion strategy used by the persuadee
* neg	: The negative sentiment of the utterance
* neu : The neutral sentiment of the utterance
* pos : The positive sentiment of the utterance

Metadata for utterances include:

* dialogue_idx: index of the dialogue from which this utterance occurs
* role: whether the utterance is spoken by the persuader ("0") or persuadee ("1")
* num_turns: The particular turn in which this utterance occurs in the dialogue

## Conversational-level information
Conversations are indexed by the id of the dialogue.

## Usage
To download directly with ConvoKit:
```
from convokit import Corpus, download
corpus = Corpus(filename=download("persuasion_corpus"))
```

For some quick stats:

```
len(corpus.get_utterance_ids())
20932
len(corpus.get_usernames())
1285
len(corpus.get_conversation_ids())
1017
```

## Contact
Please email any questions to: fl338\@cornell.edu, gd3435\@cornell.edu, dn273\@cornell.edu (Frank Li, Grace Deng, Di Ni). 

