# -------------------------------------------------------------#
# Title             :   week-01-fiber_cost_calculator
# Author            :   Sheetal Munjewar
# University        :   College of Science and Technology, Bellevue University
# Course            :   DSC 510 T302 Introduction to Data Science (2227-1)
# Professor         :   Michael Eller
# Initial Draft     :   08/10/2022
# -- Change log
# Author            :   Sheetal Munjewar
# Change date       :   08/10/2022
# Change Made       :   Initial draft.
# Change approved   :   Sheetal Munjewar
# Go Live Date      :   10/07/2022
# -------------------------------------------------------------#
# -- Variable decalriation.
labor_charge = 0.87
# print(type(labor_charge))

# -- Greeting message
greeting_msg = '\nWelcome to Complete Fiber Solution, Please answer ' \
               'followng questions to get a quote. '
print(greeting_msg)

usr_company_name = input("Enter Company Name : ")
# print("Company Name : ", usr_company_name)
# print(type(usr_company_name))

# -- Storing variable in float type.
fiber_install_feet = input(
    'Enter estimated fiber cable to be installed, in feets : ')
# print('Fiber Cable to be installed in feets :', float(fiber_install_feet))

# -- Total cost must be estimated fiber to be installed in feets into labor charge.
total_cost = round(float(fiber_install_feet) * labor_charge, 2)
# print('Total Change :', total_cost)


# -- Generating Final Report
print("\n\n#-------------------------------------------------------------#")
print("#--------------------  Estimated Quotes   --------------------#")
print("\t Company Name : ", usr_company_name.upper())
print("\t Fiber cable to be installed : ", fiber_install_feet)
print("\t Labor charge per sq. feet : ", labor_charge)
print("\t Total Cost : ", total_cost)

print("#--------------------------------------------------------------#")
