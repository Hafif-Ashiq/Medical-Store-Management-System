#Details of products
prd = list(range(10))
category = list(range(10))
manf = list(range(10))
com = list(range(10))
formula = list(range(10))
exp = list(range(10))

#Price and in stock number of medicines
in_stock = [45, 67, 43, 32, 12, 14, 34, 23, 36, 29]
price = [20, 22, 35, 17, 18, 34, 24, 27, 32, 13]

#Names of Product
prd[0] = "PANADOL"
prd[1] = "PARACETAMOL"
prd[2] = "ASPIRIN"
prd[3] = "BRUFEN"
prd[4] = "FLAGYL"
prd[5] = "ACETAMOL"
prd[6] = "AUGMENTIN"
prd[7] = "ATIVAN"
prd[8] = "FEFOL"
prd[9] = "CIPROFLAXICON"

#Category of Product
category[0] = "TABLET"
category[1] = "TABLET"
category[2] = "TABLET"
category[3] = "SYRUP"
category[4] = "TABLET"
category[5] = "SYRUP"
category[6] = "TABLET"
category[7] = "TABLET"
category[8] = "TABLET"
category[9] = "INJECTION"

# Company Name
com[0] = 'GLAXOSMITHKLINE'
com[1] = 'FLAGSHIP'
com[2] = 'RECKITTS & BENCKISER'
com[3] = 'ABOTT'
com[4] = 'PFIZER'
com[5] = 'GLAXOSMITHKLINE'
com[6] = 'SMPC'
com[7] = 'LORAZINE'
com[8] = 'FEFOL'
com[9] = 'CIPRO'

#Formula of Products
formula[0] = 'C8H9NO2'
formula[1] = 'C8H9NO2'
formula[2] = 'C9H8O4'
formula[3] = 'C13H18O2'
formula[4] = 'C6H9N3O3'
formula[5] = 'C3H6O'
formula[6] = 'C16H19N3O5S'
formula[7] = 'C15H10Cl2N2O2'
formula[8] = 'C19H19FeN7O10S'
formula[9] = 'C17H18FN3O3'

# Manufacture Date
manf[0] = "1 Jan,2021"
manf[1] = "21 May,2021"
manf[2] = "10 April,2021"
manf[3] = "31 Nov,2020"
manf[4] = "4 June,2021"
manf[5] = "29 April,2021"
manf[6] = "12 Feb,2021"
manf[7] = "17 Dec,2020"
manf[8] = "18 June,2021"
manf[9] = "7 March,2021"

#Expiry Date
exp[0] = '5 Dec,2021'
exp[1] = '15 Dec,2021'
exp[2] = '12 Nov,2021'
exp[3] = '31 Jan,2022'
exp[4] = '14 Aug,2021'
exp[5] = '17 Sep,2021'
exp[6] = '24 Oct,2021'
exp[7] = '19 Aug,2021'
exp[8] = '5 Feb,2022'
exp[9] = '15 Sep,2021'

#Start
x = 156

print("".center(x,"_"))
print("  MEDICAL STORE MANAGEMENT SYSTEM  ".center(x))

c_name = []
c_age = []
c_gender = []
c_id = []
paid_bill = []



n_o_m, f, c, a, m, e, ct, p = "Name of Medicine  ", "Formula  ", "Name of Company", "Amount in stock", "Manf.Date", "Expiry Date ", "Category", "Price"
b = (f'{n_o_m.ljust(len(n_o_m))} | {f.ljust(20)} | {c.ljust(25)} | {a} | {ct.ljust(15)} | {m.ljust(15)} | {e.ljust(15)} | {p} |')
def enter_b():
                print(b.center(x))
                print("_"*len(b))

                return 0

while True:
    print("".center(x, "_"))
    op = input("Enter S to sell medicine to customer;".title().center(x)+ "\n"+
               "Enter D to view price, details and availability of Products;".title().center(x)+" \n"+
               "Enter I to order medicine and add information or to remove any data;".center(x)+ "\n"+
               "Enter C to view Customer Details or to Search for a customer;".center(x)+ "\n"+
               "Enter E to exit:".center(x)+" \n".center(x))
    op = op.upper()
    print("-" * x)

# Exit the code
    if op == "E":
        print("  EXIT  ".center(x,"-"))
        print("".center(x,"-"))
        break
# Order medicine
    elif op == "S":
         print(" SELL MEDICINE TO CUSTOMER ".center(x,"-"))
         print("".center(x, "-"))

         cart = 0
         med = []
         num = []
         bil = []
         while True:

            name_of_prd = input("Enter the medicine you want to purchase:\n")
            name_of_prd = name_of_prd.upper()
            if prd.__contains__(name_of_prd):
                ind = prd.index(name_of_prd)
                amount = int(input("Enter the amount of Medicine required:\n"))
                if amount <= in_stock[ind]:
                    print("")
                    print("  Your order has been added to cart  ".center(x,"-"))
                    cart += 1
                    in_stock[ind] = in_stock[ind] - amount
                    med.append(name_of_prd)
                    num.append(amount)
                    bil.append(price[ind])
                    next_order = input("Enter 0 to exit this menu\n"
                                           "Otherwise, Enter anything to add more products: \n")
                else:
                    print("")
                    print(f"The stock is not available,as there are only  {in_stock[ind]} medicines remaining in stock.".center(x,"-"))
                    next_order = input("Enter 1 if you want to add anything else in cart\n"
                                           "Enter 2 if you want to change amount in same product\n"
                                           "Otherwise,Enter Anything to Exit this menu :\n")
                    if next_order != "1" or next_order != "2":
                        break
                    while next_order == "2":
                        print(f"The amount of Product in stock is {in_stock[ind]}")
                        amount = int(input("Enter the amount of Medicine required:\n"))
                        if amount <= in_stock[ind]:
                            print("")
                            print("  Your order has been added to cart.  ".center(x,"-"))
                            in_stock[ind] = in_stock[ind] - amount
                            cart += 1
                            med.append(name_of_prd)
                            num.append(amount)
                            bil.append(price[ind])
                            next_order = input("Enter 1 to add more Products to Cart\n"
                                                   "Press Enter anything  to proceed to bill:\n")
                            if next_order != "1":
                                break
                        else:
                            print("")
                            print(f"The stock is not available,as there are only {in_stock[ind]} medicines remaining in stock".title().center(x,"-"))
                            next_order = input("Enter 1 if you want to add anything else in cart\n"
                                                   "Enter 2 if you want to change amount in same product\n"
                                                   "Otherwise, Enter anything to Exit this menu:\n")
                            if next_order != "1":
                                break

            else:
                print("")
                print("  The desired Medicine is not available  ".title().center(x,"-"))
                next_order = input("Enter 0 to Exit: \n"
                                       "Enter anything else for new order: \n")
                                       
            if next_order == "0":
                break

         if cart >= 1:
    
             while True:                  #Name of Customer
                 name = input("Enter the First name of Customer:".center(x)+" \n".center(x-1))
                 if name.isalpha():

                     while True:
                         name2 = input("Enter the Second name of Customer:".center(x) + "\n".center(x-2))
                         if name2.isalpha():
                             break
                     name = name + " " + name2
                     name = name.upper()
                     c_name.append(name)
                     break

             while True:              #Age of Customer
                 age = input("Enter the age of the Customer:".center(x)+" \n".center(x-2))
                 if age.isdigit():
                     age = int(age)
                     c_age.append(age)
                     break

             while True:             #Gender of Customer
                 gender = input("Enter the Gender of Customer as M or F:".center(x)+" \n".center(x-2))
                 gender = gender.upper()
                 if gender == "M" or gender == "F":
                     c_gender.append(gender)
                     break


             while True:               #CNIC of customer
                 id = input("Enter the 13 digit ID of the customer as on CNIC:".center(x)+" \n".center(x-7))
                 if len(id) ==13 and id.isdigit():
                     c_id.append(id)
                     break

             # bill generation
             print("".center(x,"_"))
             t_rs = 0
             print("  Medical Store  ".center(x,"-"))
             print(f"ID     : {id}\nName   : {name}\nAge    : {age}\nGender : {gender}")
             print("| NAME OF MEDICINE     | AMOUNT  | PRICE  |".center(x))
             print(("-"*43).center(x))
             for i in range(cart):
                 print(f'| {med[i].ljust(20)} | {str(num[i]).ljust(7)} | {str(bil[i]).ljust(6)} |'.center(x))
                 t_rs = t_rs + (num[i] * bil[i])
                 
             paid_bill.append(t_rs)
             print(" ")
             print("Total bill : ", t_rs, "Rs.")
             t = "  Thanks For Coming  "
             print(t.center(x,"-"))

    #Details of available medicines
    elif op == "D":
        print("  DETAILS OF MEDICINES  ".center(x,"-"))
        print("".center(x,"-"))

        det = input("Enter 1 to view all Details of available medicine\n"
                    "Enter 2 to Search for the specific medicine: \n"
                    "Enter 0 to Exit: \n")

        if det == "1":
            b = (f'Sr. # | {n_o_m.ljust(len(n_o_m))} | {f.ljust(20)} | {c.ljust(22)} | {a} | {ct.ljust(15)} | {m.ljust(15)} | {e.ljust(15)} | {p} |')
            print("".center(x,"_"))
            print(b.center(x))
            print("_"*len(b))
            
            for j in range(len(prd)):
                print(f'{str(j + 1).ljust(5)} | '
                      f'{prd[j].ljust(len(n_o_m))} | '
                      f'{formula[j].ljust(20)} | '
                      f'{com[j].ljust(22)} | '
                      f'{str(in_stock[j]).center(len(a))} | '
                      f'{category[j].ljust(15)} | '
                      f'{manf[j].ljust(15)} | '
                      f'{exp[j].ljust(15)} | '
                      f'{str(price[j]).ljust(5)} |'.center(x))
            print("".center(x,"_"))


        elif det == "2":   #For Details and information
            while True:
                type_search = input("\nEnter N to search by Name\n"
                                    "Enter C to search by company\n"
                                    "Enter T to search by Category : \n"
                                    "Enter 0 to exit: \n")
                if type_search == "N":
                    search = input("Enter the name of Product you want to search : \n")
                    search = search.upper()
                    if prd.__contains__(search):
                        ind = prd.index(search)
                        print("".center(x, "_"))
                        print(f"Name of Medicine : {prd[ind]}\n"
                              f"Formula = {formula[ind]}\n"
                              f"Name of company : {com[ind]}\n"
                              f"Manfucature Date : {manf[ind]}\n"
                              f"Expiry Date : {exp[ind]}\n"
                              f"Amount of Product Available : {in_stock[ind]}\n"
                              f"Price : {price[ind]}")
                        print("".center(x, "_"))
                    else:
                        print("  The Medicine You Entered Is Not Available  ".center(x,"-"))
                        enter_b()

                elif type_search == "C":                #To search by company
                    search = input("Enter the name of Company whose medicine you want to search: \n")
                    search = search.upper()
                    if com.__contains__(search):
                        l = []
                        ind = 0
                        for i in com:
                            if i == search:
                                l.append(ind)
                            ind += 1
                        enter_b()
                        for j in l:
                            print(f'{prd[j].ljust(len(n_o_m))} | '
                                  f'{formula[j].ljust(20)} | '
                                  f'{com[j].ljust(25)} | '
                                  f'{str(in_stock[j]).center(len(a))} | '
                                  f'{category[j].ljust(15)} | '
                                  f'{manf[j].ljust(15)} | '
                                  f'{exp[j].ljust(15)} | '
                                  f'{str(price[j]).ljust(5)} |'.center(x))
                    else:
                        print()
                        print("  There is no medicine from the Name of company you Enter  ".title().center(x,"-"))
                        enter_b()

                elif type_search == "T":                      #For Search by Category
                    search = input("Enter the Category of Product you want to search: \n"
                                   "Enter T for Tablets: \n"
                                   "Enter S for Syrup \n"
                                   "Enter I for injection \n"
                                   "Else Enter the name of Category: \n")

                    if search == "T":                      #For Tablets
                        l = []
                        ind = 0
                        for i in category:
                            if i == "TABLET":
                                l.append(ind)
                            ind += 1
                        enter_b()
                        for j in l:
                            print(f'{prd[j].ljust(len(n_o_m))} | '
                                  f'{formula[j].ljust(20)} | '
                                  f'{com[j].ljust(25)} | '
                                  f'{str(in_stock[j]).center(len(a))} | '
                                  f'{category[j].ljust(15)} | '
                                  f'{manf[j].ljust(15)} | '
                                  f'{exp[j].ljust(15)} | '
                                  f'{str(price[j]).ljust(5)} |'.center(x))
                    elif search == "S":                             #For Syrup
                        l = []
                        ind = 0
                        for i in category:
                            if i == "SYRUP":
                                l.append(ind)
                            ind += 1
                        enter_b()
                        for j in l:
                            print(f'{prd[j].ljust(len(n_o_m))} | '
                                  f'{formula[j].ljust(20)} | '
                                  f'{com[j].ljust(25)} | '
                                  f'{str(in_stock[j]).center(len(a))} | '
                                  f'{category[j].ljust(15)} | '
                                  f'{manf[j].ljust(15)} | '
                                  f'{exp[j].ljust(15)} | '
                                  f'{str(price[j]).ljust(5)} |'.center(x))
                    elif search == "I":                            #For Injections
                        l = []
                        ind = 0
                        for i in category:
                            if i == "INJECTION":
                                l.append(ind)
                            ind += 1
                        enter_b()
                        for j in l:
                            print(f'{prd[j].ljust(len(n_o_m))} | '
                                  f'{formula[j].ljust(20)} | '
                                  f'{com[j].ljust(25)} | '
                                  f'{str(in_stock[j]).center(len(a))} | '
                                  f'{category[j].ljust(15)} | '
                                  f'{manf[j].ljust(15)} | '
                                  f'{exp[j].ljust(15)} | '
                                  f'{str(price[j]).ljust(5)} |'.center(x))
                    else:                                              #For other categories
                        search = search.upper()
                        if category.__contains__(search):
                            l = []
                            ind = 0
                            for i in category:
                                if i == search:
                                    l.append(ind)
                                ind += 1
                            enter_b()
                            for j in l:
                                print(f'{prd[j].ljust(len(n_o_m))} | '
                                      f'{formula[j].ljust(20)} | '
                                      f'{com[j].ljust(25)} | '
                                      f'{str(in_stock[j]).center(len(a))} | '
                                      f'{category[j].ljust(15)} | '
                                      f'{manf[j].ljust(15)} | '
                                      f'{exp[j].ljust(15)} | '
                                      f'{str(price[j]).ljust(5)} |'.center(x))
                        else:
                            print("")
                            print("  The category you entered in unavailable.  ".title().center(x,"-"))
                elif type_search == "0":
                    break

# Order medicine or add or remove information
    elif op == "I":
        print("  ADD OR REMOVE INFORMATION  ".center(x,"-"))
        print("".center(x,"-"))


        type_change = input("Enter 1 to order medicine from Company and add information\n"
                            "Enter 2 to remove information \n"
                            "Otherwise enter anything  to Exit this function: \n")


        if type_change == "1":  # Order from company or add information
            while True:
                name_med = input("Enter the name of Medicine: \n")
                name_med = name_med.upper()
                if prd.__contains__(name_med):
                    ind = prd.index(name_med)
                    print("This Medicine is already in our record".title().center(x,"-"))
                    app = input("Enter 1 to update its quantity \n"
                                "Else Enter Anything to quit this menu: \n")
                    if app == "1":
                        while True:
                            amount = input("Enter the amount you want to add for this medicine: \n")
                            if amount.isdigit():
                                amount = int(amount)
                                break
                        in_stock[ind] = amount

                else:
                    prd.append(name_med)
    
                    formula_med = input("Enter the formula of Medicine: \n")
                    formula.append(formula_med)
    
                    name_com = input("Enter the name of Company: \n")
                    name_com = name_com.upper()
                    com.append(name_com)
    
                    cat_med = input("Enter T if Tablet \n"
                                    "Enter S if Syrup \n"
                                    "Enter I if injection\n"
                                    "Enter name of category  if any other: \n")
                    if cat_med == "T":
                        category.append("TABLET")
                    elif cat_med == "S":
                        category.append("SYRUP")
                    elif cat_med == "I":
                        category.append("INJECTION")
                    else:
                        cat_med = cat_med.upper()
                        category.append(cat_med)
    
                    amo = int(input("Enter the amount of Medicine: \n"))
                    in_stock.append(amo)
    
                    price_med = int(input("Enter the price of Medicine: \n"))
                    price.append(price_med)
    
                    manf_med = input("Enter the manufacture Date: \n")
                    manf.append(manf_med)
    
                    exp_med = input("Enter the expiry date: \n")
                    exp.append(exp_med)

                next = input("Enter + to add next medicine \n"
                             "Else enter blank space: \n")
                if next != "+":
                     break

        elif type_change == "2":

            remov = "1"
            while remov == "1":
                remove = input("Enter the name of product you want to remove: \n")
                remove = remove.upper()

                if prd.__contains__(remove):
                    ind = prd.index(remove)
                    print("")
                    enter_b()
                    print(f'{prd[ind].ljust(len(n_o_m))} | '
                          f'{formula[ind].ljust(20)} | '
                          f'{com[ind].ljust(25)} | '
                          f'{str(in_stock[ind]).center(len(a))} | '
                          f'{category[ind].ljust(15)} | '
                          f'{manf[ind].ljust(15)} | '
                          f'{exp[ind].ljust(15)} | '
                          f'{str(price[ind]).ljust(5)} |'.center(x))
                    print("")
                    confirm = input("Enter C if you want to remove it \n"
                                    "Otherwise enter anything: \n")
                    if confirm == "C":
                        prd.pop(ind)
                        formula.pop(ind)
                        com.pop(ind)
                        in_stock.pop(ind)
                        category.pop(ind)
                        manf.pop(ind)
                        exp.pop(ind)
                        price.pop(ind)
                        print("  The medicine is removed from the data  ".title().center(x,"-"))
                    else:
                        print("  The request of removal has been cancelled  ".title().center(x))
                else:
                    print("The medicine you entered can not be found in the data".title().center(x,"-"))
                remov = input("Enter 1 to remove anything else \n"
                              "Enter 0 to exit this function: \n")

#View Customer information and search by name or ID
    elif op == "C":
        print("  CUSTOMER INFORMATION  ".center(x,"-"))
        print("".center(x,"-"))
        type_search = input("Enter D to view Details of all customers \n"
                            "Enter S to search for specific customer: \n"
                            "Enter E to exit: \n")
        type_search = type_search.upper()

        if type_search == 'D':
            print(" DETAILS OF ALL CUSTOMERS ".center(x,"-"))
            print("| ID              | "
                  "NAME OF CUSTOMER         | "
                  "AGE    | "
                  "GENDER |"
                  "PAID BILL|".center(x))
            print(("_"*72).center(x))
            for i in range(len(c_id)):
                print(f"| {c_id[i].ljust(15)} | "
                      f"{c_name[i].ljust(24)} | "
                      f"{str(c_age[i]).ljust(6)} | "
                      f"{c_gender[i].ljust(6)} | "
                      f"{str(paid_bill[i]).ljust(6)}Rs|".center(x))
        
        elif type_search == "S":
            print(" DETAILS BY SEARCH ".center(x,'-'))
            while True:
                search = input("Enter N to Search by name \n"
                               "Enter I to Search by ID \n"
                               "Enter E to exit this function: \n")
                search = search.upper()

                if search == "N":
                    
                    sear = input("Enter the first name of customer: \n")
                    sear2 = input("Enter second name of customer: \n")
                    nam = sear + " " + sear2
                    nam = nam.upper()

                    if c_name.__contains__(nam):
                        ind = c_name.index(nam)
                        print("".center(x,"_"))
                        print("ID              | "
                              "NAME OF CUSTOMER         | "
                              "AGE    | "
                              "GENDER |"
                              "PAID BILL|".center(x))
                        print(("_" * 72).center(x))
                        print(f"{c_id[ind].ljust(14)} | "
                              f"{c_name[ind].ljust(24)} | "
                              f"{str(c_age[ind]).ljust(6)} | "
                              f"{c_gender[ind].ljust(6)} | "
                              f"{str(paid_bill[ind]).ljust(6)}Rs |".center(x))
                        print("".center(136,"_"))
                    else:
                        print("  The name you entered does not match any data entry  ".center(x,"-"))

                elif search == "I":
                    
                    while True:
                        sear = input("Enter 13 digit CNIC number of the Customer: \n"
                                     "Enter 0 if you want to cancel the search: \n")
                        if len(sear) == 13:
                            if sear.isdigit():
                                break
                        elif sear == "0":
                            break

                    if sear == "0":
                        break

                    elif c_id.__contains__(sear):
                        print("".center(x,"_"))
                        ind = c_id.index(sear)
                        print("ID              | "
                              "NAME OF CUSTOMER         | "
                              "AGE    | "
                              "GENDER |"
                              "PAID BILL|".center(x))
                        print(("_" * 72).center(x))
                        print(f"{c_id[ind].ljust(14)} | "
                              f"{c_name[ind].ljust(24)} | "
                              f"{str(c_age[ind]).ljust(6)} | "
                              f"{c_gender[ind].ljust(6)} | "
                              f"{str(paid_bill[ind]).ljust(6)}Rs |".center(x))
                        print("".center(x,"_"))

                    else:
                        print("  The CNIC you entered doesn't match our any record.  ".center(x,"-"))

                elif search == "E":
                    break

#_________________________________________________  END  _____________________________________________