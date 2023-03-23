# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin,

pKR = {'y' : 10.07, 'c' : 8.18, 'k' : 10.53, 'h' : 6.00, 'r': 12.48, 'd' : 3.65, 'e' : 4.25 }
# Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation.


# Using count() to count the numbers of each amino acid
# To identify a count of an item within a list, you can use the count() method.

# To see how many amino acids in insulin are Y, use the count() method by entering:
insulin.count("x")
# update
float(insulin.count("x"))
seqCount = ({x:
float(insulin.count("x")) for x in
['y', 'c', 'k', 'h', 'r', 'd', 'e']
})
# The first two steps in this exercise are predecessors to the third step.

# Create a variable called pH and initialize it to zero
pH = 0
# Create the while loop by entering 
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

    print('{0:.2f}'.format(pH), netCharge)
# increment the pH variable
    pH +=1
    
