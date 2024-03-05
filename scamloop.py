from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time

i = 0

while i<10:

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Open the website
    driver.get("http://viewcreditscore.info/")
    driver.maximize_window()

    # Function to generate a random string of lowercase letters
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    # Function to generate a random 10-digit integer
    def generate_random_number():
        return ''.join(random.choices(string.digits, k=10))


    # Find the input fields
    fname_input = driver.find_element(By.NAME,"StepOneBE02VM.FirstName")
    lname_input = driver.find_element(By.NAME,"StepOneBE02VM.LastName")
    email_input = driver.find_element(By.NAME,"StepOneBE02VM.Email")
    pnumber_input = driver.find_element(By.NAME,"StepOneBE02VM.PhoneNumber")

    # Generate random data
    random_fname = generate_random_string(random.randint(3, 10))
    random_lname = generate_random_string(random.randint(3, 10))
    random_email = f"{random_fname.lower()}{random_lname.lower()}@gmail.com"
    random_pnumber = generate_random_number()

    # Fill the form fields with generated data
    fname_input.send_keys(random_fname)
    lname_input.send_keys(random_lname)
    email_input.send_keys(random_email)
    pnumber_input.send_keys(random_pnumber)

    time.sleep(10)

    # Submit the first page
    next_button = driver.find_element(By.XPATH,'//*[@id="mainForm"]/div/div/div/div[1]/div[2]/button[2]')
    next_button.click()

    # Second Page
    time.sleep(4)
    manual_address = driver.find_element(By.CLASS_NAME,'showManual')
    manual_address.click()

    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


    street_address_input = driver.find_element(By.XPATH,'//*[@id="StepTwoBE02VM_Addresses_0__StreetAddress"]')
    apartment_unit_input = driver.find_element(By.XPATH,'//*[@id="StepTwoBE02VM_Addresses_0__UnitNumber"]')
    city_address_input = driver.find_element(By.XPATH,'//*[@id="StepTwoBE02VM_Addresses_0__City"]')
    province_dropdown = Select(driver.find_element(By.XPATH,'//*[@id="StepTwoBE02VM_Addresses_0__Province"]'))
    postal_code_input = driver.find_element(By.XPATH,'//*[@id="StepTwoBE02VM_Addresses_0__PostalCode"]')

    random_street_address = generate_random_string(random.randint(5, 15)) + " " + str(random.randint(1, 100))
    random_apartment_unit = str(random.randint(10, 999))
    random_city = random.choice(["Halifax", "Dartmouth", "Sydney", "Glace Bay", "Truro", "New Glasgow", "Sydney Mines",
                                "Kentville", "New Waterford", "Amherst", "Bridgewater", "Yarmouth", "North Sydney",
                                "Greenwood", "Antigonish"])
    random_province = "NS"
    random_postal_code = ''.join(random.choices(string.ascii_uppercase, k=1)) + \
                        ''.join(random.choices(string.digits, k=1)) + \
                        ''.join(random.choices(string.ascii_uppercase, k=1)) + " " + \
                        ''.join(random.choices(string.digits, k=1)) + \
                        ''.join(random.choices(string.ascii_uppercase, k=1)) + \
                        ''.join(random.choices(string.digits, k=1))

    # Fill the form fields with generated data
    street_address_input.send_keys(random_street_address)
    apartment_unit_input.send_keys(random_apartment_unit)
    city_address_input.send_keys(random_city)
    province_dropdown.select_by_visible_text(random_province)
    postal_code_input.send_keys(random_postal_code)
    been_here = driver.find_element(By.XPATH,'//*[@id="livedSixMonths_true"]').click()
    time.sleep(10)
    
    # Submit the second  page
    next2_button = driver.find_element(By.XPATH,'//*[@id="mainForm"]/div/div/div/div[1]/div[2]/button[2]')
    next2_button.click()


    # Third Page
    time.sleep(4)
    #Click cc/dc radio button to enable further
    ccDc = driver.find_element(By.XPATH,'//*[@id="payment-option-cc"]').click()

    # Function to generate a 16-digit credit card number starting with 5272 (5272 = MasterCard, replace with whatever you like)

    #Here we are using Luhn Algorith to generate a valid credit card
    def generate_credit_card():
        # Generate the first digit (4)
        first_digit = "4"
        card_number = first_digit

        # Generate the remaining 15 digits
        for _ in range(15):
            card_number += str(random.randint(0, 9))
            
        return card_number

    def luhn_check(card_number):
        # Reverse the card number
        reversed_card_number = card_number[::-1]
        
        total = 0
        for i, digit in enumerate(reversed_card_number):
            num = int(digit)
            if i % 2 == 1:
                num *= 2
                if num > 9:
                    num -= 9
            total += num
        
        return total % 10 == 0

    # Function to generate a valid random credit card number
    def generate_valid_credit_card():
        valid_credit_card = None
        while not valid_credit_card:
            random_card_number = generate_credit_card()
            if luhn_check(random_card_number):
                valid_credit_card = random_card_number
        return valid_credit_card

    # Generate and print a valid random credit card number
    valid_credit_card_number = generate_valid_credit_card()

    # Function to generate a 3-digit CVV number
    def generate_cvv():
        return ''.join(random.choices("0123456789", k=3))

    # Function to generate a random 2-digit number for month (01 to 12)
    def generate_month():
        return str(random.randint(1, 12)).zfill(2)

    # Function to generate a random 2-digit number for year (24 to 29)
    def generate_year():
        return str(random.randint(24, 29)).zfill(2)

    #Find the input fields
    ccDc_input = driver.find_element(By.XPATH,'//*[@id="StepThreeBE02VM_CheckoutVM_CreditCardMinimalVM_CCNumber"]')
    cvv_input = driver.find_element(By.XPATH,'//*[@id="StepThreeBE02VM_CheckoutVM_CreditCardMinimalVM_CVC"]')
    yy_input = driver.find_element(By.XPATH,'//*[@id="StepThreeBE02VM_CheckoutVM_CreditCardMinimalVM_ExpirationYear"]')
    mm_input = driver.find_element(By.XPATH,'//*[@id="StepThreeBE02VM_CheckoutVM_CreditCardMinimalVM_ExpirationMonth"]')

    time.sleep(9)

    # Generate random data
    random_credit_card = valid_credit_card_number
    random_cvv = generate_cvv()
    random_mm = generate_month()
    random_yy = generate_year()

    # Fill the form with generated data

    for char in random_credit_card:
        ccDc_input.send_keys(char)
        time.sleep(0.1)

    for char in random_cvv:
        cvv_input.send_keys(char)
        time.sleep(0.1)

    for char in random_mm:
        mm_input.send_keys(char)
        time.sleep(0.1)

    for char in random_yy:
        yy_input.send_keys(char)
        time.sleep(0.1)

    #ccDc_input.send_keys(random_credit_card)
    #cvv_input.send_keys(random_cvv)
    #mm_input.send_keys(random_mm)
    #yy_input.send_keys(random_yy)
    time.sleep(10)
    # Final Submut
    agree = driver.find_element(By.XPATH,'//*[@id="mainForm"]/div[2]/div/div/div[1]/div/div/div/div[3]/div/button')
    agree.click()
    time.sleep(10)

    # Close the browser window
    driver.quit()
    
    i+=1
