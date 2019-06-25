package class0708;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;

public class ramen extends Application {
	int visitor;
	int runtime = 60*60*2;
	int count = 0;
	int line = 0;
	int num = 0;
	int waitnum = 0;
	int fillcounter;
	int counter = 8;
	int linedata[] = new int[runtime];
	int visitors[] = new int[100];
	int finishtime[] = new int[100];
	int staytime[] = new int[100];
	int waittime[] = new int[100];
	int congestion[][] = new int[counter][runtime];

	@Override
	public void start(Stage stage) {
		simulate();
		stage.setTitle("ƒ‰[ƒƒ“");
		final NumberAxis xAxis = new NumberAxis();
		final NumberAxis yAxis = new NumberAxis();
		xAxis.setLabel("ŠÔ");
		yAxis.setLabel("s—ñ‚Ì’·‚³");
		final LineChart<Number, Number> lineChart = new LineChart<Number, Number>(xAxis, yAxis);
		lineChart.setTitle("ƒ‰[ƒƒ“‚Ìs—ñ");		
		XYChart.Series series = new XYChart.Series();
		series.setName("s—ñ");		
		for(int i=0; i<runtime; i++) {
			series.getData().add(new XYChart.Data(i, linedata[i]));
		}
		Scene scene = new Scene(lineChart, 800, 600);
		lineChart.getData().add(series);
		stage.setScene(scene);
		stage.show();
	}

	public void simulate() {
		visitor = (int) (Math.random() * 8) + 3;
		for (int i=0; i<60/10; i++) {
			for (int j=0; j<visitor; j++) {
				visitors[count] = 600*i+(int)(Math.random()*601);
				staytime[count] = 60*17;
				count++;
			}
		}
		for (int i=0; i<count-1; i++) {
			for (int j=count-1; j>i; j--) {
				if (visitors[j-1]>visitors[j]) {
					int tmp1 = visitors[j-1];
					visitors[j-1] = visitors[j];
					visitors[j] = tmp1;
					int tmp2 = staytime[j-1];
					staytime[j-1] = staytime[j];
					staytime[j] = tmp2;
				}
			}
		}
		for (int i=0; i<count; i++) {
			System.out.print(visitors[i] + ", ");
		}
		System.out.println("\n" + count + "l");

		for (int time=0; time<runtime; time++) {
			if (time==visitors[num]) {
				System.out.println("‹q(" + (num) + ")" + time + "•b—ˆ“X");
				line++;
				num++;
				System.out.println("‘Ò‚¿:" + line + "l");
				if(visitors[num]==visitors[num]) {
					time--;
					continue;
				}
			}
			if (time==visitors[waitnum]+waittime[waitnum]) {
				for (int i=0; i<counter; i++) {
					if (congestion[i][time]==0) {
						System.out.println("‹q(" + (waitnum) + ")" + time + "•b“ü“X"+(visitors[waitnum]+waittime[waitnum])+"•b`"+(visitors[waitnum]+waittime[waitnum]+staytime[waitnum])+"•b");
						if (visitors[waitnum]+waittime[waitnum]+staytime[waitnum]<runtime) {
							for (int j=visitors[waitnum]+waittime[waitnum]; j<visitors[waitnum]+waittime[waitnum]+staytime[waitnum]; j++) {
								congestion[i][j] = 1;
								finishtime[waitnum] = visitors[waitnum] + waittime[waitnum] + staytime[waitnum];
							}
						} else {
							for (int j=visitors[waitnum]+waittime[waitnum]; j<runtime; j++) {
								congestion[i][j] = 1;
								finishtime[waitnum] = runtime;
							}
						}
						if (line>0) {
							line--;
						}
						System.out.println("‘Ò‚¿:" + line + "l");
						waitnum++;
						break;
					}
				}
			}
			for (int i=0; i<waitnum-1; i++) {
				for (int j=waitnum-1; j>i; j--) {
					if (finishtime[j-1]>finishtime[j]) {
						int tmp = finishtime[j-1];
						finishtime[j-1] = finishtime[j];
						finishtime[j] = tmp;
					}
				}
			}
			fillcounter = 0;
			for (int k=0; k < counter; k++) {
				if (congestion[k][time]==1 && line>0) {
					fillcounter++;
				}
				if (fillcounter==counter) {
					waittime[waitnum] = finishtime[waitnum - counter]-visitors[waitnum];
				}
			}
			linedata[time] = line;
		}
		for (int i=0; i<count; i++) {
			System.out.print(visitors[i] + ", ");
		}
		System.out.print("\n");
		for (int i=0; i<count; i++) {
			System.out.print(finishtime[i] + ", ");
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
