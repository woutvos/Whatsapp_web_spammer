from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Define some stuff
browser  = webdriver.Chrome(ChromeDriverManager().install())
platform = input("What platform do you want to use? Instagram or WhatsApp: ").lower()

# Choose to use Instagram or WhatsApp

# WhatsApp
if platform == "whatsapp":

    # Start the browser and go to the site
    browser.get('https://web.whatsapp.com')

    # Check if the user is ready
    while True:
        if input("If you have scanned the qr code type 'go ahead'. ") == "go ahead":
            break

    # Define "send()"
    def send(instagram):
        # Choose the person
        browser.find_element_by_css_selector("span[title='" + input("Enter the name or group to spam: ") + "']").click()

        # Enter the message
        inputString = input("Enter message to send: ")
        print("Started spamming! If you want to stop it press Ctrl+C.")

        # Send the messages
        try:
            while True:
                browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
                browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

        except KeyboardInterrupt:
            print("Stopped spamming...")
            pass

    # Send the messages
    while True:
        send("instagram")

# Instagram
elif platform == "instagram":

    # Open instagram
    browser.get("https://www.instagram.com/direct/t/340282366841710300949128178718937873934")

    # Accept the cookies
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()

    # Login with the account
    print("Logging in")
    time.sleep(5)
    browser.find_element_by_name("username").send_keys(input("Username: "))
    browser.find_element_by_name("password").send_keys(input("Password: "))
    browser.find_element_by_xpath("//button[@type='submit']").click()
    print("Logged in")

    # Choose to not save the credentials
    time.sleep(10)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    print("Choosed to not save the credentials")

    # Choose to not get notifications
    time.sleep(2)
    browser.find_element_by_xpath("html/body/div[4]/div/div/div/div[3]/button[2]").click()
    print("Clicked the 'Not now' button")
