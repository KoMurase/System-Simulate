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

	/*(1)　初期化　*/

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
	/*(18) 最後に集計表示*/
	printf("Average = %lf\n", (double)total_queue / time);
	return 0;
}

void e_arrival()
{
	queue++;						/*待ち行列に追加*/
	schedule(E_ARRIVAL, P1);		/*(1)次の到着を予定*/
	if (queue == 1) {					/*(2)待ち列なし(自分だけ)*/
		schedule(E_DEPARTURE, P2);  /*(4)処理終了イベントを予定*/
	}
}

void e_departure()
{
	queue--;						/*待ち行列から自分を取り除く*/
	if (queue != 0) {					/*(5)次の客が待っている*/
		schedule(E_DEPARTURE, P2);		/*処理終了イベントを予定*/
	}
}

void schedule(event_type type, int interval)
{
	event *event0, * event1;
	event *pre_event1 = (event*)NULL;  /*event1の前にあるイベント*/

	/*(19) イベントを作成*/
	event0 = (event*)malloc(sizeof(event));
	event0->type = type;
	event0->time = time + ernd((double)interval);
	event0->next = (event*)NULL;

	/*(20) イベントリストの最初のイベントを取得*/
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
