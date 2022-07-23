


logoMain = """

######      ##      #######  ######  ######
##        ######    ##   ##   ##      ##
##      ##  ##  ##  ##   ##    ##      ##
##      ##      ##  ##   ##     ##      ##
######  ##      ##  #######  ######  ######
######  ##      ##  #######  ######  ######  
"""


logoRevise = """
*************************************************
*     //----//  //------ ||    //               *
*    //    //  //        ||   //                *
*   //====//  //=======  ||  //                 *
*  //  \\\    //          || //                  *
* //    \\\  //######     ||// -ISION [Uni_2022] *
*************************************************

 -Produced by Ryan.A.Brown (BEng)


 * Currently under delevopment *

Press to continue instruction...
"""


instructionsA = """

 #**********************
 # GA Circuit Gen | v1 #
 #**********************
 # By Ryan Brown
 

 #-----------------------------
 # This program generates
 # a solution to a truth table
 # through the use of
 # Genetic Alogorithms
 #-----------------------------

 # Average fitness logged in a graph
 # PDF format (In defualt folder)


 **********************
 * Modules Needed:    *
 * ---------------    *
 *   Pandas           *
 *   Random           *
 *   Matplotlib       *
 *                    *
 * [Pip Installable]  *
 **********************



 # RANDOM BOOL TO TRUTH TABLE SITE
 # https://www.dcode.fr/boolean-truth-table
 # ^ To verify answers


Press to continue instruction...

"""


instructionsB = """

----------------------------------------
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

 # Truth table presented to system:

 #  A | B | Output
 # ---|---|-------
 #  0 | 0 |   X
 #  0 | 1 |   X
 #  1 | 0 |   X
 #  1 | 1 |   X


 # Combinations of chromosomes generated :

 # INPUT 1 ---##########
 #            # GATE 3 #----
 # INPUT 2 ---##########   |
 #                          ---##########
 #                             # GATE 5 #---- OUTPUT
 #                          ---########## 
 # INPUT 1 ---##########   |
 #            # GATE 4 #---
 # INPUT 2 ---##########

 
 # Produced Equation:
 
 #    Z = [(A GATE_3 B) GATE_5 (A GATE_4)]

\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
----------------------------------------


Press to continue instruction...

"""

instructionsC = """

 # Producing a GA steps
 #---------------------
 # 1. Chromosome Representatiom
 # 2. Fitness Function
 # 3. Selection Mechanism
 # 4. Reproduction (Cross-Over)
 # 5. Mutation Method
 # 6. Termination Criteria



 # GA Geration Cycle Loop
 #-----------------------
 # 1. Initial Population Gen
 # 2. Evaluate
 # 3. Terminate Check
 # 4. Selection
 # 5. Reproduction
 # 6. Mutation
 # 7. (Goto 2)


Press to continue instruction...

"""

instructionsD = """

 # Chromosome Representation
 # -------------------------

 # Gate Library (Gate type to be selected from)
 # library number, gate name, number of transistors required (approx)
 gate_library = [[0,"AND",6],
                 [1,"OR",6],
                 [2,"XOR",8],
                 [3,"NAND",4],
                 [4,"NOR",4],
                 [5,"XNOR",10],
                 [6,"A",0],
                 [7,"B",0],
                 [8,"NOT A",2],
                 [9,"NOT B",2]]


 # Inputs |  Layer 1 | Layer 2 |  Output
 # -------|----------|---------|--------
 #   1    |  Gate 3  | Gate 5  | Output
 #   2    |  Gate 4  |         |

 # [1-In, 2-In, 3][1-In, 2-In, 4][3-Out, 4-Out, 5][5-Out]

 # [1,2,3][1,2,4][3,4,5][5]

 chromosomeTemplate = [[1,2,0],[1,2,0],[3,4,0],[5]]


Press to continue instruction...

"""


instructionsE = """

 # Fitness Function
 # -----------------

 # Multi-Variable fitness function, where each output
 # produced by the system will be compared to the target.
 # The higher the fitness score, the higher the effectiveness.

 # Min value = 0, Mav value (target) = 1
 # All weights equal to 1/4.
 # Output : 1=MATCH, 0=FAIL

 # F(chromosome) = (out_1*w1) + (out_2*w2) + (out_3*w3) + (out_4*w4)



 # Selection Mechanism
 # -------------------

 # The two highest scoring chromosomes are selected as parents.


Press to continue instruction...
"""


instructionsF = """

 # Reproduction (Cross-Over)
 # -------------------------

 # Uniform crossover fromn two parents on each gene
 # with a threshold of 0.5 or above to swap.
 # **Parent one always given probability of 0.5**


 # EXAMPLE

 #               (0.5)    (0.5)    (0.5)
 #                |        |        |
 # Parent 1 [1,2,*0*][1,2,*2*][3,4,*4*][5]

 #               (0.1)    (0.6)    (0.8)
 #                |        |        |
 # Parent 2 [1,2,*1*][1,2,*3*][3,4,*5*][5]


 #   Produces :

 # Child 1 [1,2,*0*][1,2,*3*][3,4,*8*][5]
 #                        ^        ^

 # Child 2 [1,2,*1*][1,2,*2*][3,4,*4*][5]
 #                        ^        ^

 # ** In this program only one child is produced**

 # Reproduction of the two best candidates will repeat
 # until a new population of the required size is fufilled.


Press to continue instruction...

"""


instructionsG = """

# Mutation Method
# ---------------

# Mutation will randomly select a gene froma random
# position as choose a new value from a range (0 -> 6).

# Mutation rate is 0.1 (1 out of ten)



# Termination Criteria
# --------------------

# The generation loop will terminate if either:
# 1. A solution has been found (Fitness score of 1)
# 2. Exceeded a count of 200 generations



############################################################
#--PROGRAM--STARTING--IMINANT--#  Press Enter To Continue  #
############################################################


"""

def logoDisp():
    print(logoMain)
    print(logoRevise)

    input()
    input(instructionsA)
    input()
    input(instructionsB)
    input()
    input(instructionsC)
    input()
    input(instructionsD)
    input()
    input(instructionsE)
    input()
    input(instructionsF)
    input()
    input(instructionsG)








