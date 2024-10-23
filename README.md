# Restaurant Menu Management System

This project is a **Restaurant Menu Management System** that allows users to manage restaurant menus, including adding, updating, deleting, and loading menu items from a CSV file. The system also computes expense ratings based on the average price of the dishes.

This tool is ideal for restaurant owners, managers, or anyone looking to manage a digital restaurant menu easily. With a few simple commands, you can maintain your menu, make quick updates to item prices or details, and persist your data in CSV format for easy storage and retrieval.

## Features
- **Add Menu Items**: Users can add dishes to the restaurant menu, specifying attributes like name, calories, price, whether it is vegetarian, and spiciness level.
- **Update Menu Items**: Users can update specific attributes of a menu item.
- **Delete Menu Items**: Users can remove a single dish or the entire menu.
- **Load Menu from CSV**: Load a list of menu items from a CSV file and append it to the current menu.
- **Save Menu to CSV**: Save the current menu to a CSV file.
- **Expense Rating**: Compute the average price of all items on the menu and display an expense rating ($, $$, $$$) based on the average price.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/MenuManagementProject.git
2. Navigate into the project directory:
   ```bash
   cd restaurant-menu-management

## Expense Rating
The expense rating of the restaurant is calculated based on the average price of menu items:

- $: Average price < 10
- $$: 10 <= Average price < 20
- $$$: Average price >= 20

## Example CSV File Format
To load menu items from a CSV file, the file should have the following format:
```
name,calories,price,is_vegetarian,spicy_level
Pizza,800,12.99,no,2
Salad,200,7.99,yes,1
Pasta,600,14.99,no,3
```

- name: The name of the dish.
- calories: Integer representing the calories.
- price: Float representing the price.
- is_vegetarian: "yes" or "no" for vegetarian status.
- spicy_level: Integer representing the spiciness level (based on spicy_scale_map).

## Future Improvements
- Unit Tests: Add more extensive unit tests for validating menu operations.
- Error Handling: Improve error handling, especially for invalid CSV input formats.
- Spicy Level Customization: Allow users to customize the spicy level descriptions.

