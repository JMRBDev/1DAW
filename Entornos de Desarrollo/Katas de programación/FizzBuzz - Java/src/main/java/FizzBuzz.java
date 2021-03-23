public class FizzBuzz {
    boolean fizz(int num) {
        if (num % 3 == 0) {
            return true;
        }
        return false;
    }

    boolean buzz(int num) {
        if (num % 5 == 0) {
            return true;
        }
        return false;
    }

    boolean fizz_buzz(int num) {
        if (fizz(num) && buzz(num)) {
            return true;
        }
        return false;
    }
}
