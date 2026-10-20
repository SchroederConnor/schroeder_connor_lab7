import subprocess
import sys
import re
import os
import difflib

# -----------------------------
# Remove comments + clean code
# -----------------------------
def remove_comments_space(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Remove all whitespace (spaces, tabs, newlines, etc.)
    text = "".join(text.split())
    return text


def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# -----------------------
# File Checks
# -----------------------

REQUIRED_FILES = [
        "restaurant.h",
        "restaurant.cpp",
        "menuItem.h",
        "menuItem.cpp",
        "main.cpp",
        "Output.txt",
        "customer.h",
        "customer.cpp",
        "waitingLine.h",
        "waitingLine.cpp"
    ]
EXEC = "./restaurant"
# -----------------------------
# Check required files
# -----------------------------
def check_files():
    print("Checking required files...")
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True


# -----------------------------
# Check menuItem.h file
# -----------------------------
def check_menuItem_header():
    print("Checking menuItem.h...")
    with open("menuItem.h") as f:
        header = remove_comments_space(f.read())
    
    
    if "MenuItemoperator+(constMenuItem&)" not in header:
        print("Missing: MenuItem operator+(const MenuItem&)")
        return False
    
    if "friendostream&operator<<(ostream&,constMenuItem&)" not in header:
        print("Missing: friend ostream& operator<<(ostream&,const MenuItem&)")
        return False
    
    if "displayMenuItemData" in header:
        print("Remove: displayMenuItemData method declaration")
        return False

    return True


# -----------------------------
# Check menuItem.cpp file
# -----------------------------
def check_menuItem_cpp():
    print("Checking menuItem.cpp...")
    with open("menuItem.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "MenuItemMenuItem::operator+(constMenuItem&" not in cpp:
        print("Missing: MenuItem MenuItem::operator+(const MenuItem&)")
        return False
    
    if "ostream&operator<<(ostream&" not in cpp:
        print("Missing: friend ostream& operator<<(ostream&,const MenuItem&)")
        return False
    
    if "displayMenuItemData" in cpp:
        print("Remove: displayMenuItemData method")
        return False

    return True
 
    
   
# -----------------------------
# Check restaurant.h file
# -----------------------------
def check_restaurant_header():
    print("Checking restaurant.h...")
    with open("restaurant.h") as f:
        header = remove_comments_space(f.read())

    if "voidoperator+(constMenuItem&)" not in header:
        print("Missing: void operator+(const MenuItem&)")
        return False
    
    if "Restaurant&operator=(constRestaurant&)" not in header:
        print("Missing: Restaurant& operator = (const Restaurant&)")
        return False
    
    if "friendostream&operator<<(ostream&,constRestaurant&)" not in header:
        print("Missing: friend ostream& operator<<(ostream&, const Restaurant&)")
        return False
    
    if "displayRestaurantData" in header:
        print("Remove: displayRestaurantData method declaration")
        return False
    
    if "maxItem" not in header:
        print("Missing: maxItem variable declaration")
        return False
    
    
    if "MenuItem*items" not in header:
        print("Missing: MenuItem* items declaration")
        return False
    if "MenuItem*getItems()" not in header:
        print("Missing: MenuItem* getItems()")
        return False
    if "~Restaurant()" not in header:
        print("Missing: ~Restaurant() Destructor")
        return False

    return True

    



# -----------------------------
# Check restaurant.cpp file
# -----------------------------
def check_restaurant_cpp():
    print("Checking restaurant.cpp...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "voidRestaurant::operator+(constMenuItem&" not in cpp:
        print("Missing: void Restaurant::operator+(const MenuItem&)")
        return False
    
    if "Restaurant&Restaurant::operator=(constRestaurant&" not in cpp:
        print("Missing: Restaurant& Restaurant::operator = (const Restaurant&)")
        return False
    
    if "ostream&operator<<(ostream&" not in cpp:
        print("Missing: ostream& operator<<(ostream&, const Restaurant&)")
        return False
    
    if "displayRestaurantData" in cpp:
        print("Remove: displayRestaurantData method")
        return False
    
    
    if "MenuItem*Restaurant::getItems" not in cpp:
        print("Missing: MenuItem* MenuItem::getItems")
        return False
    if "Restaurant::~Restaurant()" not in cpp:
        print("Missing: Restaurant::~Restaurant() Destructor")
        return False
    if "maxItem=5" not in cpp:
        print("maxItem needs to be initialized with 5 in the default constructor")
        return False
    
    if cpp.count("newMenuItem") <5:
        print("There should be at least 5 dynamic allocation of MenuItem array using new keyword in the cpp file.")
        return False
    if cpp.count("delete[]items") <3:
        print("Missing: delete [] items check 1) destructor, 2)in the assignment operator overload and 3)add method")
        return False
    return True
    
 
# -----------------------------
# Check customer.h file
# -----------------------------
def check_customer_header():
    print("Checking customer.h...")
    with open("customer.h") as f:
        header = remove_comments_space(f.read())
    if "Customer*next" not in header:
        print("Missing: Customer* next declaration")
        return False
    if "Customer*getNext()" not in header:
        print("Missing: Customer* getNext()")
        return False
    if "voidsetNext(Customer*)" not in header:
        print("Missing: void setNext(Customer*)")
        return False
    if "Customer&operator=(constCustomer&)" not in header:
        print("Missing: Customer& operator = (const Customer&)")
        return False
    
    if "friendostream&operator<<(ostream&,constCustomer&)" not in header:
        print("Missing: friend ostream& operator<<(ostream&, const Customer&)")
        return False
    
    if "~Customer()" not in header:
        print("Missing: ~Customer() Destructor")
        return False

    return True

# -----------------------------
# Check customer.cpp file
# -----------------------------
def check_customer_cpp():
    print("Checking customer.cpp...")
    with open("customer.cpp") as f:
        cpp = remove_comments_space(f.read())

   
    
    if "Customer&Customer::operator=(constCustomer&" not in cpp:
        print("Missing: Customer& Customer::operator = (const Customer&)")
        return False
    
    if "ostream&operator<<(ostream&" not in cpp:
        print("Missing: ostream& operator<<(ostream&, const Customer&)")
        return False
    
    
    if "Customer*Customer::getNext" not in cpp:
        print("Missing: Customer* Customer::getNext")
        return False
    
    if "voidCustomer::setNext" not in cpp:
        print("Missing: void Customer::setNext")
        return False
    if "Customer::~Customer()" not in cpp:
        print("Missing: Customer::~Customer() Destructor")
        return False
    
   
    return True  

# -----------------------------
# Check waitingLine.h file
# -----------------------------
def check_waitingLine_header():
    print("Checking waitingLine.h...")
    with open("waitingLine.h") as f:
        header = remove_comments_space(f.read())

    if "*first" not in header and "*last" not in header:
        print("Missing: Missing *first or *last pointer declaration")
        return False
    if "Customer*getFirst()" not in header:
        print("Missing: Customer* getFirst()")
        return False
    if "Customer*getLast()" not in header:
        print("Missing: Customer* getLast()")
        return False
    if "voidsetFirst(Customer*)" not in header:
        print("Missing: void setFirst(Customer*)")
        return False
    if "voidsetLast(Customer*)" not in header:
        print("Missing: void setLast(Customer*)")
        return False
    
    if "boolcheckCustomer(Customer&)" not in header:
        print("Missing: bool checkCustomer(Customer&)")
        return False
    if "voidaddCustomer(Customer" not in header:
        print("Missing: void addCustomer(Customer&)")
        return False
    if "voidremoveCustomer()" not in header:
        print("Missing: void removeCustomer()")
        return False
    if "WaitingLine&operator=(constWaitingLine&)" not in header:
        print("Missing: WaitingLine& operator = (const WaitingLine&)")
        return False
    
    if "friendostream&operator<<(ostream&,constWaitingLine&)" not in header:
        print("Missing: friend ostream& operator<<(ostream&, const WaitingLine&)")
        return False
    
    if "~WaitingLine()" not in header:
        print("Missing: ~WaitingLine() Destructor")
        return False

    return True


# -----------------------------
# Check waitingLine.cpp file
# -----------------------------
def check_waitingLine_cpp():
    print("Checking waitingLine.cpp...")
    with open("waitingLine.cpp") as f:
        cpp = remove_comments_space(f.read())

   
    
    if "WaitingLine&WaitingLine::operator=(constWaitingLine&" not in cpp:
        print("Missing: WaitingLine& WaitingLine::operator = (const WaitingLine&)")
        return False
    
    if "ostream&operator<<(ostream&" not in cpp:
        print("Missing: ostream& operator<<(ostream&, const WaitingLine&)")
        return False
    
    
    if "Customer*WaitingLine::getFirst" not in cpp:
        print("Missing: Customer* WaitingLine::getFirst")
        return False
    
    if "voidWaitingLine::setFirst" not in cpp:
        print("Missing: void WaitingLine::setFirst")
        return False
    
    if "Customer*WaitingLine::getLast" not in cpp:
        print("Missing: Customer* WaitingLine::getLast")
        return False
    
    if "voidWaitingLine::setLast" not in cpp:
        print("Missing: void WaitingLine::setLast")
        return False
    
    if "voidWaitingLine::addCustomer" not in cpp:
        print("Missing: void WaitingLine::addCustomer")
        return False
    if "voidWaitingLine::removeCustomer" not in cpp:
        print("Missing: void WaitingLine::removeCustomer")
        return False
    if "WaitingLine::~WaitingLine()" not in cpp:
        print("Missing: WaitingLine::~WaitingLine() Destructor")
        return False
    if cpp.count("newCustomer") <7:
        print("There should be at least 7 dynamic allocation of Customer object using new keyword in the cpp file.")
        print("2 in Parameterized Constructor, 2 in Copy Constructor, 2 in assignment operator overload, 1 in addCustomer method")
        return False
   
    if cpp.count("delete") <2:
        print("delete keyword is not in use to deallocate memory either in destructor or removeCustomer method.")
        return False
   
    return True 
# -----------------------
# addItem capacity check
# -----------------------
def addItem_check():
    print("Checking addItem method...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments_space(f.read())
    if "Limit exceeded!" not in cpp:
        print("Missing overflow error message in addItem()")
        return False
    return True

# -----------------------------
# Check main file
# -----------------------------
def check_main():
    print("Checking main.cpp...")

    with open("main.cpp", "r") as f:
        content = remove_comments_space(f.read())

    check = [
        
        "displayRestaurantData",
        "addItem",
        "[",
        "]"
    ]

   

    found = [r for r in check if r in content]

    if  found:
        
        for m in found:
            print("Remove:", m)
        
        return False
    
    if content.count("newCustomer") <4:
        print("There should be 4 dynamic allocation of Customer object using new keyword in the main.cpp.")
        return False
    
    if content.count("addCustomer") != 2:
        print("Customer will be added only 2 times using the addCustomer method")
        return False
    return True 


# -----------------------------
# Build project
# -----------------------------
def build():
    print("Building project...")

    result = subprocess.run(["make"], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Build failed:\n")
        print(result.stderr)
        return False 
    return True


# -----------------------------
# Run program
# -----------------------------
def run_program():
    print("Running program...")

    if not os.path.exists(EXEC):
        print(" Executable not found")
        sys.exit(1)

    result = subprocess.run([EXEC], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Program crashed")
        print(result.stderr)
        sys.exit(1)

    print("Program output captured.")
    return result.stdout.strip()


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = os.path.exists(EXEC)
        # if not os.path.exists(EXEC):
            
        #     sys.exit(1)
        print ("Checking make clean...")

        if exe_files:
            print("Executable restaurant is not removed.")
            return False 

        if obj_files:
            print("Not all the .o files are removed.")
            return False

        return True

    except Exception:
        return False


# -----------------------------
# Load expected output
# -----------------------------
def load_expected():
    with open("Output.txt", "r") as f:
        return f.read().strip()


# -----------------------------
# Compare outputs
# -----------------------------
def compare_output():
    print("Comparing output with Output.txt...")

    actual = run_program()
    expected = load_expected()

    if actual == expected:
        print("Output matches exactly!")
        return True
    print("Output does NOT match!\nCheck output.txt")
    
# print(" Output does NOT match!\n")

    diff = difflib.unified_diff(
    expected.splitlines(),
    actual.splitlines(),
    fromfile="Expected (Output.txt)",
    tofile="Actual (Program Output)",
    lineterm=""
    )

    print("Difference Report:")
    print("  --- : Expected output")
    print("  +++ : Your program output")
    print("  -   : Line missing or incorrect in your output")
    print("  +   : Line produced by your program that differs from expected")
    print("      : Lines without a symbol match in both outputs")
    print()

    for line in diff:
        if line.startswith("@@"):
            continue
        print(line)
    return False

# -----------------------------
# Main
# -----------------------------
def main():
    total = 0
    passed = 0

    

    tests = [
        ("Required Files Exist", check_files),
        ("MenuItem Header Declarations", check_menuItem_header),
        ("MenuItem CPP Implementations", check_menuItem_cpp),
        ("Restaurant Header Declarations", check_restaurant_header),
        ("Restaurant CPP Implementations", check_restaurant_cpp),
        ("Customer Header Declarations", check_customer_header),
        ("Customer CPP Implementations", check_customer_cpp),
        ("WaitingLine Header Declarations", check_waitingLine_header),
        ("WaitingLine CPP Implementations", check_waitingLine_cpp),
        
        ("main.cpp Structure", check_main),
        ("Makefile Builds", build),
        ("Executable Created and Output Matching", compare_output),
        ("Make Clean Works", check_make_clean),
        
        
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)
   


if __name__ == "__main__":
    main()