import time
import random
sentences=[ "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class."
    ]

def typing_test():
    test_sentence=random.choice(sentences) #UPAR SENTENCE VARIABLE MEI SE KOI BHI RANDOM SENTENCE DE SKTI HAI IS FUNCTION KE THROUGH 
    print("TYPE THE FOLLOWING SENTENCE AS FAS AS YOU CAN")
    print(test_sentence)
    input("enter if you are ready for the test....")
    start_time=time.time() # MEASURES THE START TIME
    user_input= input("\nstart typing...\n")
    end_time=time.time()
    original_words = test_sentence.split()
    typed_words = user_input.split()
    correct_words=0
    for original, typed in zip(original_words, typed_words):
        if original == typed:
            correct_words += 1
    time_taken = end_time - start_time
    time_taken_in_minutes=time_taken/60
    word_count=len(test_sentence.split())
    accuracy = (correct_words / len(original_words)) * 100

    print("result:")
    print(f"Time taken:{time_taken:.2f} seconds")
    print(f"words typed: {word_count}")
    print(f"Typing speed: {word_count / time_taken_in_minutes:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
typing_test()
