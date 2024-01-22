# RouletteTester


There are several methods for interacting with the UI, to use in scripts for automatic testing.
Here is a few examples:

  def place_bet_amount(self, amount):
        try:
            amount_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input'))) 
            amount_input.clear()
            amount_input.send_keys(str(amount))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")  
            
    def get_bet_amount(self):
        try:
            time.sleep(0.5)
            textbox_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[1]/input')))
            return textbox_element.get_attribute('value')
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
            bet_add_OneCent_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[2]')))
            bet_add_OneCent_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
