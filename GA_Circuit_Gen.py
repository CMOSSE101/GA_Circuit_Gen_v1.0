
#****************
# GA Circuit Gen | v1
#****************
# By Ryan Brown

#---------------
# This programe generates
# a solution to a truth table
# through the use of
# Genetic Alogorithms
#---------------



# RANDOM BOOL TO TRUTH TABLE SITE
# https://www.dcode.fr/boolean-truth-table
# ^ To verify answers


import pandas as pd
import random
import matplotlib
#import numpy as np

# start on screen instruct
from starter import logoDisp
logoDisp()


#\/\/\/\/\/\/\/\/\/\/
#--------------------


# *CHANGABLE*
# Truth table to generate an equation from
truthTable = [[0,0,0],
              [0,1,1],
              [1,0,0],
              [1,1,0]]

# *CHANGABLE*
# Size of population
population_size = 10
crossover_rate = 100 # NOT USED CURRENTLY
mutation_rate = 50 # NOT USED CURRENTLY
max_gens = 40


#--------------------
#\/\/\/\/\/\/\/\/\/\/



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
#

# Suitable solution presented to user:

# > Generated boolen equation as chromosome



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



# GLOBAL VARUABLES
# ----------------

population = []

fitness_scores = []

succesfull = []

solution_found = False
generation_num = 0



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
#----------------------------------------------------------#
############################################################



# Generate Initial Population
# --------------------------

# Database for storing chromosomes
#pop_base = pd.DataFrame(columns=['Chromosomes'])

def genChromosomes():
    global pop_base
    # Generate chromosomes for speicied population size
    for i in range(0,population_size):
                           # Generate Gate 1
        population.append([[1,2, random.randint(0, 9)],
                           # Generate Gate 2
                           [1,2, random.randint(0, 9)],
                           # Generate Gate 3
                           [3,4, random.randint(0, 5)], # cannot be A, B, NOT A, NOT B
                           # Output never changes
                           [5]])

    #pop_base = pop_base.append({'Chromosomes':i}, ignore_index=True)

    # Display the produced population
    print("\nGenerated Initial Population:\n-----------------------------")
    for i in range(0,population_size):
        print(" | " + str(i) + " |    " + str(population[i]))



    input("\nPress Enter to continue...")



# Evaluation
# ----------

# Logic Gates

def AND(a,b):
    if (a==1) and (b==1):
        return True
    else:
        return False


def OR(a,b):
    if (a==1) or (b==1):
        return True
    else:
        return False


def XOR(a,b):
    if (a!=b):
        return True
    else:
        return False


def NAND(a,b):
    if (a==1) and (b==1):
        return False
    else:
        return True


def NOR(a,b):
    if (a==1) or (b==1):
        return False
    else:
        return True


def XNOR(a,b):
    if (a!=b):
        return False
    else:
        return True

def A(a,b):
    return a

def B(a,b):
    return b

def NOT_A(a,b):
    return not a

def NOT_B(a,b):
    return not b


# Evaluate given circuit (chromosome)
def testChromosome(chromosome,a,b):
    # gate 1
    if chromosome[0][2] == 0:
        c = AND(a,b)
    elif chromosome[0][2] == 1:
        c = OR(a,b)
    elif chromosome[0][2] == 2:
        c = XOR(a,b)
    elif chromosome[0][2] == 3:
        c = NAND(a,b)
    elif chromosome[0][2] == 4:
        c = NOR(a,b)
    elif chromosome[0][2] == 5:
        c = XNOR(a,b)
    elif chromosome[0][2] == 6:
        c = A(a,b)
    elif chromosome[0][2] == 7:
        c = B(a,b)
    elif chromosome[0][2] == 8:
        c = NOT_A(a,b)
    elif chromosome[0][2] == 9:
        c = NOT_B(a,b)
        
    # gate 2
    if chromosome[1][2] == 0:
        d = AND(a,b)
    elif chromosome[1][2] == 1:
        d = OR(a,b)
    elif chromosome[1][2] == 2:
        d = XOR(a,b)
    elif chromosome[1][2] == 3:
        d = NAND(a,b)
    elif chromosome[1][2] == 4:
        d = NOR(a,b)
    elif chromosome[1][2] == 5:
        d = XNOR(a,b)
    elif chromosome[1][2] == 6:
        d = A(a,b)
    elif chromosome[1][2] == 7:
        d = B(a,b)
    elif chromosome[1][2] == 8:
        d = NOT_A(a,b)
    elif chromosome[1][2] == 9:
        d = NOT_B(a,b)
        
    # gate 3
    if chromosome[2][2] == 0:
        e = AND(c,d)
    elif chromosome[2][2] == 1:
        e = OR(c,d)     
    elif chromosome[2][2] == 2:
        e = XOR(c,d)
    elif chromosome[2][2] == 3:
        e = NAND(c,d)
    elif chromosome[2][2] == 4:
        e = NOR(c,d)
    elif chromosome[2][2] == 5:
        e = XNOR(c,d)
    elif chromosome[2][2] == 6:
        e = A(c,d)
    elif chromosome[2][2] == 7:
        e = B(c,d)
    elif chromosome[2][2] == 8:
        e = NOT_A(c,d)
    elif chromosome[2][2] == 9:
        e = NOT_B(c,d)

    # Return output of circuit
    return e


# calculates fitness of chomosome
def fitnessCalc(chromosome):
    global solution_found # if chromosome passes all tests
    fitnessScore = 0 #  tracks fitness of chromosome

    # For each row in the truth table
    for row in range(0,4):
        # get truth table values
        a = truthTable[row][0]
        b = truthTable[row][1]
        correct = truthTable[row][2]

        # test circuit against truth table row
        result = testChromosome(chromosome,a,b)

        # update fitness score
        if result == correct:
            fitnessScore += (1*0.2)

        print("A: ",a," B: ",b," Correct: ",correct," Actual: ",result)

    # if chromosome fully succesfull
    if fitnessScore >= 0.8:
        solution_found = True
        # Add to succesfull population
        succesfull.append(chromosome.copy())

    # calulate gates transistors (approx)
    transistors = (gate_library[chromosome[0][2]][2] +
                   gate_library[chromosome[1][2]][2] +
                   gate_library[chromosome[2][2]][2])


    # update fitness for transistors used
    fitnessScore += ((1/transistors) *0.2) # smaller no. gates = better score

    print("\n\tFitness Score: ",fitnessScore,"/1")
    return fitnessScore



# checks if generation loop should end
def termination():
    # Checks against termination criteria.
    # False = Exit, True = Run
    if solution_found == True:
        print("\n\tTermation.... Solution Found\n\n")
        return False
    if generation_num >= max_gens:
        print("\n\tTermation.... Max Num Generations Exeeded\n\n")
        return False

    # if no termination criteria met
    return True



# generate boolean equation
def genBool(chromosome):

    # Create boolean equation
    equation = "Z = ("

    # first layer gate (3)
    if (chromosome[0][2] not in (6,7,8,9)):
        equation += "A "
    equation += gate_library[chromosome[0][2]][1]
    if (chromosome[0][2] not in (6,7,8,9)):
        equation += " B"
    equation += ") "
    
    # end gate (5)
    equation += gate_library[chromosome[2][2]][1]
        
    # first layer gate (4)
    equation += " ("
    if (chromosome[0][2] not in (6,7,8,9)):
        equation += "A "
    equation += gate_library[chromosome[1][2]][1]
    if (chromosome[0][2] not in (6,7,8,9)):
        equation += " B"
    equation += ") "

     # calulate gates used (approx)
    transistors = (gate_library[chromosome[0][2]][2] +
                   gate_library[chromosome[1][2]][2] +
                   gate_library[chromosome[2][2]][2])

    
    print("\nBoolean Equation:\n\t" + equation)
    print("\nNumber of transistors used: " + str(transistors))

    genDiag(chromosome)


def genDiag(chromosome):

    # format text for within gate box's
    gate_3 = "            #  "
    gate_3 += gate_library[chromosome[0][2]][1]
    for i in range(0, 6-len(gate_library[chromosome[0][2]][1])):
        gate_3 += " "
    gate_3 += "#----"

    gate_4 = "            #  "
    gate_4 += gate_library[chromosome[1][2]][1]
    for i in range(0, 6-len(gate_library[chromosome[1][2]][1])):
        gate_4 += " "
    gate_4 += "#----"

    gate_5 = "                             #  "
    gate_5 += gate_library[chromosome[2][2]][1]
    for i in range(0, 6-len(gate_library[chromosome[2][2]][1])):
        gate_5 += " "
    gate_5 += "#---- OUTPUT (Z)"

    # display diagram
    print("Produced Curcuit:\n")
    print(" INPUT 1 ---##########")
    print(gate_3)
    print(" INPUT 2 ---##########   |")
    print("                          ---##########")
    print(gate_5)
    print("                          ---##########")
    print(" INPUT 1 ---##########   |")
    print(gate_4)
    print(" INPUT 2 ---##########\n")

    print("\n") # space fpor readability


# perform reprodcution, produce one child
def cross_Uniform(parent1, parent2):

    # all genes by defult from parent 1
    gene1 = parent1[0][2]
    gene2 = parent1[1][2]
    gene3 = parent1[2][2]

    # chromsoomes have 3 genes.
    # Generate 3 random values [0.0 -> 1.0]
    #if probability of parent 2 gene above 0.5, swap
    if random.randint(0, crossover_rate)/crossover_rate >= 0.5:
        gene1 = parent2[0][2]
        #print("cross")
    if random.randint(0, crossover_rate)/crossover_rate >= 0.5:
        gene2 = parent2[1][2]
        #print("cross")
    if random.randint(0, crossover_rate)/crossover_rate >= 0.5:
        gene3 = parent2[2][2]
        #print("cross")
    
    # return child
    child = [[1,2,gene1],[1,2,gene2],[3,4,gene3],[5]]
    #print (child)
    return child


# Mutate random genes
def mutate(chromosome):
    # generate probability of mutation
    prob_mutation = random.randint(0, mutation_rate)

    # If to mutate
    if prob_mutation == 1:
        # choose random gene to mutate
        gene_index = random.randint(0, 2)
        # select random value
        
        if gene_index == 2: # last gate cannot have value above 5
            gene_value = random.randint(0, 5)
        else:
            gene_value = random.randint(0, 9)
            

        chromosome[gene_index][2] = gene_value

        print("mutation")

    return chromosome
    

fitness_avg_log = []

# Evaluate all chromosomes in population
def genrationLoop():
    global population
    global fitness_avg_log
    global generation_num
    
    # Generation Loop
    while (termination()):
        
        # EVALUATE
        #---------

        fitness_scores = [] # clear old scores
        fitness_avg = 0
        

        # evaluate all chromosomes
        for i in range(0,population_size):
            print ("\n\nEvaluating Chromosome - [",i+1,"/ 10 ] - ", population[i])
            # calculate and record fitness scores. Chromosome index, score
            fitness_score = fitnessCalc(population[i])
            fitness_scores.append([i,fitness_score]) # index, score
            fitness_avg += fitness_score / population_size
            #print("AVG")
            #print(fitness_avg)
        fitness_avg_log.append(fitness_avg)
        #print(fitness_avg_log)


        # 
        # TERMINATION CHECK
        #------------------
        print ("\nGeneration - Finnished")
        print ("----------------------")
        # find and display any succesfull chromosomes 
        if termination() == False:
            # notify of feasable solution
            print("\nFEASABLE SULUTION FOUND")
            print("-----------------------")
            input("Press Enter to continue...")


            
            # display new population
            print("\nNew Population: (Gen ",generation_num,")")
            print("-----------------------------")
            for i in range(0, population_size):
                print(" | " + str(i) + " |    " + str(population[i]) + " | Fitness : " + '%.4f' %fitness_scores[i][1])   

            input("Press Enter to continue...")

            # display succesful chromosome count
            num_success = len(succesfull)
            print("\nSuccesfull Chromosomes : ", num_success)
            print("")
            
            # print all succesfull chromosomes
            for i in range(0, num_success):
                print(succesfull[i])
                genBool(succesfull[i])

            # display generation count
            print("\n\n Generations passed: " + str(generation_num))
            break



        # SELECTION
        #----------
        
        #print(fitness_scores)
        # sort list by order of fitness score values (Small to Large)
        fitness_scores.sort(key = lambda fitness_scores: fitness_scores[1])
        # reverse order of list (Large to Small)
        fitness_scores.reverse()
        #print(fitness_scores)
              
        # select most highest chromosome
        parent_1 = population[fitness_scores[0][0]]
        # select second highest chromosome
        parent_2 = population[fitness_scores[1][0]]

        # print selected parents
        print("\nSelected Parents:")
        print(parent_1)
        print(parent_2)



        # REPRODUCTION
        #-------------
        new_population = []
        # generate new child population
        print("\nGenerating new population")
        for i in range(0, population_size):
            new_population.append(cross_Uniform(parent_1, parent_2))
            #print("population new")
            #print(new_population)



        # MUTATION
        #---------
        # for each chromosome, randomly choose if and hwere to mutate
        for i in range(0, population_size):
            new_population[i] = mutate(new_population[i])


        population = []
        population = new_population.copy() # replace old population

        generation_num += 1

        # display new population
        print("\nNew Population: (Gen ",generation_num,")")
        print("-----------------------------")
        for i in range(0, population_size):
            print(" | " + str(i) + " |    " + str(population[i]) + " | Fitness : " + '%.4f' %fitness_scores[i][1])   

            
        # END OF GENERATION
        #------------------
        #input("\nPress to continue... (Next Gen)")





###########
# MAIN CODE
###########

genChromosomes()
genrationLoop()


input("\nPress to continue... (End Program & Plot Results)")



# log and plot fitnesses
fit_log = pd.DataFrame(fitness_avg_log)
fit_log_plot = fit_log.plot(kind="line", grid=True).get_figure()
fit_log_plot.savefig("GA_Circuit_Average_Fitness.pdf")
print("Average Fitness Plot - Complete")

print("\n\nEnd Of Program")



# www.cmoss-electronics.com


