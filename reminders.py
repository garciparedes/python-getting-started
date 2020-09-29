from time import sleep, time


def main():
    reminders = list()
    while True:
        command = input()
        for reminder in reminders:
            if reminder[1] - time() >= 0:
                continue
            reminder[0] = True
        reminders.sort()
        if command == "q":
            break
        elif command == "a":
            message = input("What to reminder? --> ")
            seconds = round(time()) + int(input("How many seconds? --> "))
            reminder = [False, seconds, message]
            reminders.append(reminder)
            print(f"Created a reminder!")
            print()
        elif command == "s":
            print("Remainders:")
            print("\tCompleted\tRemaining\tMessage")
            for reminder in reminders:
                print(f"\t{reminder[0]}\t\t{reminder[1] - round(time()):>9}\t{reminder[2]}")
            print()

        sleep(0.5)


if __name__ == '__main__':
    main()
