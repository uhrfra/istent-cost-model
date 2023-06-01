import os
import random
import statistics

# from https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Tabellen/_tabellen-innen-lebenserwartung-sterbetafel.html
mortality_male = [0.00330799, 0.00022811, 0.00012285, 0.00011276, 0.00010963, 0.00009759, 0.00008445, 0.00008689,
                  0.00006758, 0.00007211, 0.00006572, 0.00006527, 0.00008257, 0.00009671, 0.00011849, 0.00015211,
                  0.00021986, 0.00027065, 0.00038214, 0.00042731, 0.00040762, 0.0004023, 0.00040448, 0.00041295,
                  0.00044439, 0.00042945, 0.00044999, 0.00045188, 0.00047417, 0.0004896, 0.00053827, 0.00058309,
                  0.00060129, 0.00065199, 0.00071628, 0.00077844, 0.00091236, 0.00103895, 0.00104265, 0.00116636,
                  0.00125828, 0.00143897, 0.00143241, 0.00167621, 0.00179318, 0.00192079, 0.00210387, 0.00238611,
                  0.00267489, 0.00304134, 0.00327823, 0.00365662, 0.00404999, 0.00447502, 0.00497629, 0.00568259,
                  0.00635367, 0.006982, 0.00776165, 0.00874689, 0.0096153, 0.0107523, 0.01187571, 0.01304604,
                  0.01433246, 0.01566113, 0.01718158, 0.01849977, 0.02007856, 0.02170607, 0.02328274, 0.02510174,
                  0.02723326, 0.02916232, 0.03205313, 0.03433424, 0.03786492, 0.04169168, 0.04486698, 0.04976661,
                  0.05575657, 0.06265298, 0.06935787, 0.07856244, 0.08942218, 0.1014755, 0.11494965, 0.1288383,
                  0.14618512, 0.16505988, 0.18472025, 0.20236514, 0.22730695, 0.24664126, 0.27199627, 0.2915915,
                  0.31952858, 0.33744518, 0.36148217, 0.38444607, 0.40668933]

mortality_female = [0.00284394, 0.00019787, 0.00011989, 0.00010329, 0.0000948, 0.000066, 0.0000622, 0.00005971,
                    0.00006217, 0.00005486, 0.0000491, 0.00007089, 0.0000617, 0.00008317, 0.00010635, 0.00011556,
                    0.00012415, 0.00012443, 0.00014995, 0.00017416, 0.00017059, 0.00017675, 0.00017209, 0.00016512,
                    0.00015664, 0.00017961, 0.0001769, 0.00020421, 0.00023613, 0.00023734, 0.00026558, 0.00030974,
                    0.00032993, 0.0003521, 0.00039098, 0.00046154, 0.00046864, 0.00053497, 0.00055386, 0.00063224,
                    0.00065609, 0.0007456, 0.00079752, 0.00089626, 0.00097747, 0.00105327, 0.00120013, 0.00129005,
                    0.00151559, 0.00170414, 0.00185245, 0.00203604, 0.00219746, 0.00249457, 0.00275499, 0.00305589,
                    0.0033585, 0.00371596, 0.0041746, 0.00461402, 0.00513519, 0.00555541, 0.00611401, 0.00680015,
                    0.00734921, 0.00813238, 0.0088305, 0.00957517, 0.01035715, 0.01157397, 0.01271682, 0.01392558,
                    0.01545559, 0.01669612, 0.01862441, 0.02026754, 0.02247963, 0.02505062, 0.02736759, 0.03121579,
                    0.03558687, 0.04070724, 0.0464882, 0.05418743, 0.06336499, 0.07338527, 0.08535191, 0.09808956,
                    0.11223342, 0.12860337, 0.14700761, 0.16548836, 0.18749316, 0.20782756, 0.23043549, 0.25364684,
                    0.27912421, 0.30141357, 0.32638665, 0.34127272, 0.36465451]


class PersonParameters:
    prob_male = 47.0 / (47.0 + 49.0)
    age_mean = 75.25
    age_sigma = 6.65
    # Units per year
    prob_med_k_prae = 53 / 96
    prob_med_b_prae = 60 / 96
    prob_med_a_prae = 30 / 96
    prob_med_p_prae = 86 / 96
    prob_med_k_post = 34 / 96
    prob_med_b_post = 39 / 96
    prob_med_a_post = 52 / 96
    prob_med_p_post = 20 / 96
    units_without_stent_mean = 2.23
    units_without_stent_sigma = 1.12
    units_with_stent_mean = 1.42
    units_with_stent_sigma = 1.34


class CostParameters:
    costs_med_k = 42.38 * 4
    costs_med_b = 17.70 * 4
    costs_med_a = 42.38 * 4
    costs_med_p = 68.00 * 4
    costs_per_stent = 1478.26


class Person:
    age: int
    is_male: bool
    has_stent: bool
    has_med_k: bool
    has_med_b: bool
    has_med_a: bool
    has_med_p: bool
    age_of_death: int

    def __str__(self):
        s = "age: " + str(self.age)
        s += "; age_of_death: " + str(self.age_of_death)
        s += "; is_male: " + str(self.is_male)
        s += "; has_stent: " + str(self.has_stent)
        s += "; has_med_k: " + str(self.has_med_k)
        s += "; has_med_b: " + str(self.has_med_b)
        s += "; has_med_a: " + str(self.has_med_a)
        s += "; has_med_p: " + str(self.has_med_p)
        return s


def make_person(params: PersonParameters, has_stent: bool):
    p = Person()
    p.age = round(random.normalvariate(params.age_mean, params.age_sigma))
    p.is_male = random.random() < params.prob_male
    p.has_stent = has_stent
    if has_stent:
        p.has_med_k = random.random() < params.prob_med_k_post
        p.has_med_b = random.random() < params.prob_med_b_post
        p.has_med_a = random.random() < params.prob_med_a_post
        p.has_med_p = random.random() < params.prob_med_p_post
    else:
        while True: # Without stent at least one med must be present
            p.has_med_k = random.random() < params.prob_med_k_prae
            p.has_med_b = random.random() < params.prob_med_b_prae
            p.has_med_a = random.random() < params.prob_med_a_prae
            p.has_med_p = random.random() < params.prob_med_p_prae
            if p.has_med_p or p.has_med_a or p.has_med_b or p.has_med_k:
                break

    p.age_of_death = 101
    for i in range(p.age, 101):
        m = random.random()
        if p.is_male:
            if m < mortality_male[i]:
                p.age_of_death = i
                break
        else:
            if m < mortality_female[i]:
                p.age_of_death = i
                break

    return p


def calculate_costs_in_life(p: Person):
    unit_sum = 0.0

    if p.has_stent:
        unit_sum += (p.age_of_death - p.age) * p.units_with_stent
    else:
        unit_sum += (p.age_of_death - p.age) * p.units_without_stent

    return unit_sum


cost_params = CostParameters()

num_samples = 10000


costs_with_stent = []
scatterplot_data_with_stent = []
treatment_costs_with_stent = {}

for i in range(0, num_samples):
    p = make_person(PersonParameters(), True)
    print(p)

    med_count = 0
    years = p.age_of_death - p.age
    costs = 0.0
    costs_per_year = 0.0

    if p.has_med_k:
        costs += cost_params.costs_med_k * years
        med_count += years
        costs_per_year += cost_params.costs_med_k

    if p.has_med_b:
        costs += cost_params.costs_med_b * years
        med_count += years
        costs_per_year += cost_params.costs_med_b

    if p.has_med_a:
        costs += cost_params.costs_med_a * years
        med_count += years
        costs_per_year += cost_params.costs_med_a

    if p.has_med_p:
        costs += cost_params.costs_med_p * years
        med_count += years
        costs_per_year += cost_params.costs_med_p

    if p.has_stent:
        costs += cost_params.costs_per_stent

    print("Costs: " + str(costs))
    costs_with_stent.append(costs)
    scatterplot_data_with_stent.append([med_count, costs, years])
    
    current_treatment_costs = cost_params.costs_per_stent
    for i in range(p.age, p.age_of_death):
        current_treatment_costs += costs_per_year
        if i-p.age in treatment_costs_with_stent:
            treatment_costs_with_stent[i-p.age].append(current_treatment_costs)
        else:
            treatment_costs_with_stent[i-p.age] = [current_treatment_costs]
         

costs_without_stent = []
scatterplot_data_without_stent = []
treatment_costs_without_stent = {}

for i in range(0, num_samples):
    p = Person()
    p = make_person(PersonParameters(), False)
    print(p)

    med_count = 0
    years = p.age_of_death - p.age
    costs = 0.0
    costs_per_year = 0.0

    if p.has_med_k:
        costs += cost_params.costs_med_k * years
        med_count += years
        costs_per_year += cost_params.costs_med_k

    if p.has_med_b:
        costs += cost_params.costs_med_b * years
        med_count += years
        costs_per_year += cost_params.costs_med_b

    if p.has_med_a:
        costs += cost_params.costs_med_a * years
        med_count += years
        costs_per_year += cost_params.costs_med_a

    if p.has_med_p:
        costs += cost_params.costs_med_p * years
        med_count += years
        costs_per_year += cost_params.costs_med_p

    if p.has_stent:
        costs += cost_params.costs_per_stent

    print("Costs: " + str(costs))
    costs_without_stent.append(costs)
    scatterplot_data_without_stent.append([med_count, costs, years])
    
    current_treatment_costs = 0
    for i in range(p.age, p.age_of_death):
        current_treatment_costs += costs_per_year
        if i-p.age in treatment_costs_without_stent:
            treatment_costs_without_stent[i-p.age].append(current_treatment_costs)
        else:
            treatment_costs_without_stent[i-p.age] = [current_treatment_costs]

#Output results
costs_with_stent_mean = statistics.mean(costs_with_stent)
costs_with_stent_stdev = statistics.pstdev(costs_with_stent)
print("Costs with stent: mean = {0:.2f}, stddev = {1:.2f}".format(costs_with_stent_mean, costs_with_stent_stdev))

costs_without_stent_mean = statistics.mean(costs_without_stent)
costs_without_stent_stdev = statistics.pstdev(costs_without_stent)
print(
    "Costs without stent: mean = {0:.2f}, stddev = {1:.2f}".format(costs_without_stent_mean, costs_without_stent_stdev))

# Output plot data to files
os.makedirs('plot_data', exist_ok = True)

with open('plot_data/scatterplot_with_stent.data', 'w') as f:
    for entry in scatterplot_data_with_stent:
        f.write(str(entry[0]) + "; " + str(entry[1]) + "; " + str(entry[2]) + ";\n")
        
with open('plot_data/scatterplot_without_stent.data', 'w') as f:
    for entry in scatterplot_data_without_stent:
        f.write(str(entry[0]) + "; " + str(entry[1]) + "; " + str(entry[2]) + ";\n")

treatment_costs_with_stent_avg = []
for i in range(0, 100):
    if not i in treatment_costs_with_stent:
        break
    treatment_costs_with_stent_avg.append(sum(treatment_costs_with_stent[i])/len(treatment_costs_with_stent[i]))

with open('plot_data/treatment_costs_with_stent_avg.data', 'w') as f:
    for entry in treatment_costs_with_stent_avg:
        f.write(str(entry) + ";\n")

treatment_costs_without_stent_avg = []
for i in range(0, 100):
    if not i in treatment_costs_without_stent:
        break
    treatment_costs_without_stent_avg.append(sum(treatment_costs_without_stent[i])/len(treatment_costs_without_stent[i]))
    
with open('plot_data/treatment_costs_without_stent_avg.data', 'w') as f:
    for entry in treatment_costs_without_stent_avg:
        f.write(str(entry) + ";\n")