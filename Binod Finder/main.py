import os

def isBinod(filename):
    with open(filename, 'r') as f:
        content = f.read()
    if 'binod' in content.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    dir_content = os.listdir()
    # print(dir_content)
    count = 0
    for item in dir_content:
        if item.endswith('*'):
            print(f'Detecting Binod in {item}.')
            flag = isBinod(item)
            if flag:
                print(f'Binod is in {item}.')
                count += 1
            else:
                print(f'Binod is not find in {item}.')
    
    print(f'Summary of Binod is:-')
    print(f'total {count} Binod found.')