from selenium import webdriver
import time
import xlrd
from xlwt import Workbook

def trackVehicle():
    try:
        # File location
        excelLoc = ('./VehicleTrack.xlsx')

        # To open Workbook
        wb = xlrd.open_workbook(excelLoc)
        sheet = wb.sheet_by_index(0)

        # Extracting number of rows
        noOfVehicleNumber = sheet.nrows

        vehicle_array = []
        for r in range(1, noOfVehicleNumber):
            vehicle_array.append(sheet.cell_value(r, 0))

        # Workbook is created
        wb = Workbook()

        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1')

        url = 'https://vc.tmsitrimble.in/cms/login/masterLogin.action'
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(url)

        u = driver.find_element_by_name('username')
        u.send_keys('mahindra')
        p = driver.find_element_by_name('password')
        p.send_keys('mlog#1603')
        submit = driver.find_element_by_xpath('/html/body/div/div[4]/div[4]/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td/span/a')
        submit.click()

        time.sleep(20)

        print('After login')

        sheet1.write(0, 0, 'Vehicle Number')
        sheet1.write(0, 1, 'Location')
        sheet1.write(0, 2, 'Date')

        for i in range(len(vehicle_array)):
            vehicleInput = driver.find_element_by_name('vehicleNumber')
            vehicleInput.send_keys(vehicle_array[i])
            print('====================')

            vehicle_search = driver.find_element_by_class_name('dijitButtonText')
            vehicle_search.click()

            time.sleep(10)
            # wait = selenium.WebDriverWait(driver, 10)
            # men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="Scroll_0"]/td[1]/a')))

            v_number = driver.find_element_by_xpath('//*[@id="Scroll_0"]/td[1]/a').text
            location = driver.find_element_by_xpath('//*[@id="Scroll_0"]/td[2]').text
            dueDate = driver.find_element_by_xpath('//*[@id="Scroll_0"]/td[3]').text

            print('v_number ', v_number)
            print('location ', location)
            print('dueDath ', dueDate)

            sheet1.write(i+1, 0, v_number)
            sheet1.write(i+1, 1, location)
            sheet1.write(i+1, 2, dueDate)

        wb.save('Vehicle Tracking.xls')
    except:
        wb.save('Vehicle Tracking.xls')

if __name__ == '__main__':
    trackVehicle()
