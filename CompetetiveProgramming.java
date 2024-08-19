// 1. Write a programming to find the number of permutations of consonants in a given string.
// 2. Write a program to find the count of number of words in a given string.
class CompetetiveProgramming {
    public static boolean isVowel(char c) {
        String vowels = "aeiou";
        c = Character.toLowerCase(c);
        return vowels.indexOf(c) != -1;
    }

    // public static boolean isVowel2(char c) {
    // String vowels = "AEIOU";
    // c = Character.toUpperCase(c);
    // return vowels.indexOf(c) != -1;
    // }

    // public static boolean isVowel3(char c) {
    // if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
    // c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
    // return true;
    // }
    // return false;
    // }

    // public static boolean isVowel4(char c) {
    // String vowels = "aeiouAEIOU";
    // return vowels.indexOf(c) != -1;
    // }

    public static int countConsonents(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!isVowel(s.charAt(i)) && Character.isAlphabetic(s.charAt(i))) {
                count++;
            }
        }
        return count;
    }

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        // ex: 4! = 4*3!
        return n * factorial(n - 1);
    }

    // public static int factorial2(int n) {
    // int fact = 1;
    // for (int i = 1; i <= n; i++) {
    // fact = fact * i;
    // }
    // return fact;
    // }
    public static int countWords(String s) {
        s = s.trim();
        if (s.length() == 0) {
            return 0;
        }
        int count = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String a = " UDAYA SREE     ";
        System.out.println(a.charAt(4));
        int consonentCount = countConsonents(a);
        int factorial = factorial(consonentCount);
        System.out.println("Words in " + a.trim() + " is " + countWords(a));
        System.out.println("Factorial of consonents in " + a.trim() + " is " + factorial);
    }
}
