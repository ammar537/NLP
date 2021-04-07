import numpy
import sys

graph = {}
page_rank_arr=[[1 for i in range(1)]]
matrix = [[0 for i in range(1)] for j in range(1)]
teleporation_parameter = [[0.85] for i in range(1)]
converge = False
# ouput1_file = open("ouput1.txt" , "w")
ouput2_file = open("ouput2.txt" , "w")
num_list= []
max_nodes = 0


        # Open file
def get_file():   
        global max_nodes
        input_file = open(sys.argv[1], "r")

        for line in input_file:
                num_list.append(line.strip().split(" "))
                (key, val) = line.split()
                graph.setdefault(int(key),[]).append(int(val))

        num_list_numpy = numpy.array(num_list)
        max_nodes= int((max(num_list_numpy.flatten()))) + 1
        print("max_nodes" , max_nodes)


# Print Key & Values of the graph
def print_inputfile_graph_values():
        for key, val in graph.items():
                print("< " + str(key) + " : ", end = "")
                # ouput1_file.write("< " + str(key) + " : ")

                for element in val:
                        print(str(element) , end=" ")
                        # ouput1_file.write(str(element) + " ")

                print(">")
                # ouput1_file.write("> \n")



# initialize matrix
def form_matrix():
        global matrix
        matrix = [[0 for i in range(max_nodes)] for j in range(max_nodes)]
        for key, val in graph.items():
                for i in range(max_nodes):
                        if i in val:
                                matrix[key][i] = 1/len(val)
                        else:
                                matrix[key][i] = 0
        print(matrix)


# calculate matrix * teleportation
def page_rank_calculation():
        global page_rank_arr
        page_rank_arr=[[1 for i in range(max_nodes)]]
        matrix_transpose = numpy.transpose(matrix)
        teleporation_parameter = [[0.85] for i in range(max_nodes)]
        teleporation_parameter_numpy = numpy.array(teleporation_parameter)
        for i in range(100):
                result = numpy.dot(matrix_transpose, teleporation_parameter_numpy)
                page_rank_arr.append(result.ravel().tolist())
                print (page_rank_arr[i])
                
                max_percentage = 0
                for j in range(max_nodes):
                        percentage = (abs(result[j] - teleporation_parameter_numpy[j])/teleporation_parameter_numpy[j]) *100
                        
                        # Calcualte Maximum Change
                        if (max_percentage < percentage[0]):
                                max_percentage = percentage[0]


                print("Maximum change compared to last Matrix = " , max_percentage)

                # assign the new value for new iteration
                teleporation_parameter_numpy = result
                
                # check if the percentage change is less than 5%
                if(max_percentage < 5):
                        print("It Converges")
                        ouput2_file.write("It converges \n\n")
                        break

        iteration_number = 0
        for line in page_rank_arr:

                ouput2_file.write("Iteration Number = " + str(iteration_number) + "\n< ")
                for i in range(len(line)):
                        ouput2_file.write(str(i) + " : " + str(line[i]) )
                        if (i!=5):
                                ouput2_file.write(",\t")
                ouput2_file.write("> \n\n")
                iteration_number += 1


        

# main
if __name__ == "__main__":
    get_file()
    print_inputfile_graph_values()
    form_matrix()
    page_rank_calculation()
    print(max_nodes , max_nodes)
