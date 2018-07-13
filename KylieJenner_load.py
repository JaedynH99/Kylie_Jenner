import string

from Vocabulary import Digraph, Word, Edge

graph=Digraph()

def load_article(article):
    global graph
    with open('article.txt') as a:
        previous_word=None
        for i, line in enumerate(a):
            table = str.maketrans(dict.fromkeys(string.punctuation))
            line = line.translate(table)
            for w, word in enumerate(line.split()):
                # print(i, w, word)
                node = graph.add_node(Word(word.lower(),(i,w)))
                if previous_word:
                    graph.add_edge(Edge(previous_word, node))
                previous_word = node

    a.close()


load_article('article.txt')
print(graph)
print(graph.find_distance('influx','entrepreneurs'))