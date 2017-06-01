from selenium import webdriver
import time
driver = webdriver.Firefox()
url='http://www.amazon.com/gp/gw/ajax/s.html'
driver.get(url)

time.sleep(15)

def No_of_windows():

    windows = driver.window_handles
    number_windows = len(windows)
    return number_windows



def Switch_Window(index):
    try:
        index = int(index)
    except ValueError:
        raise Exception('Please pass an integear value')

    total_window = No_of_windows()
    if index > total_window:
        raise Exception('Requested index is more then avilable window')

    windows = driver.window_handles
    requested_window = windows[index]
    driver.switch_to.window(requested_window)

    return

print No_of_windows()
Switch_Window(0)