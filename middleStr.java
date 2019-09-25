package algoPractice;

public class middleStr {
	
	/*���� ����
	�ܾ� s�� ��� ���ڸ� ��ȯ�ϴ� �Լ�, solution�� ����� ������. �ܾ��� ���̰� ¦����� ��� �α��ڸ� ��ȯ�ϸ� �˴ϴ�.

	���ѻ���
	s�� ���̰� 1 �̻�, 100������ ��Ʈ���Դϴ�.
	����� ��
	"abcde" -> "c"
	"qwer" -> "we"*/
	
	//My answer
	public static String getMiddle(String example) {
		String answer = null;
		int length = example.length();
		int loc = length/2;
		if(length%2 == 0) {
			answer = example.substring(loc-1, loc+1);
	    }else {
		    answer = example.substring(loc, loc+1);
	    }		
		return answer;
	}
	
	//reference 1
	// https://wayhome25.github.io/algorithm/2017/06/10/mid-char/
	public static String getMiddle1(String word){
	    int len = word.length();
	    if (len % 2 == 1){
	      // return word.charAt(len/2)+"";
	      // char > Stirng ����ȯ
	      // Least efficient and most memory-inefficient, but common amongst beginners because of its simplicity
	      return Character.toString(word.charAt(len/2)); //  Most efficient way
	    }else{
	      return word.substring(len/2-1, len/2+1);        
	    }
	  }
	
	//reference 2
	// https://wayhome25.github.io/algorithm/2017/06/10/mid-char/
	public static String getMiddle2(String word) {
		int length = word.length();
		int index = length / 2;
		return (length % 2 == 0) ? word.substring(index - 1, index + 1) : word.substring(index, index + 1);
	}
	
	public static void main(String[] args) {
		
		System.out.println(getMiddle("abcde"));
		System.out.println(getMiddle("qwer"));
		
		System.out.println(getMiddle1("abcde"));
		System.out.println(getMiddle1("qwer"));
		
		System.out.println(getMiddle2("abcde"));
		System.out.println(getMiddle2("qwer"));
	}

}
