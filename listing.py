import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
    imlist = []
    for filename in os.listdir("data/train/input_data"): 
        if filename.startswith('a'):
            imlist.append(filename)
            # print("yes")
    
    print(imlist)
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 