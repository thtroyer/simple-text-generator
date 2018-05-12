from textgenrnn import textgenrnn
import os

training_file = "training_data.txt"

textgen = textgenrnn()
num_loops = 50 
temperatures_to_generate = [0.2, 0.5, 0.8, 1.0, 1.2, 1.5]

def saveLinesToFile(file_name, iteration, temperature, data):
    file_handle = open(file_name + ".txt", "a")
    file_handle.write("Iteration: " + str(iteration) + "\n")
    file_handle.write("Temperature : " + str(temperature) + "\n")
    for item in data:
        file_handle.write(item)
        file_handle.write("\n")
    file_handle.write("\n")
    file_handle.write("____________________________\n")
    file_handle.close()

for i in range(0,num_loops):
    textgen.train_from_file(training_file, num_epochs=1)
    
    for temp in temperatures_to_generate:
        generated = textgen.generate(n=50, return_as_list=True, temperature=temp)
        saveLinesToFile("output", i, temp, generated)

