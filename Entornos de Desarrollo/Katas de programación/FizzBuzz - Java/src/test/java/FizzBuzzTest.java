import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {
    @Test
    public void test_multiplo_3() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.fizz(3);
        assertTrue(esMultiplo);
    }

    @Test
    public void test_no_multiplo_3() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.fizz(7);
        assertFalse(esMultiplo);
    }

    @Test
    public void test_multiplo_5() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.buzz(5);
        assertTrue(esMultiplo);
    }

    @Test
    public void test_no_multiplo_5() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.buzz(7);
        assertFalse(esMultiplo);
    }

    @Test
    public void test_fizz_buzz() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.buzz(15);
        assertTrue(esMultiplo);
    }

    @Test
    public void test_no_fizz_buzz() {
        FizzBuzz fb = new FizzBuzz();
        boolean esMultiplo = fb.buzz(16);
        assertFalse(esMultiplo);
    }
}