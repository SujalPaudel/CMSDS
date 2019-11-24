import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir("data/train/100%_te"): 
        dst ="e-" + str(i) + ".png"
        src ="data/train/100%_te/"+ filename 
        dst ="data/train/100%_te/"+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 