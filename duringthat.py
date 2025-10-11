import random
import datetime

def greet():
    names = ["Alex", "Jordan", "Taylor", "Sam", "Morgan"]
    name = random.choice(names)
    print(f"Hello, {name}! The time is {datetime.datetime.now().strftime('%H:%M:%S')}.")

def random_sum():
    nums = [random.randint(1, 10) for _ in range(3)]
    print(f"Numbers: {nums} → Sum: {sum(nums)}")

if __name__ == "__main__":
    greet()
    random_sum()
