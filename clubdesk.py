import getpass
import os
import shutil
import sys
import time
from datetime import datetime
from os.path import basename
from zipfile import ZipFile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

download_path = os.getcwd() + "/" + datetime.now().strftime("%Y-%m-%d-%H%M%S")


def prep_folder():
    if not os.path.exists(download_path):
        os.makedirs(download_path)


def create_zip():
    with ZipFile('backup-'+ datetime.now().strftime("%Y-%m-%d-%H%M%S")+'.zip', 'w') as ZipObj:
        for folderName, subfolders, filenames in os.walk(download_path):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                ZipObj.write(filePath, basename(filePath))


def delete_folder():
    shutil.rmtree(download_path)


def export_all():
    spalten_selection = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[6]/div/table/tbody/tr/td[2]/div')
    spalten_selection.click()
    spalten_selection = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]')  # click in selection
    spalten_selection.click()
    time.sleep(1)
    format_selection = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[9]/div/table/tbody/tr/td[2]/div')
    format_selection.click()
    format_selection = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]')
    format_selection.click()
    time.sleep(1)
    ok_button = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/div')
    ok_button.click()


def login_clubdesk():
    user_input = driver.find_element_by_name('userId')
    user_input.send_keys(getpass.getpass(prompt='Username:', stream=sys.stdout))
    pwd_input = driver.find_element_by_name('password')
    pwd_input.send_keys(getpass.getpass(prompt='Passwort:', stream=sys.stderr))
    submit_button = driver.find_element_by_name('submitButton')
    submit_button.click()
    time.sleep(4)


def save_mitglieder():
    member_button = driver.find_element_by_xpath('//*[@id="app-chooser-view"]/div[2]/div')
    member_button.click()
    member_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[5]/div/span[2]')
    member_button.click()
    export_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div/table[5]/tbody/tr[2]/td[2]/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td[2]/div')
    export_button.click()
    time.sleep(1)
    export_all()


def save_rechnungen():
    kategorien = [
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[1]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[2]/div/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[3]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[4]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[5]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[6]/div/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[7]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[8]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[9]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[10]/div/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[11]/div/span[2]',
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/table/tbody/tr/td/div[12]/div/span[2]']
    rechnungen = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/table/tbody/tr/td[2]/div/div[7]/div')
    rechnungen.click()
    rechnungen = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/ul/li[1]/a[2]/em/span/span')
    rechnungen.click()
    # Kategorie Entwürfe
    for k in kategorien:
        driver.find_element_by_xpath(k).click()
        time.sleep(5)
        export_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[1]/div[1]/div/div/table[3]/tbody/tr[2]/td[2]/div/div/div/table/tbody/tr[1]/td/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td[2]/div')))
        export_button.click()
        time.sleep(5)
        export_all()


def save_buchhaltung():
    buchhaltung = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/table/tbody/tr/td[2]/div/div[7]/div')
    buchhaltung.click()
    buchhaltung = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/ul/li[2]/a[2]/em/span/span')
    buchhaltung.click()
    buchhaltung = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/table/tbody/tr[2]/td[2]/div/div')
    buchhaltung.click()
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/span').click()
    time.sleep(2)
    export_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div[7]/div[2]/div/div[2]/div[1]/div/div/table[2]/tbody/tr[2]/td[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td[2]/div')
    export_button.click()
    time.sleep(1)
    format_selection = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[6]/div/table/tbody/tr/td[2]/div')
    format_selection.click()
    format_selection = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]')
    format_selection.click()
    time.sleep(1)
    ok_button = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/div')
    ok_button.click()
    time.sleep(10)


print('Temporären Folder erstellen')
prep_folder()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=1")  # 3=fatal only
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})

chrome_local_state_prefs = {
    "browser": {
        "enabled_labs_experiments": ["new-usb-backend@1"],
    }
}
chrome_options.add_experimental_option("localState", chrome_local_state_prefs)

# driver = webdriver.Chrome('C:/Users/DMR/Documents/PythonScripts/Clubdesk\chromedriver.exe',options=chrome_options)
# driver = webdriver.Chrome('usr/local/bin/chromedriver',options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# driver.get('chrome://flags');
driver.get('https://app.clubdesk.com/clubdesk/start?_ga=2.55198701.7561376.1612889610-1978372832.1542742166')

login_clubdesk()
time.sleep(1)
print('Alle Kontakte:')
save_mitglieder()
time.sleep(1)
print('Rechnungen:')
save_rechnungen()
time.sleep(1)
print('Buchhaltung:')
save_buchhaltung()
print('Zipfile erstellen')
create_zip()
print('Temporären Folder löschen')
time.sleep(10)
delete_folder()
driver.quit()
