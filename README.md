# 🏠 Rent & Expense Splitter Calculator

A simple Python CLI tool that helps roommates or flatmates **split shared expenses fairly** — including rent, food, and electricity — divided equally among all persons living together.

---

## 📋 Features

- Calculate total electricity bill from units consumed and charge per unit
- Add rent and food expenses to the total
- Automatically split the final amount equally among all persons
- Lightweight — no external libraries required

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Run the Script

```bash
python rent_calculator.py
```

---

## 💡 How It Works

The program asks for the following inputs:

| Input | Description |
|---|---|
| `Hostel/Flat Rent` | Total monthly rent of the room or flat |
| `Food Amount` | Total amount spent on food/snacks ordered |
| `Electricity Units` | Total electricity units consumed |
| `Charge Per Unit` | Cost per electricity unit (in ₹ or your currency) |
| `Number of Persons` | Total people sharing the flat/room |

It then calculates:

```
Total Bill     = Electricity Units × Charge Per Unit
Per Person Pay = (Rent + Food + Total Bill) ÷ Number of Persons
```

---

## 🖥️ Sample Output

```
Enter your hostel/flat rent = 8000
Enter the amount of food ordered = 1200
Enter the total of electricity spend = 150
Enter the charge per unit = 8
Total amount of electricity = 1200
Each person will pay = 3466
```

---

## 📁 Project Structure

```
rent-calculator/
│
├── rent_calculator.py   # Main Python script
└── README.md            # Project documentation
```

---

## 🛠️ Built With

- **Python 3** — Core language
- No external libraries — uses only built-in `input()` and arithmetic operations

---

## 🙋 Use Cases

- College hostel roommates splitting monthly expenses
- Friends sharing a flat/apartment
- PG (Paying Guest) residents calculating individual dues

---

## 📌 Future Improvements

- [ ] Add support for unequal splitting (custom shares per person)
- [ ] Export the bill summary to a `.txt` or `.pdf` file
- [ ] Build a GUI version using `Tkinter`
- [ ] Add currency selection support
- [ ] Include water bill and internet bill as inputs

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, open issues, or submit pull requests.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by [Your Name](https://github.com/yourusername)
