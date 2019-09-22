from typing import Callable, Generator, Tuple, List, Dict, Set, Optional, Hashable
from collections import defaultdict

from convokit.transformer import Transformer
from convokit.model import Corpus, User, Utterance, Conversation
import re
import numpy as np

class AvgQuestions(Transformer):

    def __init__(self, verbose: bool=False):
        self.ATTR_NAME = "AvgQuestions"
        self.verbose = verbose

    def transform(self, corpus: Corpus) -> Corpus:
        """Computes the average number of questions asked in a conversation
        
        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """

        if self.verbose: print("Finding questions per utterance")
        
        questions = []
        allutterids = corpus.get_utterance_ids()
        for i in list(range(0, len(allutterids))):
            utter_id = allutterids[i]
            text = corpus.get_utterance(utter_id).text
            nquestions = len(re.findall(r'\?+', text))
            questions.append(nquestions) #gives number of questions in each utterance
         
        if self.verbose: print("Finding questions per conversation")
        allconvoids = corpus.get_conversation_ids()
        for i in list(range(0, len(allconvoids))):
            convo_id = allconvoids[i]
            convo_utters = corpus.get_conversation(convo_id)._utterance_ids
            avgquestion = np.mean(np.asarray(questions)[np.asarray(convo_utters)])
            corpus.get_conversation(convo_id)._meta[self.ATTR_NAME] = avgquestion 
            #adds average questions per conversation to conversation metadata

        return corpus

    def _preprocess_utterances(self, corpus: Corpus) -> Tuple[List[Hashable], List[Dict]]:
        """Preprocessing won't be needed.
        
        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """
        
        return corpus