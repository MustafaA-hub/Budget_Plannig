import wsimple

def get_otp():
    return input("Enter otpnumber: \n>>>")


email = str(input("Enter email: \n>>>"))
password = str(input("Enter password: \n>>>"))

ws = wsimple(email, password, otp_callback=get_otp) 

# always check if wealthsimple is working (return True if working or an error)
if ws.is_operational(): 
  # check the current operation status of internal Wealthsimple Trade
  print(ws.current_status())
  
  # return a list of securities that include GOOG and GOOGL
 # print(ws.find_securities("GOOG")) 
  
  # create deposit order for 2000 CAD into your account
 # ws.make_deposit(2000)
  
  # create withdrawal order for 6000 CAD into your account
  #ws.make_withdrawal(6000)
  
  # return opening and closing of the exchange NYSE
  print(ws.get_market_hours(exchange="NYSE"))