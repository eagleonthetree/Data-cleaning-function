import pandas as pd
import tkinter as tk
from tkinter import filedialog


def print_menu():
    print(31 * "-", "MENU", 31 * "-")
    print("1. Show spreadsheet in a dataframe")
    print("2. Remove line feed and excessive space characters")
    print("3. Alter text case for all columns")
    print("4. Alter text case for a specified column")
    print("5. Inspect for duplicated rows ")
    print("6. Remove a row")
    print("7. Remove a column")
    print("8. Update a cell")
    print("9. Sort rows by column value")
    print("10. Show selected column's value counts")
    print("11. Alter column value(s)")
    print("12. Save cleaned data to CSV file")
    print("13. Leave")
    print(69 * "-")


def case_menu():
    print("1. Title Case")
    print("2. lower case")
    print("3. UPPER CASE")
    print("4. Capitalize first letter")


def show(dataframe):
    print(df)
    print("CSV file is displayed in dataframe")
    return


def remove_space(dataframe):
    df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\r"], value=["", ""], regex=True, inplace=True)
    df.replace(to_replace=[r"\\n", "\n"], value=["", "/"], regex=True, inplace=True)
    df.replace(to_replace=["  ", "  "], value=["", " "], regex=True, inplace=True)
    cols = df.select_dtypes(['object']).columns
    df[cols] = df[cols].apply(lambda x: x.str.strip())
    print(df)
    return


def case_change(dataframe):
    case_menu()
    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        for col in df.columns:
            df[col] = df[col].str.title()

    elif choice1 == 2:
        for col in df.columns:
            df[col] = df[col].str.lower()

    elif choice1 == 3:
        for col in df.columns:
            df[col] = df[col].str.upper()
    elif choice1 == 4:
        for col in df.columns:
            df[col] = df[col].str.capitalize()

    print(df)
    return


def column_case_change(dataframe):
    print(list(df.columns))

    choice2 = str(input("Enter the column name for case change: "))

    case_menu()
    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        df[choice2] = df[choice2].str.title()
    elif choice3 == 2:
        df[choice2] = df[choice2].str.lower()
    elif choice3 == 3:
        df[choice2] = df[choice2].str.upper()
    elif choice3 == 4:
        df[choice2] = df[choice2].str.capitalize()

    print(df)

    return


def duplicate_inspect(dataframe):
    duplicatedrows = df[df.duplicated(keep='first')]
    print("Duplicated Rows are :")
    print(duplicatedrows)

    return


def row_remove(dataframe):
    choice5 = int(input("Enter your row number to delete: "))
    print(df.loc[[choice5]])
    Safety = int(input('Type 1 to confirm delete, otherwise type 2: '))

    if Safety == 1:
        df.drop([choice5], axis=0, inplace=True)
        print(df)
        print(31 * "-", "Row", choice5, "has been deleted", 31 * "-")

    elif Safety == 2:
        return


def column_remove(dataframe):
    print(list(df.columns))
    choice4 = str(input("Enter your column name to delete: "))
    for column in df[choice4]:
        print(column)
    Safety = int(input('Type 1 to confirm delete, otherwise type 2: '))

    if Safety == 1:
        for delete_column in df[choice4]:
            print(delete_column, "is now removed")
        df.drop([choice4], axis=1, inplace=True)
        print(df)
        print(31 * "-", "Row", choice4, "has been deleted", 31 * "-")

    elif Safety == 2:
        return


def cell_update(dataframe):
    row_number = int(input("Enter row number: "))
    if row_number in df.index:
        print(df.loc[[row_number]])
    else:
        print("please enter a valid row number")

    column_name = str(input("Enter the column name for change: "))

    if not {column_name}.issubset(df.columns):
        print("please enter a valid columns")

    old_value = df.at[row_number, column_name]
    new_value = str(input("Enter new cell value: "))

    print("The new cell value of row ", row_number, "column ", column_name, "will be updated from ",
          old_value, "to ", new_value)

    Safety1 = int(input('Type 1 to confirm change, otherwise type 2: '))

    if Safety1 == 1:
        df.at[row_number, column_name] = new_value
        print("row has been updated to", (df.loc[[row_number]]))
    elif Safety1 == 2:
        return


def sort_rows(dataframe):
    print(list(df.columns))
    sort_option = str(input("Enter the column name to sort: "))

    df.sort_values(by=sort_option, inplace=True)
    print("Content in dataframe has been sorted based on a column", sort_option, "in ascending Order : ")
    print(df)

    return dataframe


def show_column(dataframe):
    print(list(df.columns))
    column_display = str(input("Enter the column name to display occurrence: "))

    print(df[column_display].value_counts())
    print("Column value counts has been displayed in descending order")
    return


def change_column_value(dataframe):
    print(list(df.columns))
    column_change = str(input("Enter the column for change: "))

    change_value = str(input("Enter the value for change: "))

    new_value = str(input("New value: "))

    df[column_change] = df[column_change].replace([change_value], new_value)

    for column in df[column_change]:
        print(column)

    return


def save_file(dataframe):
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300, bg='cyan', relief='raised')
    canvas1.pack()

    def exportcsv():
        global df

        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv(export_file_path, index=False, header=True)

        root.destroy()

    export_button = tk.Button(text='Click to Export CSV', command=exportcsv, bg='hot pink', fg='grey6',
                              font=('helvetica', 12,))
    canvas1.create_window(150, 150, window=export_button)

    root.mainloop()

    return


def quit():
    exit()


terminate = False
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg='cyan', relief='raised')
canvas1.pack()


def importcsv():
    global df

    import_file_path = filedialog.askopenfilename()

    print("File has been imported from: ", import_file_path)
    df = pd.read_csv(import_file_path)
    pd.set_option('display.max_columns', None)

    root.destroy()


import_button = tk.Button(text="      Click here to import CSV File     ", command=importcsv, bg='hot pink',
                          fg='grey6',
                          font=('helvetica', 12,))
canvas1.create_window(150, 150, window=import_button)

root.mainloop()

while (not terminate):
    print_menu()
    choice = int(input("Enter your choice [1-13]: "))
    if choice == 1:
        show(df)
    elif choice == 2:
        remove_space(df)
    elif choice == 3:
        case_change(df)
    elif choice == 4:
        column_case_change(df)
    elif choice == 5:
        duplicate_inspect(df)
    elif choice == 6:
        row_remove(df)
    elif choice == 7:
        column_remove(df)
    elif choice == 8:
        cell_update(df)
    elif choice == 9:
        df = sort_rows(df)
    elif choice == 10:
        show_column(df)
    elif choice == 11:
        change_column_value(df)
    elif choice == 12:
        save_file(df)
    elif choice == 13:
        quit()
    else:
        print("Invalid choice! Please enter a valid choice ranging from 1-13.")
