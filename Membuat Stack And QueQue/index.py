from collections import deque

print("=" * 5, "CONTOH 1: STACK", "=" * 5)
X = [1, 2, 3, 4, 5, 6]
print("Data Sekarang : ", X)

# Memasukkan Data Baru
X.append(7)
print("Data Masuk    : ", 7)
print("Data Sekarang : ", X)

X.append(8)
print("Data Masuk    : ", 8)
print("Data Sekarang : ", X)

# Mengeluarkan Data Yang Terakhir
X.pop() 
print("Data Sekarang : ", X)

# Stacking
Y = X.pop()
print("Data Keluar   : ", Y)
print("Data Sekarang : ", X)

print('\n')

#=========================================
print("=" * 5, "CONTOH 2: QUEUE", "=" * 5)

Antrian = deque([1,2,3,4,5])
print("Data Sekarang : ", Antrian)

# Menambahkan Data
Antrian.append(6)
print("Data Masuk    : ", 6)
print("Data Sekarang : ", Antrian)

Antrian.append(7)
print("Data Masuk    : ", 7)
print("Data Sekarang : ", Antrian)

# Mengurangi Antrian
Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Antrian.append(8)
print("Data Masuk    : ", 8)
print("Data Sekarang : ", Antrian)


print("\n")
print("=" * 5, "INTERTACTIVE PROGRAM STACK AND QUEUE", "=" * 5)
# STACK AND QUEUE IN PYTHON (INTERACTIVE)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack Kosong!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack Kosong!"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if self.is_empty():
            return "Queue Kosong!"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue Kosong!"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("\nPilih struktur data yang akan digunakan:")
        print("1. Stack")
        print("2. Queue")
        print("3. Keluar")
        choice = input("Masukkan pilihan Anda (1/2/3): ")

        if choice == "1":
            while True:
                print("\nStack Operations:")
                print("1. Push (tambahkan)")
                print("2. Pop (hapus element paling atas)")
                print("3. Peek (intip)")
                print("4. Display (tampilkan)")
                print("5. Back")
                stack_choice = input("Masukkan pilihan Anda (1/2/3/4/5): ")

                if stack_choice == "1":
                    value = input("Masukkan nilai yang akan di push: ")
                    stack.push(value)
                    print(f"Stack: {stack.display()}")

                elif stack_choice == "2":
                    print(f"Popped: {stack.pop()}")
                    print(f"Stack: {stack.display()}")

                elif stack_choice == "3":
                    print(f"Element paling atas: {stack.peek()}")

                elif stack_choice == "4":
                    print(f"Stack: {stack.display()}")

                elif stack_choice == "5":
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi!")

        elif choice == "2":
            while True:
                print("\nQueue Operations:")
                print("1. Enqueue (tambahkan element)")
                print("2. Dequeue (hapus element paling depan)")
                print("3. Front (intip)")
                print("4. Display (tampilkan)")
                print("5. Back")
                queue_choice = input("Masukkan pilihan Anda (1/2/3/4/5): ")

                if queue_choice == "1":
                    value = input("Masukkan nilai ke-1 yang akan di enqueue: ")
                    queue.enqueue(value)
                    print(f"Queue: {queue.display()}")

                elif queue_choice == "2":
                    print(f"Dequeued: {queue.dequeue()}")
                    print(f"Queue: {queue.display()}")

                elif queue_choice == "3":
                    print(f"Element paling depan: {queue.front()}")

                elif queue_choice == "4":
                    print(f"Queue: {queue.display()}")

                elif queue_choice == "5":
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi!")

        elif choice == "3":
            print("Keluar... Goodbye, Semoga dapat membantu pengetahuan anda!")
            break

        else:
            print("Pilihan tidak valid. Coba lagi!")


if __name__ == "__main__":
    main()
