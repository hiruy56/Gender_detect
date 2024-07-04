from nltk.corpus import names
import nltk
import random

def gender_features(word):
    return {'last_letter': word[-1]}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender)
               for (n, gender) in labeled_names]

train_set, test_set = featuresets[500:], featuresets[:500]

with open('names.txt') as file:
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    while True:
        name = input("Enter a name (or 'exit' to quit): ")
        
        if name.lower() == 'exit':
            break
        
        prediction = classifier.classify(gender_features(name))
        
        if prediction == 'male':
            print("It's a male name.")
        elif prediction == 'female':
            print("It's a female name.")
        else:
            print("Couldn't determine the gender.")
