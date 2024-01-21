from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import keyboard
import locale
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CSGOEmpireRouletteTester:
    def __init__(self, driver_path):
        service = Service(executable_path=driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://csgoempire.com/roulette')
   
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #def login(self, username, password):
        #Dont want to simulate login case, for privacy reasons as of now

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

    def place_bet_TenCent(self):
        try:
            bet_add_TenCent_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[3]')
            bet_add_TenCent_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    
    def place_bet_Dollar(self):
        try:
            bet_add_Dollar_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[4]')
            bet_add_Dollar_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        
    def place_bet_TenDollars(self):
        try:
            bet_add_TenDollars_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[5]')
            bet_add_TenDollars_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def place_bet_HundredDollars(self):
        try:
            bet_add_HundredDollar_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[6]')
            bet_add_HundredDollar_button.click()    
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def place_bet_half(self):
        try:
            bet_sub_Half_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[7]')
            bet_sub_Half_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def place_bet_Double(self):
        try:
            bet_add_Double_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[8]')
            bet_add_Double_button.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def place_bet_MaxBalance(self, Curr_Balance):
        try:
            bet_add_MaxBalance_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[4]/div/div[2]/div/button[9]')
            bet_add_MaxBalance_button.click() 
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            
        #Temp code, since I am not logged in:
        self.place_bet_amount(Curr_Balance)

    #Random pressing clear-, +0.01-, +0.1- ...... MAX-buttons
    def place_bet_extra_randomized(self, initial_bet, curr_balance):
        try:
            tot_bet = initial_bet
    
            #Numbers of buttons pressed
            random1 = random.randint(0,2)
                        
            for i in range(random1):
                #Choose which button
                random2 = random.randint(0,72)    
            
                #Number spesific a button is pressed
                random3 = random.randint(1,2)
                
                if random2 >= 0 and random2 < 5:
                    for j in range(random3):
                        print("clear_btn_pressed")
                        self.place_bet_Clear()
                        tot_bet = 0
                        
                elif random2 >= 5 and random2 < 20:
                    for j in range(random3):
                        print("0.01_btn_pressed")
                        self.place_bet_OneCent()
                        tot_bet += 0.01
                elif random2 >= 20 and random2 < 30:
                    for j in range(random3):
                        print("0.1_btn_pressed")
                        self.place_bet_TenCent()
                        tot_bet += 0.1
                elif random2 >= 40 and random2 < 50:
    
                    for j in range(random3):
                        print("1_btn_pressed")
                        self.place_bet_Dollar()
                        tot_bet += 1
                elif random2 >= 50 and random2 < 55:
                    for j in range(random3):
                        print("10_btn_pressed")
                        self.place_bet_TenDollars()
                        tot_bet += 10
                elif random2 >= 55 and random2 < 60:
                    for j in range(random3):
                        print("100_btn_pressed") 
                        self.place_bet_HundredDollars() 
                        tot_bet += 100
                elif random2 >= 60 and random2 < 65:
                    for j in range(random3):
                        print("half_btn_pressed")  
                        self.place_bet_half()
                        tot_bet /= 2
                elif random2 >= 65 and random2 < 70:
                    for j in range(random3):
                        print("double_btn_pressed") 
                        self.place_bet_Double()
                        tot_bet *= 2
                elif random2 >= 70 and random2 <= 72:
                    for j in range(random3):
                        print("Max_btn_pressed") 
                        self.place_bet_MaxBalance(curr_balance)
                        tot_bet = curr_balance
                        
            return tot_bet
        
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
   
    def place_bet_team(self, team):
        try:
            if team == "ct":
                self.place_bet_CT()
            elif team == "t":
                self.place_bet_T()
            elif team == "bonus":
                self.place_bet_bonus()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        
    def place_bet_CT(self):
        try:
            place_bet_ct_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[5]/div[1]/button')
            #Unable til press, since not logged in
            #Remember to comment out click line when simulating:
            place_bet_ct_button.click()
            print("CT_bet_btn_Pressed")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    def place_bet_T(self):
        try:
            place_bet_t_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[5]/div[3]/button')
            #Unable til press, since not logged in
            #Remember to comment out click line when simulating:
            place_bet_t_button.click()
            print("T_bet_btn_Pressed")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    def place_bet_bonus(self):
        try:
            place_bet_bonus_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[5]/div[2]/button')
            #Unable til press, since not logged in
            #Remember to comment out click line when simulating:
            place_bet_bonus_button.click()
            print("Bonus_bet_btn_Pressed")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    #Gets the result from the past 10 rolls
    def get_previous_10_rolls(self):
        try:
            # Declare an array of integers with a size of 10
            ar = ['0'] * 10
            
            #print(str(len(ar)))
            for i in range(0,10):
                # print(i)
                ar[i] = (self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[' + str(i+1) + ']/div')))).get_attribute("class")
    
            returnstring = ""
            for j in ar:
                s = j.split("coin-",1)[1]
                f = s.split(" ")[0]
                returnstring += f + "\t"
    
            return returnstring
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    
    def get_result_last_roll(self):
        try:
            lastTen = self.get_previous_10_rolls()
            lastRoll = lastTen.split("\t")[9]
            return lastRoll
        except NoSuchElementException as e:
            print(f"Element not found: {e}")


    def verify_outcome(self):
        # Example: Verify the outcome of the bet
        # (add assertions or checks based on the expected behavior)
        pass
    
    def check_ready_bet(self):
        try:
            Next_bet_ready = tester.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]')
            if(Next_bet_ready.is_displayed()):
                return True
            else:
                return False
            
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    def check_bet_result(self, teamBet):
        try:
            winningTeam = self.get_result_last_roll()
            
            if(teamBet == winningTeam): 
                return True
            else:
                return False
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            
    def get_last_100rolls_team_cnt(self, team):
        try:
            if team == "ct":
                ct_100_cnt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[3]')))
                return int((ct_100_cnt.text))
            elif team == "t":
                t_100_cnt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[7]')))
                return int(t_100_cnt.text)
            elif team == "bonus":
                bonus_100_cnt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[5]')))
                return int(bonus_100_cnt.text)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            
    #Not in use, since not logged in         
    def get_current_balance(self):
        try:
            Curr_Balance =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span/div/span[2]')))       
            # Replace commas with dots
            cleaned_string = Curr_Balance.text.replace(',', '.')
            
            return cleaned_string

        except NoSuchElementException as e:
            print(f"Element not found: {e}")



  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Main1(self):        
        #In order to simulate a user without logging in, i am making a balance variable, 
        #insted of reading the lable/textbox for balance at the roulette view

        #Init:
        Balance = 1000

        Initial_bet = 0

        bet_comma = 0
        Total_bet = 0

        Team_Selector = 0
        Team = ""
        New_Round = True
        Bets_placed = False
        n_bets = 1
    
        try:
            time.sleep(1)
            print("-------------------------------------------------\nSimulation start\nMode: Wildecard\nPress q to exit")
            while True:    
                try:
    
                    if(tester.check_ready_bet() == False):
    
                        print("Wheel rolling!")
                        time.sleep(1)
                        New_Round = True       
                        tester.place_bet_Clear()
                        
                    elif tester.check_ready_bet():
                        if New_Round == True:
    
                            
                            if Bets_placed == True:
                                resultstr = ""
                                
                                resultstr += ("Last Roll: " + (tester.get_result_last_roll()) + "\nLast bet: " + Team)
                                
                                #print("Last roll: " + (tester.get_result_last_roll()) + "\nLast bet: " + Team)
                                
                                #Win
                                if(tester.check_bet_result(Team)):
                                    resultstr += (Fore.GREEN + "\nWin: ")
                                    if(Team == "bonus"):
                                        Balance += (Total_bet * 14)
                                        resultstr += str(Total_bet * 14)
    
                                        #print("Profit:\t" + str(Total_bet * 14))
       
                                    else:
                                        Balance += (Total_bet * 2)
                                        #print("Profit:\t" + str(Total_bet * 2))
                                        resultstr += str(Total_bet * 2)
                                #Loss
                                else:
                                    resultstr += (Fore.RED + "\nLoss: " + str(round(Total_bet,2)))
                                    #print("Lost: \t-" + str(Total_bet))
                                    
                                    
                                print(resultstr + Style.RESET_ALL)
                                Bets_placed = False
                                        
                            if Bets_placed == False:
                                Bets_placed = True
                                #Check result, if
                                #Place bet(s)
                                print("-------------------------------------------------\n" + "Bet#" + str(n_bets) + "\nBalance: " + str(round(Balance,2)))
                                #Random bet (10-25)
                                Initial_bet = 0
                                Initial_bet = random.randint(100, 250)
                                print("Initial bet: " + str(Initial_bet))
                                tester.place_bet_amount(Initial_bet)
                                #Add extra bets 0.01, 0.01 etc
                                Total_bet = round(tester.place_bet_extra_randomized(Initial_bet, (Balance)),2)
                                
                                #Temp
                                #Total_bet = Initial_bet
                                
                                #Endre tilbake til 0, 14
                                Team_Selector = random.randint(0,14)
                                if Team_Selector >=0 and Team_Selector <= 6:
                                    Team = "ct"
                                elif Team_Selector >6 and Team_Selector <=12:
                                    Team = "t"
                                elif Team_Selector > 12 and Team_Selector <= 14:
                                    Team = "bonus"
                                
        
                                n_bets += 1
                                tester.place_bet_team(Team)
                                Balance -= Total_bet  
                                print("Bet placed\t" + Team + "\t" +str(Total_bet) + " Coin(s)\tNew Balance: " + str(round(Balance, 2)))
                               
                                #Checking for ',' in bet-textbox, and replacing with '.'
                                try: 
                                    bet_comma =tester.get_bet_amount()
                                    # Replace commas with dots
                                    cleaned_string = bet_comma.replace(',', '.')
                            
                                    # Convert the cleaned string to a float
                                    float_value = float(cleaned_string)
                                    if Total_bet != float_value:
                                        print("Error: Mismatch between Theoretical and actual bet size!")

                                except ValueError as e:
                                    print(f"Error converting to float: {e}")
                                    #Lag metode som sjekker faktisk textbox-verdi, og sammenlign d me Total_Bet. Flagg vist der er diff
                                    #Ble av og til diff om det ble mange trykk på 0.01 0.1 knappene
                                
                            New_Round = False    
                            
                    if keyboard.is_pressed('q'):  # Check if the 'q' key is pressed
                        break  # Break out of the loop if 'q' is pressed

                except:
                    print("ka i alge dage")
                    pass
        
        except KeyboardInterrupt:
            print("Simulation Interupted")
            pass
        finally:
            print("Simulation Ended\n-------------------------------------------------")
            tester.driver.quit()    
            
    def Main2(self, martingale_bet, martingale_team):

        #Init:
        Balance = 1000
        bet_comma = 0
        Total_bet = 0
        Team = ""
        New_Round = True
        Bets_placed = False
        n_bets = 1
        prev_loss = False
        prev_bet = 0.0
        Losing_streak_cnt = 0
        Losing_streak_cnt_max = 0
        Winning_streak_cnt = -1
        Winning_streak_cnt_max=0
        first_run = True
    
        try:
            time.sleep(1)
            print("-------------------------------------------------\nSimulation start\nMode: Martingale#1,X*2+X on L\nPress q to exit\n")
            tester.get_last_100rolls_team_cnt("ct")
            while True:    
                try:
                    if(tester.check_ready_bet() == False):
    
                        print("Wheel rolling!")
                        time.sleep(1)
                        New_Round = True       
                        tester.place_bet_Clear()
                        first_run = False
                        
                    elif (tester.check_ready_bet() == True and first_run == False):

                        if New_Round == True:    
                            
                            if Bets_placed == True:
                                resultstr = ""
                                
                                resultstr += ("Last Roll: " + (tester.get_result_last_roll()) + "\nLast bet: " + Team)

                                #Win
                                if(tester.check_bet_result(Team)):
                                    resultstr += (Fore.GREEN + "\nWin: ")
                                    Balance += (Total_bet * 2)
                                    #print("Profit:\t" + str(Total_bet * 2))
                                    resultstr += str(Total_bet * 2)
                                    prev_loss = False
                                #Loss
                                else:
                                    resultstr += (Fore.RED + "\nLoss: " + str(round(Total_bet,2)))
                                    #print("Lost: \t-" + str(Total_bet))
                                    prev_loss = True
                                                                        
                                print(resultstr + Style.RESET_ALL)
                                Bets_placed = False
                                        
                            if Bets_placed == False:
                                Bets_placed = True
                                #Check result, if
                                #Place bet(s)
                                print("-------------------------------------------------\n" + "Bet#" + str(n_bets))
                                                                  
                                if (prev_loss):
                                    Total_bet = (prev_bet * 2 + martingale_bet)
                                    Losing_streak_cnt += 1
                                    if Losing_streak_cnt > Losing_streak_cnt_max:
                                        Losing_streak_cnt_max = Losing_streak_cnt
                                    Winning_streak_cnt = 0
                                    print("Current losing streak: " + str(Losing_streak_cnt))
                                else:
                                    Total_bet = martingale_bet
                                    Winning_streak_cnt += 1
                                    if Winning_streak_cnt > Winning_streak_cnt_max:
                                        Winning_streak_cnt_max = Winning_streak_cnt
                                    Losing_streak_cnt = 0
                                    print("Current winning streak: " +  str(Winning_streak_cnt))
                                
                                print("Longest winning streak: " + str(Winning_streak_cnt_max) 
                                      + "\nLongest losing streak: " + str(Losing_streak_cnt_max)
                                      + "\nBalance: " + str(round(Balance,2)) + "\n")
                                

                                #Calculate bet size
                                Total_bet = round(Total_bet, 2,)
                                
                                #Place bet
                                tester.place_bet_amount(Total_bet)
                                Team = martingale_team

                                #Static team pick
                                tester.place_bet_team(Team)
                                
                                Balance -= Total_bet  
                                print("Bet placed\t" + Team + "\t" +str(Total_bet) + " Coin(s)\tNew Balance: " + str(round(Balance, 2)))
                                prev_bet = Total_bet
                                
                                #Accumulating session number
                                n_bets += 1
                                
                                #Checking for ',' in bet-textbox, and replacing with '.'
                                try: 
                                    bet_comma =tester.get_bet_amount()
                                    # Replace commas with dots
                                    cleaned_string = bet_comma.replace(',', '.')
                            
                                    # Convert the cleaned string to a float
                                    float_value = float(cleaned_string)
                                    if Total_bet != float_value:
                                        print("Error: Mismatch between Theoretical and actual bet size!")

                                except ValueError as e:
                                    print(f"Error converting to float: {e}")
                                    #Lag metode som sjekker faktisk textbox-verdi, og sammenlign d me Total_Bet. Flagg vist der er diff
                                    #Ble av og til diff om det ble mange trykk på 0.01 0.1 knappene
                                
                            New_Round = False    
                            first_run = False
                            
                    if keyboard.is_pressed('q'):  # Check if the 'q' key is pressed
                        break  # Break out of the loop if 'q' is pressed

                except:
                    print("ka i alge dage")
                    pass
        
        except KeyboardInterrupt:
            print("Simulation Interupted")
            pass
        finally:
            print("Simulation Ended\n-------------------------------------------------")
            tester.driver.quit()    
            
    def Main3(self, martingale_bet):

         #Init:
         Balance = 1000
         bet_comma = 0
         Total_bet = 0
         Team = ""
         New_Round = True
         Bets_placed = False
         n_bets = 1
         prev_loss = False
         prev_bet = 0.0
         Losing_streak_cnt = 0
         Losing_streak_cnt_max = 0
         Winning_streak_cnt = -1
         Winning_streak_cnt_max=0
         first_run = True
     
         try:
             print("-------------------------------------------------\nSimulation start\nMode: Martingale#2,X*2+X on L\nTeam picked according to last 100 rolls\nPress q to exit\n")
             while True:    
                 try:
                     if(tester.check_ready_bet() == False):
     
                         print("Wheel rolling!")
                         time.sleep(1)
                         New_Round = True       
                         tester.place_bet_Clear()
                         first_run = False
                         
                     elif (tester.check_ready_bet() == True and first_run == False):

                         if New_Round == True:    
                             
                             if Bets_placed == True:
                                 resultstr = ""
                                 
                                 resultstr += ("Last Roll: " + (tester.get_result_last_roll()) + "\nLast bet: " + Team)

                                 #Win
                                 if(tester.check_bet_result(Team)):
                                     resultstr += (Fore.GREEN + "\nWin: ")
                                     Balance += (Total_bet * 2)
                                     #print("Profit:\t" + str(Total_bet * 2))
                                     resultstr += str(Total_bet * 2)
                                     prev_loss = False
                                 #Loss
                                 else:
                                     resultstr += (Fore.RED + "\nLoss: " + str(round(Total_bet,2)))
                                     #print("Lost: \t-" + str(Total_bet))
                                     prev_loss = True
                                                                         
                                 print(resultstr + Style.RESET_ALL)
                                 Bets_placed = False
                                         
                             if Bets_placed == False:
                                 Bets_placed = True
                                 #Check result, if
                                 #Place bet(s)
                                 print("-------------------------------------------------\n" + "Bet#" + str(n_bets))
                                                                   
                                 if (prev_loss):
                                     Total_bet = (prev_bet * 2 + martingale_bet)
                                     Losing_streak_cnt += 1
                                     if Losing_streak_cnt > Losing_streak_cnt_max:
                                         Losing_streak_cnt_max = Losing_streak_cnt
                                     Winning_streak_cnt = 0
                                     print("Current losing streak: " + str(Losing_streak_cnt))
                                 else:
                                     Total_bet = martingale_bet
                                     Winning_streak_cnt += 1
                                     if Winning_streak_cnt > Winning_streak_cnt_max:
                                         Winning_streak_cnt_max = Winning_streak_cnt
                                     Losing_streak_cnt = 0
                                     print("Current winning streak: " +  str(Winning_streak_cnt))
                                 
                                 print("Longest winning streak: " + str(Winning_streak_cnt_max) 
                                       + "\nLongest losing streak: " + str(Losing_streak_cnt_max)
                                       + "\nBalance: " + str(round(Balance,2)) + "\n")
                                 

                                 #Calculate bet size
                                 Total_bet = round(Total_bet, 2,)
                                 
                                 #Place bet
                                 tester.place_bet_amount(Total_bet)
                                 
                                 if(tester.get_last_100rolls_team_cnt("ct") <= tester.get_last_100rolls_team_cnt("t")):
                                     Team = "ct"
                                 else:
                                     Team = "t"
                                 

                                 #Static team pick
                                 tester.place_bet_team(Team)
                                 
                                 Balance -= Total_bet  
                                 print("Bet placed\t" + Team + "\t" +str(Total_bet) + " Coin(s)\tNew Balance: " + str(round(Balance, 2)))
                                 prev_bet = Total_bet
                                 
                                 #Accumulating session number
                                 n_bets += 1
                                 
                                 #Checking for ',' in bet-textbox, and replacing with '.'
                                 try: 
                                     bet_comma =tester.get_bet_amount()
                                     # Replace commas with dots
                                     cleaned_string = bet_comma.replace(',', '.')
                             
                                     # Convert the cleaned string to a float
                                     float_value = float(cleaned_string)
                                     if Total_bet != float_value:
                                         print("Error: Mismatch between Theoretical and actual bet size!")

                                 except ValueError as e:
                                     print(f"Error converting to float: {e}")

                                 
                             New_Round = False    
                             first_run = False
                             
                     if keyboard.is_pressed('q'):  # Check if the 'q' key is pressed
                         break  # Break out of the loop if 'q' is pressed

                 except:
                     print("Error")
                     pass
         
         except KeyboardInterrupt:
             print("Simulation Interupted")
             pass
         finally:
             print("Simulation Ended\n-------------------------------------------------")
             tester.driver.quit()    

    def Main4(self, martingale_bet):

         #Init:
         Balance = 1000
         bet_comma = 0
         Total_bet = 0
         Team = ""
         New_Round = True
         Bets_placed = False
         n_bets = 1
         prev_loss = False
         prev_bet = 0.0
         Losing_streak_cnt = 0
         Losing_streak_cnt_max = 0
         Winning_streak_cnt = -1
         Winning_streak_cnt_max=0
         first_run = True
     
         try:
             
           
             
             print("40sec until simulation starts")
             time.sleep(40)

             
             print("-------------------------------------------------\nSimulation start\nMode: Martingale#2,X*2+X on L\nTeam picked according to last 100 rolls\nPress q to exit\n")
             while True:    
                 try:
                     if(tester.check_ready_bet() == False):
     
                         print("Wheel rolling!")
                         time.sleep(1)
                         New_Round = True       
                         tester.place_bet_Clear()
                         first_run = False
                         
                     elif (tester.check_ready_bet() == True and first_run == False):

                         if New_Round == True:    
                             
                             if Bets_placed == True:
                                 resultstr = ""
                                 
                                 resultstr += ("Last Roll: " + (tester.get_result_last_roll()) + "\nLast bet: " + Team)

                                 #Win
                                 if(tester.check_bet_result(Team)):
                                     resultstr += (Fore.GREEN + "\nWin: ")
                                     #Balance += (Total_bet * 2)
                                     resultstr += str(Total_bet * 2)
                                     prev_loss = False
                                 #Loss
                                 else:
                                     resultstr += (Fore.RED + "\nLoss: " + str(round(Total_bet,2)))
 
                                     prev_loss = True
                                                                         
                                 print(resultstr + Style.RESET_ALL)
                                 Bets_placed = False
                                         
                             if Bets_placed == False:
                                 Bets_placed = True
                                 #Check result, if
                                 #Place bet(s)
                                 print("-------------------------------------------------\n" + "Bet#" + str(n_bets))
                                 
                                  #Get active balance
                                 try:
                                     Balance = float(tester.get_current_balance())
                                 except NoSuchElementException as e:
                                     print(f"Element not found: {e}" + "køllefgaen")
                                     Balance = 0
                                 
                                 if (prev_loss):
                                     Total_bet = (prev_bet * 2 + martingale_bet)
                                     if Total_bet >= Balance:
                                         Total_bet = Balance
                                     Losing_streak_cnt += 1
                                     if Losing_streak_cnt > Losing_streak_cnt_max:
                                         Losing_streak_cnt_max = Losing_streak_cnt
                                     Winning_streak_cnt = 0
                                     print("Current losing streak: " + str(Losing_streak_cnt))
                                 else:
                                     Total_bet = martingale_bet
                                     Winning_streak_cnt += 1
                                     if Winning_streak_cnt > Winning_streak_cnt_max:
                                         Winning_streak_cnt_max = Winning_streak_cnt
                                     Losing_streak_cnt = 0
                                     print("Current winning streak: " +  str(Winning_streak_cnt))
                                 
                                                                  
                                 print("Longest winning streak: " + str(Winning_streak_cnt_max) 
                                       + "\nLongest losing streak: " + str(Losing_streak_cnt_max)
                                       + "\nBalance: " + str(round(Balance,2)) + "\n")
                                 

                                 #Calculate bet size
                                 Total_bet = round(Total_bet, 2,)
     
                                 #Place bet
                                 tester.place_bet_amount(Total_bet)
                                 
                                 if(tester.get_last_100rolls_team_cnt("ct") <= tester.get_last_100rolls_team_cnt("t")):
                                     Team = "ct"
                                 else:
                                     Team = "t"
                                 

                                 #Static team pick
                                 tester.place_bet_team(Team)
                              
                                 print("Bet placed\t" + Team + "\t" +str(Total_bet) + " Coin(s)\tNew Balance: " + str(round((Balance- Total_bet),2)))
                                 prev_bet = Total_bet
                                 
                                 #Accumulating session number
                                 n_bets += 1
                                 
                                 #Checking for ',' in bet-textbox, and replacing with '.'
                                 try: 
                                     bet_comma =tester.get_bet_amount()
                                     # Replace commas with dots
                                     cleaned_string = bet_comma.replace(',', '.')
                             
                                     # Convert the cleaned string to a float
                                     float_value = float(cleaned_string)
                                     if Total_bet != float_value:
                                         print("Error: Mismatch between Theoretical and actual bet size!")

                                 except ValueError as e:
                                     print(f"Error converting to float: {e}")

                                 
                             New_Round = False    
                             first_run = False
                             
                     if keyboard.is_pressed('q'):  # Check if the 'q' key is pressed
                         break  # Break out of the loop if 'q' is pressed

                 except:
                     print("Error")
                     pass
         
         except KeyboardInterrupt:
             print("Simulation Interupted")
             pass
         finally:
             print("Simulation Ended\n-------------------------------------------------")
             tester.driver.quit()            



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
        