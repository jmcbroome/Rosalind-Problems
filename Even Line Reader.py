#Jakob McBroome
#BME 205

def even_read(filename):
    '''Function has file manipulation built in, taking a file path as input. Returns a list of strings representing lines numbered odd from the file with the first line being labeled number 1.'''
    with open(filename, "r") as input:
        lines_list = input.readlines()
        even_index = range(1, len(lines_list), 2)
        #this actually produces odd numbers, but since we're labeling the file lines starting with 1, we need odd indexes to correspond to even lines
        output_lines = []
        for index in even_index:
            if lines_list[index][-1:] == "\n": 
                output_lines.append(lines_list[index][0:-1])
                #the readlines() outputs lines with \n at the end, this strips them if they're present
            else:
                output_lines.append(lines_list[index])
            #append the entry in lines list
        return output_lines

even_read("even_line_test")
even_read("q5_input.txt")




