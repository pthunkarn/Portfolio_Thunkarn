## burger menu
menu_id <- c(1,2,3,4)
menu <- c("Signature Burger", "Cheese Burger", 
          "Fish Burger", "Double Cheese Burger")
menu_price <- as.numeric(c(399, 399, 499, 599))
our_menu <- data.frame(menu_id, menu, menu_price)

#Addtional
side_id <- c(1,2,3)
side <- c("French Fries", "Onion Ring", "Hash Brown")
add_price <- as.numeric(c(20,40,40))
our_side <- data.frame(side_id, side, add_price)

chatbot <- function() {
  print("Hello welcome to our Burger restaurant. Hope you enjoy your meal")
  
  # Get the customer's name
  cus_name <- readline("Before you order, May i know your name first?: ")
  
  # Print "Hello! Name"
  print(paste("Hello!", cus_name))
  
  print("Now it's time to order your Burger. Please see our menu")
  print(our_menu)
  
  # Receive order
  selected_id <- readline("Which burger you want to have today? :)")
  
  # Find the menu name for the selected ID
  menu_name <- our_menu[our_menu$menu_id == selected_id, "menu"]
  menu_price <- our_menu[our_menu$menu_id == selected_id, "menu_price"]
  # Print the order
  print(paste("Nice! You have ordered", menu_name, 
              "and price is", menu_price, "THB"))
  
  # Add order
  print("How about the side menu? Here is our side dishes menu")
  print(our_side)
  selected_id <- readline("Which side dishes do you want?")
  
  # Find the menu name for the selected ID
  add_name <- our_side[our_side$side_id == selected_id, "side"]
  add_price2 <- our_side[our_side$side_id == selected_id, "add_price"]
  # Print the order
  print(paste("Nice! You have ordered", add_name, 
              "and price is", add_price2, "THB"))
  # Sum the price of the menu and add price
  total_price <- menu_price + add_price2
  
  # Print the total price
  print(paste("The total price of your order is", total_price, "THB. Thank you", cus_name, "Have a good day!"))
}

chatbot()

