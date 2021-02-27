#CSE122 HW4 Q2b
#Mingyu Ding @miding

p_a = 0.2
p_b = 0.4
p_c = 0.6
p_d = 0.7

inv_p_a = round(1-p_a, 1)
inv_p_b = round(1-p_b, 1)
inv_p_c = round(1-p_c, 1)
inv_p_d = round(1-p_d, 1)
count = 0

probs = [inv_p_a, inv_p_b, inv_p_c, inv_p_d]
min_order = [0, 0, 0, 0]
min_a_sum = 10

print("No.||a_1||a_2||a_3||a_sum")
#Select X
for x in probs:

    #select y
    for y in probs:
        if y==x:
            continue

        #select w
        for w in probs:
            if (w==x)or(w==y):
                continue

            #select x
            for z in probs:
                if (z==x)or(z==y)or(z==w):
                    continue
                else:
                    
                    #compute probilities and swtiching activities at each nodes
                    p_1 = round(1-(x*y), 2)
                    p_2 = round(1-(w*z), 2)
                    p_3 = round(1-((1-p_1)*(1-p_2)), 2)
                    a_1 = round((1-p_1)*p_1, 2)
                    a_2 = round((1-p_2)*p_2, 2)
                    a_3 = round((1-p_3)*p_3, 2)
                    a_sum = round(a_1 + a_2 + a_3, 2)

                    count = count + 1
                    print(count,a_1,a_2,a_3, a_sum)
                    #print(x,y,w,z)

                    if a_sum < min_a_sum:
                        min_order = [x, y, w, z]
                        min_a_sum = a_sum

#print result                        
print(">>>>>Result<<<<<")
print("Inputs Order's inv probs||min a summation")
print(min_order, min_a_sum)
                    
            