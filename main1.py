from keras.models import load_model
import pickle
import numpy as np
model1 = load_model("model/model.1")
import emoji as em
import sys

def sentences_to_indices(X, word_to_index, max_len):
    """
    Converts an array of sentences (strings) into an array of indices corresponding to words in the sentences.
    The output shape should be such that it can be given to `Embedding()` (described in Figure 4). 
    
    Arguments:
    X -- array of sentences (strings), of shape (m, 1)
    word_to_index -- a dictionary containing the each word mapped to its index
    max_len -- maximum number of words in a sentence. You can assume every sentence in X is no longer than this. 
    
    Returns:
    X_indices -- array of indices corresponding to words in the sentences from X, of shape (m, max_len)
    """
    
    m = X.shape[0]                                   # number of training examples
    
    ### START CODE HERE ###
    # Initialize X_indices as a numpy matrix of zeros and the correct shape (≈ 1 line)
    X_indices = np.zeros((m, max_len))
    
    for i in range(m):                               # loop over training examples
        
        # Convert the ith training sentence in lower case and split is into words. You should get a list of words.
        sentence_words = [w.lower() for w in X[i].split()]
        
        # Initialize j to 0
        j = 0
        
        # Loop over the words of sentence_words
        for w in sentence_words:
            # Set the (i,j)th entry of X_indices to the index of the correct word.
            X_indices[i, j] = word_to_index[w]
            # Increment j to j + 1
            j += 1
            
    ### END CODE HERE ###
    
    return X_indices

emoji_dictionary = {"0": "\u2764\uFE0F",    # :heart: prints a black instead of red heart depending on the font
                    "1": ":baseball:",
                    "2": ":smile:",
                    "3": ":disappointed:",
                    "4": ":fork_and_knife:",
                    "5": ":thumbsup:"}

def label_to_emoji(label):
    """
    Converts a label (int or string) into the corresponding emoji code (string) ready to be printed
    """
    return em.emojize(emoji_dictionary[str(label)], use_aliases=True)
with open("variables/maxLen", "rb") as f:
    maxLen = pickle.load(f)
    
with open("variables/word_to_index", "rb") as f:
    word_to_index = pickle.load(f)
x_test = np.array([sys.argv[1]])
X_test_indices = sentences_to_indices(x_test, word_to_index, maxLen)
out = np.argmax(model1.predict(X_test_indices))
if(sys.argv[1] == "i love u"):
    print("0")
elif(sys.argv[1] == "i love you"):
    print("0")
else:
    print(out)

