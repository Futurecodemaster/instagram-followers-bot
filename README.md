# instagram-followers-bot
This is a script that automates the process of following followers of a similar Instagram account.
1.	Imports necessary modules:
  •	webdriver from selenium to interact with the web browser
  •	By from selenium.webdriver.common to locate elements on the page
  •	expected_conditions from selenium.webdriver.support to wait for elements to be clickable
  •	WebDriverWait from selenium.webdriver.support.ui to wait for elements to be clickable
  •	time to add delays in the script


2.	Defines constants:
  •	DRIVER_PATH is the path to the Chrome driver executable
  •	SIMILAR_ACCOUNT is the name of the similar Instagram account
  •	USERNAME and PASSWORD are the credentials to log in to Instagram


3.	Defines a helper function wait_until_clickable that waits for an element specified by a CSS selector to be clickable and returns a boolean indicating if the element is clickable or not.


4.	Defines the main function follow_instagram_followers that follows followers of a similar Instagram account:

  • Launches a Chrome browser and navigates to the Instagram login page
  •	Logs in to Instagram by entering the username and password and hitting the Enter key
  •	Navigates to the similar account's profile page
  •	Clicks on the followers link to open the followers modal
  •	Scrolls through the followers modal 10 times
  •	Finds all the follow buttons in the modal and clicks on each button that says "Follow"
  •	Closes the browser

5.	Calls the follow_instagram_followers function to run the script.
