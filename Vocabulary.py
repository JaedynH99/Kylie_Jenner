visited=[]
class Word:
    def __init__(self, word, position):
        self.word=word
        self.positions=[position]


    def add_position(self, position):
        self.positions.extend(position)

    def __str__(self):
        return self.word

class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return f'{self.src}->{self.dest}'


class Digraph(object):
        """Represents a directed graph of Node and Edge objects"""

        def __init__(self):
            self.nodes = set([])
            self.edges = {}  # must be a dict of Node -> list of edges

        def __str__(self):
            edge_strings = []
            for edges in self.edges.values():
                for edge in edges:
                    edge_strings.append(str(edge))
            edge_strings = sorted(edge_strings)  # sort alphabetically
            return '\n'.join(edge_strings)  # concat edge_strings with "\n"s between them

        def get_edges_for_node(self, node):
            return self.edges[node]

        def has_node(self, node):
            return node in self.nodes

        def add_node(self, word):
            new_word=self.find(word)
            if new_word:
                new_word.add_position(word.positions)
                return new_word
            else:
                self.nodes.add(word)
                return(word)

        def add_edge(self, edge):
            """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
            ValueError if either of the nodes associated with the edge is not
            in the  graph."""
            if edge.src not in self.nodes:
                self.add_node(edge.src)
            if edge.dest not in self.nodes:
                self.add_node(edge.dest)

            if edge.src not in self.edges.keys():
                self.edges[edge.src] = [edge]
            else:
                self.edges[edge.src].append(edge)

        def find(self, word):
            for test in self.nodes:
                if word.word==test.word:
                    return test
            return None

        def find_word(self, str):
            for test in self.nodes:
                if str==test.word:
                    return test
            return None

        def find_min_distance(self, start_node, end_node, depth, min_depth):
            global visited
            if min_depth:
                if depth>=min_depth:
                    return min_depth
            if depth>50:
                return None
            visited.append(start_node)
            edges=self.get_edges_for_node(start_node)
            for edge in edges:
                if edge.dest==end_node:
                    return depth
            for edge in edges:
                if edge not in visited:
                    end_depth= self.find_min_distance(edge.dest, end_node, depth + 1, min_depth)
                    if end_depth and (not min_depth or end_depth < min_depth):
                        min_depth=end_depth
            return min_depth

        def find_distance(self, start, end):

            start_node=self.find_word(start)
            end_node=self.find_word(end)
            if not start_node or not end_node:
                raise ValueError
            return self.find_min_distance(start_node,end_node, 1, None)
            # pass



