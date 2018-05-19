#!/bin/bash

# remove empty lines and debug output
awk '!/Iteration.*/' output.txt > cleanedData.txt
awk '!/Temperature.*/' cleanedData.txt > cleanedData2.txt

# remove duplicates in training data and sort it
sort -u cleanedData2.txt > cleanedData3.txt
sort -u training_data.txt > sorted_training_data.txt

# remove examples in original data
comm -23 cleanedData3.txt sorted_training_data.txt > cleaned_output.txt

# cleanup
rm cleanedData.txt
rm cleanedData2.txt
rm cleanedData3.txt
rm sorted_training_data.txt

