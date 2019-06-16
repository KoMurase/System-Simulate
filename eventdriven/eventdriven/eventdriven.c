#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define Rand() ((double)(rand()+1)/RAND_MAX) 
#define ernd(num) (-log(Rand())*(num))

#define END_TIME 7200.0
#define P1 10.0
#define P2 5.0 

typedef enum {
	E_ARRIVAL = 100,
	E_DEPARTURE
}event_type;

typedef struct _event {
	event_type type;
	double time;
	struct _event* next;
}event;

void e_arrival();
void e_departure();
void schedule(event_type type, int interval);

double time;
double l_time;
int total_queue;
int queue;
event top;

int main()
{
	event* current;

	/*(1)�@�������@*/

	time = 0.0;
	queue = 0.0;
	total_queue = 0;
	
	schedule(E_ARRIVAL, P1);

	while (time < END_TIME) {
		current = top.next;
		top.next = current->next;

		l_time = time;
		time = current->time;
		total_queue += (time - l_time) * queue;

		switch (current->type) {
		case E_ARRIVAL:
			e_arrival();
			break;
		case E_DEPARTURE:
			e_departure();

			break;
		default:
			break;

		}
		free(current);
	}
	/*(18) �Ō�ɏW�v�\��*/
	printf("Average = %lf\n", (double)total_queue / time);
	return 0;
}

void e_arrival()
{
	queue++;						/*�҂��s��ɒǉ�*/
	schedule(E_ARRIVAL, P1);		/*(1)���̓�����\��*/
	if (queue == 1) {					/*(2)�҂���Ȃ�(��������)*/
		schedule(E_DEPARTURE, P2);  /*(4)�����I���C�x���g��\��*/
	}
}

void e_departure()
{
	queue--;						/*�҂��s�񂩂玩������菜��*/
	if (queue != 0) {					/*(5)���̋q���҂��Ă���*/
		schedule(E_DEPARTURE, P2);		/*�����I���C�x���g��\��*/
	}
}

void schedule(event_type type, int interval)
{
	event *event0, * event1;
	event *pre_event1 = (event*)NULL;  /*event1�̑O�ɂ���C�x���g*/

	/*(19) �C�x���g���쐬*/
	event0 = (event*)malloc(sizeof(event));
	event0->type = type;
	event0->time = time + ernd((double)interval);
	event0->next = (event*)NULL;

	/*(20) �C�x���g���X�g�̍ŏ��̃C�x���g���擾*/
	event1 = top.next;
	pre_event1 = &top;

	while (1) {
		if (event1 == (event*)NULL) {
			pre_event1->next = event0;
			break;
		}
		else if (event0->time < event1->time) {
			pre_event1->next = event0;
			event0->next = event1;
			break;
		}
		pre_event1 = event1;
		event1 = event1->next;
	}
}
