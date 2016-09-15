juveniles_num = 10
adults_num = 10
seniles_num = 10
juveniles_surv_rate = 1
adults_surv_rate  = 1
seniles_surv_rate = 0
birth_rate = 2.0
num_generations = 25
generation_values = []
total_population = juveniles_num + adults_num + seniles_num
generation_values.append([juveniles_num, adults_num, seniles_num, total_population])


print()
print("Running model...\n")
# print headers and Generation 0 values
print("Generation     Juveniles     Adult     Seniles     Total")
print("{:>8}{:>14}{:>12}{:>11}{:>11}".format(0, juveniles_num, adults_num, seniles_num, total_population))

# iterate through generations
for i in range(1,num_generations + 1):
    juveniles_num, adults_num, seniles_num, total_population = generation_values[i-1]

    new_juveniles_num = int((adults_num * birth_rate))               
    new_adults_num = int((juveniles_num * juveniles_surv_rate))
    new_seniles_num = int(((seniles_num * seniles_surv_rate) + (adults_num * adults_surv_rate)))
    new_total_population = new_juveniles_num + new_adults_num + new_seniles_num
    
    generation_values.append([new_juveniles_num, new_adults_num, new_seniles_num, new_total_population])
    print("{:>8}{:>14}{:>12}{:>11}{:>11}".format(i, new_juveniles_num, new_adults_num, new_seniles_num, new_total_population))

print()
