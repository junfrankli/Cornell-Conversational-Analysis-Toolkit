# Persuasion for Good 
A large metadata-rich collection of online conversations between two people where one participant ("persuader") is trying to convince the other ("persuadee") to donate to a charity. This dataset contains 1017 dialogues, each with several conversational turns. Additionally, every user has a personality vector associated with them generated through psycological surveys.

Distributed together with:
"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good" https://arxiv.org/pdf/1906.06725.pdf. Xuewei Wang et al. ACL 2019.

## Dataset details
Original data: https://gitlab.com/ucdavisnlp/persuasionforgood/tree/master/data

## User-level information
Users in this dataset are Amazon Turks. For each user, we further provide the following information as user-level metadata:

'extrovert.x'
'agreeable.x'
'conscientious.x'
'neurotic.x'
'open.x'
'care.x'
'fairness.x'
'loyalty.x'
'authority.x'
'purity.x'
'freedom.x'
'conform.x'
'tradition.x'
'benevolence.x'
'universalism.x'
'self_direction.x'
'stimulation.x'
'hedonism.x'
'achievement.x'
'power.x'
'security.x'
'rational.x'
'intuitive.x'
'age.x'
'sex.x'
'race.x'
'edu.x'
'marital.x'
'employment.x'
'income.x'
'religion.x'
'ideology.x\'

Additionally, the metadata includes the final amount that the user donated following a particular dialogue.

## Utterance-level information
For each utterance, we provide:

* id: index of the utterance
* user: the user who authored the utterance
* root: index of the conversation root of the utterance
* reply_to: index of the utterance to which this utterance replies to (None if the utterance is the first utterance in a conversation.)
* text: textual content of the utterance

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

