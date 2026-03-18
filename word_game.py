# https://moringa.instructure.com/courses/1379/assignments/86632?module_item_id=235809

paragraph = input("Enter a paragraph: ").lower()
word_to_count = input("Enter the word to count: ").lower()

def count_specific_word(paragraph, word_to_count):
    return paragraph.count(word_to_count)
    
def identify_most_common_word(paragraph):
    words = paragraph.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return max(word_count, key=word_count.get)

def calculate_average_word_length(paragraph):
    words = paragraph.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words) if words else 0
    return average_length

def count_paragraphs(paragraph):
    paragraphs = paragraph.split('\n\n')
    return len(paragraphs)

def count_sentences(paragraph):
    sentences = paragraph.split('. ')
    return len(sentences)

if __name__ == "__main__":
    print("Most common word:", identify_most_common_word(paragraph=paragraph))
    print("Average word length:", calculate_average_word_length(paragraph=paragraph))
    print("Sentense count:", count_sentences(paragraph=paragraph))
    print("Paragraph count:", count_paragraphs(paragraph=paragraph))
    print("Word count:", count_specific_word(paragraph=paragraph, word_to_count=word_to_count))