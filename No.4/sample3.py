person = []
seat=[0]*8
q_length = 0
time =0
limit=100
import random
def visit_person(kaisuu):
    for i in range(kaisu):
        r_time = random.randint(0,100)
        person.append(r_time)
        print(person)
        person.sort()
        print(person)

def main():
    visit_person(20)
    while time<limit :
        for i in range(20):
            for time in range(100):
                for k in range(8):
                    if person[i]==time and seat[k] ==0:
                        seat[k] == 1
                        print(seat)

                    elif person[i]==time and seat[k]==1:
                        person[i]+=17
                        q_length+=1
                        print('person[%d]の状況',person[i])

        time+=1
