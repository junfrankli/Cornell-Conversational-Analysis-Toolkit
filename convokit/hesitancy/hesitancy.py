from typing import Callable, Generator, Tuple, List, Dict, Set, Optional, Hashable
from collections import defaultdict

from convokit.transformer import Transformer
from convokit.model import Corpus, User, Utterance, Conversation
import re
import numpy as np

class hesitancy(Transformer):

    def __init__(self, verbose: bool=False):
        self.NAME1 = 'Pause'
        self.NAME2 = 'Hesitancy'
        self.NAME3 = 'Avg Pause'
        self.NAME4 = 'Avg Hesitancy'
        self.verbose = verbose

    def transform(self, corpus: Corpus) -> Corpus:
        """Computes the count of pause and hesitancy words for each utterance, then aggregates them for each conversation
        
        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """

        if self.verbose: print("Finding counts of pause and hesitancy words...")
        
        pause_words = ['um', 'umm', 'ummm', 'uh', 'uhh', 'uhhh', 'hm', 'hmm', 'hmmm', 'er', 'err', 'uh huh', 'huh',
               'mhm', 'mhmm', 'erm', '...', 'ah', 'ahh', 'ahem', 'eh', 'ehh', 'ehhh', 'meh']
        hesitant_words = ['maybe', 'not',  'sure', 'unsure', 'probably', 'well', 'okay', 'like', 'actually', 
                   'basically', 'seriously', 'totally', 'literally', 'know', 'mean', 
                   'guess', 'suppose', 'but', 'something', 'so', 'wow', 'just', 'really', 
                  'later', 'wait', 'future', 'almost', 'slightly', 'perhaps', 'somehow', 
                 'sort', 'kind', 'little', 'somewhat', 'hey', 'alas', 'see', 'sounds', 'ok',
                 'roughly', 'why', 'how', 'yep', 'yup', 'may', 'possibly', 'might', 'could', 'doubt',
                 'skeptical', 'don\'t', 'won\'t', 'nah']

        pause = []
        hesitancy = []
        allutterids = corpus.get_utterance_ids()
        for i in list(range(0, len(allutterids))):
            utter_id = allutterids[i]
            text = corpus.get_utterance(utter_id).text
            textcleaned = "".join(c for c in text if c not in ('!','.',':', '?', '\'', ',', '\"', '@', '#', '$', '%', 
                                                       '^', '&', '*', '(', ')', '-', '~', '`', '_', '+', '=', 
                                                       '>', '<', '[', ']', '{', '}'))
            textlist = textcleaned.split()
            npause = len([i for i in textlist if i in pause_words])
            nhesitant = len([i for i in textlist if i in hesitant_words])
            pause.append(npause) #gives number of pause words in each utterance
            hesitancy.append(nhesitant) #gives number of hesitant words in each utterance
            corpus.get_utterance(utter_id).meta[self.NAME1] = npause
            corpus.get_utterance(utter_id).meta[self.NAME2] = nhesitant
        
        allconvoids = corpus.get_conversation_ids()
        for i in list(range(0, len(allconvoids))):
            convo_id = allconvoids[i]
            convo_utters = corpus.get_conversation(convo_id)._utterance_ids
            avgpause = np.mean(np.asarray(pause)[np.asarray(convo_utters)])
            avghesitancy = np.mean(np.asarray(hesitancy)[np.asarray(convo_utters)])
            corpus.get_conversation(convo_id)._meta[self.NAME3] = avgpause
            corpus.get_conversation(convo_id)._meta[self.NAME4] = avghesitancy

        return corpus

    def _preprocess_utterances(self, corpus: Corpus) -> Tuple[List[Hashable], List[Dict]]:
        """Preprocessing won't be needed.
        
        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """
        
        return corpus