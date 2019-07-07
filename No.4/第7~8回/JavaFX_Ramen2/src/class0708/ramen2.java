package class0708;

import java.util.Random;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;

public class ramen2 extends Application {
	int visitor;
	int runtime = 60*60*2+1;
	int count = 0;
	int line = 0;
	int maxline = 0;
	int num = 0;
	int finishnum = 0;
	int addseat = 2;
	int counter = 8;
	int linedata[] = new int[runtime];
	int visitors[] = new int[100];
	int staytime[] = new int[100];
	int congestion[][] = new int[counter+addseat][runtime];

	@Override
	public void start(Stage stage) {
		simulate();
		stage.setTitle("ƒ‰[ƒƒ“");
		final CategoryAxis xAxis = new CategoryAxis();
		if(maxline%5 != 0) {
			maxline = (int)(maxline/5)*5+5;
		}
		final NumberAxis yAxis = new NumberAxis(0, maxline, 5);
		xAxis.setLabel("ŠÔ");
		yAxis.setLabel("s—ñ‚Ì’·‚³");
		final BarChart<String, Number> BarChart = new BarChart<String, Number>(xAxis, yAxis);
		BarChart.setTitle("ƒ‰[ƒƒ“‚Ìs—ñ");		
		XYChart.Series series = new XYChart.Series();
		series.setName("s—ñ");
		for(int j=0; j<10; j++) {
			series.getData().add(new XYChart.Data("11:5"+j, 0));
		}
		for(int i=0; i<runtime; i++) {
			int hours = 12+(int)(i/3600);
			int minutes = 0+(int)(i/60);
			if(i>3600) {
			minutes = 0+(int)((i-3600)/60);
			}
			if(minutes<10) {
				series.getData().add(new XYChart.Data(hours+":0"+minutes, linedata[i]));
			}
			else {
				series.getData().add(new XYChart.Data(hours+":"+minutes, linedata[i]));
			}
		}
		Scene scene = new Scene(BarChart, 1200, 600);
		BarChart.getData().add(series);
		stage.setScene(scene);
		stage.show();
	}

	public void simulate() {
		Random rand = new Random();
		//visitor = rand.nextInt(8)+3;
		visitor = 10;
		for (int i=0; i<60/10; i++) {
			for (int j=0; j<visitor; j++) {
				visitors[count] = 600*i+rand.nextInt(601);
				staytime[count] = rand.nextInt(841)+600;
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
		
		for (int time=0; time<runtime; time++) {
			if (time==visitors[num]) {
				System.out.println("‹q(" + (num) + ")" + time + "•b—ˆ“X");
				line++;
				num++;
				System.out.println("‘Ò‚¿:" + line + "l");
			}
			if(line>0 && maxline<5) {
				for (int i=0; i<counter; i++) {
					if(congestion[i][time] == 0) {
						System.out.println("‹q(" + (finishnum) + ")" + time + "•b“ü“X"+time+"•b`"+(time+staytime[finishnum])+"•b");
						if ((time+staytime[finishnum])<runtime) {
							for (int j=time; j<(time+staytime[finishnum]); j++) {
								congestion[i][j] = 1;
							}
						} else {
							for (int j=time; j<runtime; j++) {
								congestion[i][j] = 1;
							}
						}
						line--;
						finishnum++;
						System.out.println("‘Ò‚¿:" + line + "l");
						break;
					}
				}
			}
			else if(line>0 && maxline>=5){
				for (int i=0; i<counter+addseat; i++) {
					if(congestion[i][time] == 0) {
						System.out.println("‹q(" + (finishnum) + ")" + time + "•b“ü“X"+time+"•b`"+(time+staytime[finishnum])+"•b");
						if ((time+staytime[finishnum])<runtime) {
							for (int j=time; j<(time+staytime[finishnum]); j++) {
								congestion[i][j] = 1;
							}
						} else {
							for (int j=time; j<runtime; j++) {
								congestion[i][j] = 1;
							}
						}
						line--;
						finishnum++;
						System.out.println("‘Ò‚¿:" + line + "l");
						break;
					}
				}
			}
			if(time==visitors[num] && visitors[num]==visitors[num-1]) {
				time-=1;
				continue;
			}
			linedata[time] = line;
			if(maxline<line) {
				maxline = line;
			}
		}
		for (int i=0; i<count; i++) {
			System.out.print(visitors[i] + ", ");
		}
		System.out.println("\n" + count + "l");
	}

	public static void main(String[] args) {
		launch(args);
	}
}