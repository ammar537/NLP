import networkx as nx
import matplotlib.pyplot as plt

def plot_degree_distribution(graph):
        unique_degree = []
        count_degree = []
        for i in nx.degree(graph):
                unique_degree.append(i[0])
                count_degree.append(i[1])
        
        print(len(unique_degree))
        print(len(count_degree))
                

        plt.bar(unique_degree, count_degree)
        plt.show()

# def plot_degree_distribution_2(graph):
#         unique_degree = []
#         count_degree = []

#         print(nx.degree(graph))
        
# graph = nx.read_edgelist('facebook_combined/facebook_combined.txt')
graph = nx.read_edgelist('wiki-Vote.txt/wiki-Vote.txt')


print (nx.info(graph))

nx.draw(graph)
plt.show()

# plot_degree_distribution(graph)