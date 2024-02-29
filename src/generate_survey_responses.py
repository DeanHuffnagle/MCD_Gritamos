import random
import config.config as conf


def generate_response(num):
    length = len(conf.RESPONSE_SIGNATURE)
    index = num % length
    string = f'{random.choice(conf.RESPONSE_PART_ONE)} ' \
             f'{random.choice(conf.RESPONSE_PART_TWO)} ' \
             f'{random.choice(conf.RESPONSE_PART_THREE)} ' \
             f'{conf.RESPONSE_SIGNATURE[index]}'
    return string

if __name__ == "__main__":
    i=0
    while(i<10):
        print(generate_response(i))
        i+=1
