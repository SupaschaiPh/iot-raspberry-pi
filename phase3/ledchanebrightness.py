import read , pwm ,time
def main():
    read0 = (read.ReadChannel(0)/4095)*100
    print(read0)
    pwm.changeCycle(read0)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(0.5)
