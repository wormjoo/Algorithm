import java.util.Scanner;
import java.util.Stack;

class StringEdit {
	public int cost[][]; // 편집 최소비용 표
	public char edit[][]; // 편집 표
	public int order_i[]; // cost(i, j)에서의 i를 담은 배열
	public int order_j[]; // cost(i, j)에서의 j를 담은 배열
	public int size; // 편집 거리

	public int getMin(int i, int j, int a, int b, int c) { // 최소 비용 선택
		int min;
		if (a <= b) { 
			if (a <= c) {
				min = a;
				edit[i][j] = 'D'; // Delete(삭제)
			}
			else {
				min = c;
				edit[i][j] = 'I'; // Insert(삽입)
			}
		}
		else {
			if (c >= b) {
				min = b;
				edit[i][j] = 'C'; // Change(교체)
			}
			else {
				min = c;
				edit[i][j] = 'I'; // Insert(삽입)
			}
		}
		return min; // 최소 반환
	}
	
	public void createTable(int n, int m, String x, String y) { // cost, edit 표 생성
		cost = new int[n+1][m+1]; // cost 동적할당
		edit = new char[n+1][m+1]; // edit 동적할당
		cost[0][0] = 0; // i = j = 0 : cost(i,j) = 0
		edit[0][0] = '-'; //i = j = 0 : edit(i,j) = '-'
		for (int i = 1; i <= n; i++) { // i > 0, j = 0 : x_i 를 삭제한다.
			cost[i][0] = cost[i-1][0] + 1;
			edit[i][0] = 'D';
		}
		for (int j = 1; j <= m; j++) { // i = 0, j > 0 : y_j 를 삽입한다.
			cost[0][j] = cost[0][j-1] + 1;
			edit[0][j] = 'I';
		}
		for (int i = 1; i <= n; i++) { // i > 0, j > 0 : 다음의 3가지 경우 중 비용이 최소가 되는 것을 선택
			for (int j = 1; j <= m; j++) {
				if (x.charAt(i-1) == y.charAt(j-1)) {
					cost[i][j] = cost[i-1][j-1]; // // x_i = y_j 이면 C(x_i) = 0
					edit[i][j] = 'C'; // Change(교체)
				}
				else {
					cost[i][j] = getMin(i, j, cost[i-1][j]+1, cost[i-1][j-1]+2, cost[i][j-1] + 1);
				}
			}
		}
		
		System.out.println();
		System.out.println("-- COST --"); // cost 표 출력
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= m; j++) {
				System.out.print(cost[i][j] + " ");
			}
			System.out.println();
		}
		
		System.out.println();
		System.out.println("-- EDIT --"); // edit 표 출력
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= m; j++) {
				System.out.print(edit[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public void backTrace(int n, int m) { // 역추적으로 구한 최적의 편집 순서열
		int i = n;
		int j = m;
		
		Stack<Integer> stack_i = new Stack<>(); // i를 담을 스택 생성
		Stack<Integer> stack_j = new Stack<>(); // j를 담을 스택 생성
		
		while (!(i==0 && j==0)) {
			switch(edit[i][j]) {
			case 'C': // 교체인 경우
				i = i - 1;
				j = j - 1;
				break;
			case 'D': // 삭제인 경우
				i = i - 1;
				break;
			case 'I': // 삽입인 경우
				j = j - 1;
				break;
			}
			stack_i.push(i);
			stack_j.push(j);
		}
		size = stack_i.size(); // 편집 거리
		order_i = new int[size+1];
		order_j = new int[size+1];
		
		for (int k = 0; k < size; k++) { // 역으로 편집 순서 넣기 위해 스택 pop
			order_i[k] = stack_i.pop();
			order_j[k] = stack_j.pop();
		}
		
		order_i[size] = n; // 최종 순서
		order_j[size] = m; // 최종 순서
		
		for (int k = 0; k <= size; k++) // 최적의 편집 순서열 출력
			System.out.print("(" + order_i[k] + ", " + order_j[k] + ") ");
		System.out.println();
		System.out.println();
	}
	
	public void Apply(String x, String y) { // 입력 문자열에 차례로 적용
		StringBuffer apply = new StringBuffer(); // 적용된 문자열을 담을 버퍼
		apply.append(x); // 처음에 x로 시작
		char add; // y 삽입 시 그때의 y_j 문자
		
		System.out.println("(" + order_i[0] + ", " + order_j[0] + ") : " + apply);
		for (int k = 1; k <= size; k++) {
			if ((order_i[k] == order_i[k-1]+1) && (order_j[k] == order_j[k-1]+1)) { // 대각선 아래로 이동 : 문자열 변화 없음
				System.out.println("(" + order_i[k] + ", " + order_j[k] + ") : " + apply);
			}
			else if ((order_i[k] == order_i[k-1]+1) && (order_j[k] == order_j[k-1])) { // 아래로 이동 : x_i 삭제
				String str_apply = apply.toString();
				for (int i = order_i[k]-1; i<size; i++) {
					if (str_apply.charAt(i) == x.charAt(order_i[k]-1)) {
						apply.delete(i,  i+1);
						break;
					}
				}
				System.out.println("(" + order_i[k] + ", " + order_j[k] + ") : " + apply);
			}
			else if ((order_i[k] == order_i[k-1]) && (order_j[k] == order_j[k-1]+1)) { // 오른쪽으로 이동 : y_i 삽입
				if (order_j[k] == 1) { // x_1 앞에 삽입
					add = y.charAt(order_j[k]-1);
					apply.insert(0, add);
				}
				else if (order_j[k] == size) { // x 뒤에 삽입
					add = y.charAt(order_j[k]-1);
					apply.append(add);
				}
				else { // x 중간에 삽입
					add = y.charAt(order_j[k]-1);
					apply.insert(order_j[k]-1, add);
				}
				System.out.println("(" + order_i[k] + ", " + order_j[k] + ") : " + apply);
			}
		}
	}
}

public class report4 {
	public static void main(String[] args) {
		int n, m; // 두 문자열 각가의 길이
		String x, y; // 두 문자열
		
		Scanner sc = new Scanner(System.in);
		StringEdit se = new StringEdit(); // class 객체 생성
		
		System.out.print("두 문자열의 길이를 입력 : ");
		n = sc.nextInt();
		m = sc.nextInt();
		System.out.print("두 문자열을 입력 : ");
		x = sc.next();
		y = sc.next();
		
		se.createTable(n, m, x, y);
		System.out.print("최적의 편집 순서열 : ");
		se.backTrace(n, m);
		System.out.println("입력 문자열에 차례로 적용하기 :");
		se.Apply(x, y);
	}
}
