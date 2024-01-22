# RouletteTester


There are several methods for interacting with the UI, to use in scripts for automatic testing.
Here is a few examples:


   
    def get_bet_amount(self):
        try:
            time.sleep(0.5)
            textbox_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
            '[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input')))
            return textbox_element.get_attribute('value')
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            
      def place_bet_amount(self, amount):
        try:
            amount_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, 
                '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input'))) 
            amount_input.clear()
            amount_input.send_keys(str(amount))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")  
   
        
    def place_bet_Clear(self):
        try:
            bet_Clear_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[1]')
            bet_Clear_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
       
    def place_bet_OneCent(self):
        try:
            bet_add_OneCent_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*  [@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[2]')))
            bet_add_OneCent_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")



I hace created a few Main() scripts, which automatic tests the UI and gives feedback on the result.
To pick which scenario to test, i edit the Scenario_to_run-variable, and execute the .py:





      if __name__ == "__main__":
       # Set the path to the ChromeDriver executable
       driver_executable_path = 'C:/Users/okvad/Documents/Python Scripts/chromedriver-win64/chromedriver-win64/chromedriver.exe'
       tester = CSGOEmpireRouletteTester(driver_executable_path)
       
       # Example Usage:
       # Choose which simulation to run  
       Scenario_to_run = 4
       
       # Wildcard, clear-, 0.01- ....... max-button testing    
       if Scenario_to_run == 1:
           tester.Main1()
   
       #The Martingale System #1, Start_bet*2+Start_bet on loss
       elif Scenario_to_run == 2:
           #Argument: start_bet + team
           tester.Main2(1.0, "ct")
           
       #The Martingale System #2, Start_bet*2+Start_bet on loss. Picks t or ct compared to last 100 rolls    
       elif Scenario_to_run == 3:
           #Argument: start_betq
           tester.Main3(0.03)     
       #Real life test, with login and balance    
       elif Scenario_to_run == 4:
           tester.Main4(0.02)
