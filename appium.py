from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time
from PIL import Image
from io import BytesIO
from appium.webdriver.common.touch_action import TouchAction

# Specify the path of flipkart.apk in capabilities
# Change the deviceName in capabilities to match your emulator or device
capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',  # Replace with your emulator/device name
    'app': '/home/reddy/Android/Sdk/platform-tools/flipkart1.apk',  # Path to Flipkart APK
    'appPackage': 'com.flipkart.android',
    'appActivity': '.activity.HomeFragmentHolderActivity',
}

appium_server_url = 'http://localhost:4723'

try:
    driver = webdriver.Remote(appium_server_url, capabilities)
except Exception as e:
    print(f"Exception occurred while establishing connection to Appium server: {str(e)}")
    raise e

try:
    driver.implicitly_wait(50)  # Implicit wait for 50 seconds
except Exception as e:
    print(f"Exception occurred while setting implicit wait: {str(e)}")
    raise e

try:
    # Click on Login Skip button if present
    try:
        Skip_button = driver.find_element(by=MobileBy.ID, value='com.flipkart.android:id/custom_back_icon').click()
    except Exception as e:
        print(f"Exception occurred while clicking Skip button: {str(e)}")
        raise e
except Exception as e:
    print(f"Exception occurred in try block for clicking Skip button: {str(e)}")
    raise e

try:
    driver.implicitly_wait(30)  # Reduce implicit wait to 30 seconds
except Exception as e:
    print(f"Exception occurred while setting implicit wait: {str(e)}")
    raise e

try:
    # Perform search for 'Hindi books'
    try:
        search = driver.find_element(by=MobileBy.XPATH, value='(//android.widget.FrameLayout[@resource-id="com.flipkart.android:id/main_content"])[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]').click()
    except Exception as e:
        print(f"Exception occurred while performing search: {str(e)}")
        raise e
except Exception as e:
    print(f"Exception occurred in try block for performing search: {str(e)}")
    raise e

try:
    # Wait to load the search element due to emulator or device performance
    time.sleep(5)
except Exception as e:
    print(f"Exception occurred while sleeping: {str(e)}")
    raise e

try:
    # Enter 'Hindi books' into the search field
    try:
        send_key = driver.find_element(by=MobileBy.CLASS_NAME, value='android.widget.EditText')
        send_key.send_keys('Hindi books')
    except Exception as e:
        print(f"Exception occurred while sending keys: {str(e)}")
        raise e
except Exception as e:
    print(f"Exception occurred in try block for sending keys: {str(e)}")
    raise e

try:
    # Wait for 5 seconds after typing search query
    time.sleep(5)
except Exception as e:
    print(f"Exception occurred while sleeping: {str(e)}")
    raise e

try:
    # Click on the first book in search results
    try:
        click_on_books = driver.find_element(by=MobileBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]').click()
    except Exception as e:
        print(f"Exception occurred while clicking on books: {str(e)}")
        raise e
except Exception as e:
    print(f"Exception occurred in try block for clicking on books: {str(e)}")
    raise e

try:
    # Wait for 5 seconds after clicking on the book
    time.sleep(5)
except Exception as e:
    print(f"Exception occurred while sleeping: {str(e)}")
    raise e

try:
    # Handle 'Not Now' popups if they appear
    try:
        not_now_button = driver.find_element(by=MobileBy.ID, value='com.flipkart.android:id/not_now_button').click()
        time.sleep(5)
        not_now_again = driver.find_element(by=MobileBy.ID, value='com.flipkart.android:id/not_now_button').click()
    except Exception as e:
        print(f"Exception occurred while handling 'Not Now' popup: {str(e)}")
        raise e
except Exception as e:
    print(f"Exception occurred in try block for handling 'Not Now' popup: {str(e)}")
    raise e

try:
    driver.implicitly_wait(10)  # Reduce implicit wait to 10 seconds
except Exception as e:
    print(f"Exception occurred while setting implicit wait: {str(e)}")
    raise e

try:
    # Scroll down to capture screenshots of Hindi books
    for scroll in range(20):
        try:
            for i, screen_shot in enumerate(driver.find_elements(by=MobileBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')):
                try:
                    # Capture screenshot of each book element
                    screen_shot_element = screen_shot.screenshot_as_png
                    image = Image.open(BytesIO(screen_shot_element))
                    image.save(f'screen_shots/screenshot_{i+1}_{scroll}.png')
                except Exception as e:
                    print(f"Exception occurred while capturing screenshot: {str(e)}")
                    raise e

                # Perform scroll action to navigate to the next set of books
                scroll_action = TouchAction(driver)
                scroll_action.press(x=508, y=1952).move_to(x=526, y=784).release().perform()
        except Exception as e:
            print(f"Exception occurred in inner loop: {str(e)}")
            raise e
except Exception as e:
    print(f"Exception occurred in try block for scrolling: {str(e)}")
    raise e

try:
    driver.quit()  # Quit the driver session after completing the operation
except Exception as e:
    print(f"Exception occurred while quitting driver session: {str(e)}")
    raise e
