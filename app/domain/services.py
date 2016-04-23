from sklearn.feature_extraction.text import TfidfVectorizer


def extract_tags(text):
    tfidf_vect = TfidfVectorizer(stop_words=['in', 'the', 'on', 'a', 'she', 'he', 'and', 'or', 'to', 'for'])
    word_tfidf = tfidf_vect.fit_transform([text])
    word_list = tfidf_vect.get_feature_names()

    most_descriptive_tags = {}

    for i in word_tfidf[0].indices:
        word = word_list[i]
        tfidf = word_tfidf[0, i]
        if tfidf > 0.2:
            most_descriptive_tags[word] = tfidf

    sorted_result_with_most_descriptive_tags_coming_first = [word for word in sorted(most_descriptive_tags, key=most_descriptive_tags.get, reverse=True)]
    return sorted_result_with_most_descriptive_tags_coming_first


