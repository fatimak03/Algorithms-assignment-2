#Assignment 2
#Fatima Khan
#100812028

#importing the time module to add delays for visualization
import time
#importing os module to use system beep sound
import os  

#merge sort function with step-by-step visualization
def merge_sort_with_steps(arr):
    #base case: if the array has more than one element, proceed with sorting
    if len(arr) > 1:
        #find the middle index of the array
        mid = len(arr) // 2  
        #split the array into left half
        L = arr[:mid] 
        #split the array into right half
        R = arr[mid:]  

        #print the process of dividing the array
        print("Dividing array:", arr)
        print("Left half:", L)
        print("Right half:", R)

        #recursively sort the left half
        merge_sort_with_steps(L)
        #recursively sort the right half
        merge_sort_with_steps(R)

        #initialize pointers for L, R, and the main array
        i = j = k = 0  

        #merge the sorted halves back into the main array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                #copy the smaller element from L to arr
                arr[k] = L[i]  
                #move the pointer in L
                i += 1  
            else:
                #copy the smaller element from R to arr
                arr[k] = R[j] 
                #move the pointer in R 
                j += 1  
                #sound effect for swap (beep sound)
                #produce a beep sound using os library
                print('\a')  
                #delay for better visualization
                time.sleep(0.1)  
            #move the pointer in the main array
            k += 1  

        #copy any remaining elements of L if there are any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        #copy any remaining elements of R if there are any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        #print the process of merging the array
        print("Merging:", arr)

#array to be sorted
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
#print the original array
print("Original Array:", arr)  
#call the merge sort function
merge_sort_with_steps(arr)  
#print the sorted array
print("Sorted Array:", arr)  

