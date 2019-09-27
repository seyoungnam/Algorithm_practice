package algoPractice;

public class FindPrime {
	//My answer1 = 테스트 실패
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
	//모범 답안
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
	//모범답안2
	 public int numberOfPrime(int n) {
	        int result = 0;
	        // 함수를 완성하세요.
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
