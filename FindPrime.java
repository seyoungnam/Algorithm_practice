package algoPractice;

public class FindPrime {
	//My answer1 = �׽�Ʈ ����
	public static int solution(int n) {
		int answer = 0;
		for(int i=2; i<=n; i++) {
			boolean flag = true;
			for(int j=2; j<i; j++) {
				if(i%j == 0) {
					flag = false;
					break;
				}
			}
			if(flag) {
				answer++;
			}
		}
		return answer;
	}
	
	//My answer2
	public static int solution2(int n) {
		int answer = 0;
		for(int i=2; i<=n; i++) {
			boolean flag = true;
			for(int j=2; j<=Math.sqrt(i); j++) {
				if(i%j == 0) {
					flag = false;
					break;
				}
			}
			if(flag) {
				answer++;
			}
		}
		return answer;
	}
	//��� ���
	public int numberOfPrime(int n) {
        int result = 0;
        for(int i=2; i<=n; i++){
        for(int j=2; j<=i; j++){
        if(j == i){
            ++result;
        } else if(i%j == 0){
            break;
        }
      }
    }

        return result;
    }
	//������2
	 public int numberOfPrime(int n) {
	        int result = 0;
	        // �Լ��� �ϼ��ϼ���.
	    for(int i=2; i<=n; i++){
	      for(int j=1; j<=Math.sqrt(i); j++){
	        if((j != 1) & (i % j == 0)){
	          break;
	        } else if(j+1 > Math.sqrt(i)){
	          result++;
	        }
	      }
	    }
	        return result;
	    }

	public static void main(String[] args) {
		System.out.println(solution(10));
		System.out.println(solution(10));
		
		
		

	}

}
